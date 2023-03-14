<?php 

class ConnectionManager {
    private $master;
    private $slaves;
  
    public function __construct($masterConfig, $slaveConfigs) {
      // 连接主库
      $this->master = new PDO(
        "mysql:host={$masterConfig['host']};dbname={$masterConfig['database']}",
        $masterConfig['username'],
        $masterConfig['password']
      );
      
      // 连接从库
      foreach ($slaveConfigs as $config) {
        $this->slaves[] = new PDO(
          "mysql:host={$config['host']};dbname={$config['database']}",
          $config['username'],
          $config['password']
        );
      }
    }
  
    public function getMaster() {
      return $this->master;
    }
  
    public function getSlave() {
      $slaveCount = count($this->slaves);
      if ($slaveCount === 0) {
        return $this->master;
      } else {
        return $this->slaves[rand(0, $slaveCount - 1)];
      }
    }
  }

  class ShardingDatabase {
    private $connectionManager;
    private $shardCount;
  
    public function __construct($connectionManager, $shardCount) {
      $this->connectionManager = $connectionManager;
      $this->shardCount = $shardCount;
    }
  
    public function findById($id) {
      $shardId = $id % $this->shardCount;
      $statement = $this->connectionManager->getSlave()->prepare(
        "SELECT * FROM `user_{$shardId}` WHERE `id` = :id"
      );
      $statement->execute(['id' => $id]);
      return $statement->fetch(PDO::FETCH_ASSOC);
    }
  
    public function insert($data) {
      $shardId = $data['id'] % $this->shardCount;
      $statement = $this->connectionManager->getMaster()->prepare(
        "INSERT INTO `user_{$shardId}` (`id`, `name`) VALUES (:id, :name)"
      );
      $statement->execute(['id' => $data['id'], 'name' => $data['name']]);
    }
  
  ?>