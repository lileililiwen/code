<?php 
class MultiLevelCache {
    const DEFAULT_EXPIRATION_TIME = 3600; // 缓存默认过期时间，单位秒
    const MAX_RETRY_COUNT = 3; // 最大重试次数
  
    private $cacheConfigs; // 缓存配置数组
    private $cacheProviders = []; // 缓存供应商数组
    private $localCache = []; // 本地缓存数组
  
    public function __construct($cacheConfigs) {
      $this->cacheConfigs = $cacheConfigs;
    }
  
    // 获取缓存值
    public function get($key) {
      // 先从本地缓存中查找
      if (isset($this->localCache[$key])) {
        return $this->localCache[$key];
      }
  
      // 从优先级缓存开始查找
      foreach ($this->cacheProviders as $provider) {
        $value = $provider->get($key);
        if ($value !== null) {
          // 缓存命中，更新本地缓存并返回值
          $this->localCache[$key] = $value;
          return $value;
        }
      }
  
      // 所有缓存都没有命中，路由到数据库
      $value = $this->getFromDatabase($key);
      if ($value !== null) {
        // 从数据库获取到值，更新缓存并返回值
        $this->localCache[$key] = $value;
        $this->cacheProviders[0]->set($key, $value);
        return $value;
      }
  
      return null;
    }
  
    // 设置缓存值
    public function set($key, $value, $expiration = self::DEFAULT_EXPIRATION_TIME) {
      $this->localCache[$key] = $value;
      foreach ($this->cacheProviders as $provider) {
        $provider->set($key, $value, $expiration);
      }
    }
  
    // 删除缓存值
    public function delete($key) {
      unset($this->localCache[$key]);
      foreach ($this->cacheProviders as $provider) {
        $provider->delete($key);
      }
    }
  
    // 根据配置获取优先级最高的缓存供应商
    private function getPriorityProvider() {
      // 如果没有配置，则返回空
      if (empty($this->cacheConfigs)) {
        return null;
      }
  
      // 按照优先级排序
      $sortedConfigs = $this->cacheConfigs;
      usort($sortedConfigs, function ($a, $b) {
        return $b['priority'] - $a['priority'];
      });
  
      // 获取优先级最高的缓存供应商
      foreach ($sortedConfigs as $config) {
        $provider = $this->getProvider($config);
        if ($provider !== null) {
          return $provider;
        }
    }
  
 // 根据配置获取缓存供应商
 private function getProvider($config) {
    if (!isset($config['type'])) {
      return null;
    }

    switch ($config['type']) {
      case 'redis':
        $provider = $this->createRedisProvider($config);
        break;
      case 'memcached':
        $provider = $this->createMemcachedProvider($config);
        break;
      default:
        $provider = null;
        break;
    }

    return $provider;
  }

  // 创建Redis缓存供应商
  private function createRedisProvider($config) {
    if (!extension_loaded('redis')) {
      return null;
    }

    $redis = new Redis();
    if (!$redis->connect($config['host'], $config['port'])) {
      return null;
    }

    if (isset($config['password'])) {
      $redis->auth($config['password']);
    }

    if (isset($config['database'])) {
      $redis->select($config['database']);
    }

    return new RedisCacheProvider($redis);
  }

  // 创建Memcached缓存供应商
  private function createMemcachedProvider($config) {
    if (!extension_loaded('memcached')) {
      return null;
    }

    $memcached = new Memcached();
    if (!$memcached->addServer($config['host'], $config['port'])) {
      return null;
    }

    return new MemcachedCacheProvider($memcached);
  }

  // 从数据库获取值
  private function getFromDatabase($key) {
    // TODO: 从数据库获取值
    return null;
  }

  // 初始化缓存供应商数组
  private function initCacheProviders() {
    foreach ($this->cacheConfigs as $config) {
      $provider = $this->getProvider($config);
      if ($provider !== null) {
        $this->cacheProviders[] = $provider;
      }
    }
  }

  // 重试获取缓存值
  private function retryGet($key) {
    $retryCount = 0;
    while ($retryCount < self::MAX_RETRY_COUNT) {
      $provider = $this->getPriorityProvider();
      if ($provider === null) {
        break;
      }

      $value = $provider->get($key);
      if ($value !== null) {
        $this->localCache[$key] = $value;
        return $value;
      }

      $retryCount++;
    }

    return null;
  }

  // 获取缓存值，支持重试
  public function getWithRetry($key) {
    // 先从本地缓存中查找
    if (isset($this->localCache[$key])) {
      return $this->localCache[$key];
    }

    // 重试获取缓存值
    $value = $this->retryGet($key);
    if ($value !== null) {
      return $value;
    }

    // 所有缓存都没有命中，路由到数据库
    $value = $this->getFromDatabase($key);
    if ($value !== null) {
      // 从数据库获取到值，更新缓存并返回值
      $this->localCache[$key] = $value;
      $this->cacheProviders[0]->set($key, $value);
      return $value;
    }

    return null;
  }
}

// 缓存供应商接口
interface CacheProvider {
  public function get($key);
  public function set($key
}
// Redis缓存供应商
class RedisCacheProvider implements CacheProvider {
    private $redis;
    
    public function __construct($redis) {
        $this->redis = $redis;
    }
    
    public function get($key) {
        return $this->redis->get($key);
    }
    
    public function set($key, $value) {
     return $this->redis->set($key, $value);
    }
}
    
// Memcached缓存供应商
class MemcachedCacheProvider implements CacheProvider {
    private $memcached;
    
    public function __construct($memcached) {
        $this->memcached = $memcached;
    }
    
    public function get($key) {
        return $this->memcached->get($key);
    }
    
    public function set($key, $value) {
        return $this->memcached->set($key, $value);
    }
}
    
// 使用示例
$configs = array(
    array(
    'type' => 'redis',
    'host' => '127.0.0.1',
    'port' => 6379,
    ),
    array(
    'type' => 'memcached',
    'host' => '127.0.0.1',
    'port' => 11211,
    ),
);

$cache = new MultiLevelCache($configs);
$value = $cache->getWithRetry('my_key');
if ($value === null) {
    echo 'Not found';
} else {
    echo $value;
}
?>