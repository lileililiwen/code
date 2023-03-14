<?php
class AggregatedImageHostingService {
  private $services;
  private $retryCount;

  public function __construct($services, $retryCount = 3) {
    $this->services = $services;
    $this->retryCount = $retryCount;
  }

  public function uploadImage($imageData) {
    foreach ($this->services as $service) {
      for ($i = 0; $i <= $this->retryCount; $i++) {
        try {
          $imageUrl = $service->uploadImage($imageData);
          return $imageUrl;
        } catch (Exception $e) {
          // 图床服务不可用，尝试下一个服务
          continue;
        }
      }
    }

    // 所有图床服务均不可用
    throw new Exception('Unable to upload image to any hosting service');
  }
}

interface ImageHostingService {
  public function uploadImage($imageData);
}

class PrimaryImageHostingService implements ImageHostingService {
  public function uploadImage($imageData) {
    // 实现优先级最高的图床服务上传逻辑
  }
}

class SecondaryImageHostingService implements ImageHostingService {
  public function uploadImage($imageData) {
    // 实现次优先级的图床服务上传逻辑
  }
}

// 配置聚合图床服务
$primaryService = new PrimaryImageHostingService();
$secondaryService = new SecondaryImageHostingService();
$services = array($primaryService, $secondaryService);
$aggregatedService = new AggregatedImageHostingService($services);

// 上传图片
$imageData = file_get_contents('example.png');
$imageUrl = $aggregatedService->uploadImage($imageData);
echo 'Uploaded image URL: ' . $imageUrl;