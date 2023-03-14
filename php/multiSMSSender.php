<?php 
// 定义 SmsGateway 接口
interface SmsGateway {
    public function send($to, $message);
}

// 实现 TwilioGateway 类
class TwilioGateway implements SmsGateway {
    public function send($to, $message) {
        // 使用 Twilio API 发送短信
    }
}

// 实现 NexmoGateway 类
class NexmoGateway implements SmsGateway {
    public function send($to, $message) {
        // 使用 Nexmo API 发送短信
    }
}

// 实现 SmsRouter 类
class SmsRouter {
    private $gateways = array();
    
    public function addGateway($gateway) {
        $this->gateways[] = $gateway;
    }
    
    public function send($to, $message, $gatewayName = null) {
        // 如果指定了网关，则路由到指定的网关
        if ($gatewayName !== null) {
            foreach ($this->gateways as $gateway) {
                if (get_class($gateway) === $gatewayName) {
                    $gateway->send($to, $message);
                    return;
                }
            }
            throw new Exception("Invalid gateway name: $gatewayName");
        }
        
        // 否则使用负载均衡算法路由到最空闲的网关
        usort($this->gateways, function($a, $b) {
            return $a->getQueueSize() <=> $b->getQueueSize();
        });
        $this->gateways[0]->send($to, $message);
    }
}

// 在 config.php 文件中定义网关的凭据和其他配置信息
$twilioConfig = array(
    'accountSid' => '...',
    'authToken' => '...',
    'fromNumber' => '...'
);
$nexmoConfig = array(
    'apiKey' => '...',
    'apiSecret' => '...',
    'fromNumber' => '...'
);

// 创建 TwilioGateway 和 NexmoGateway 实例，并添加到 SmsRouter 中
$twilio = new TwilioGateway($twilioConfig);
$nexmo = new NexmoGateway($nexmoConfig);
$router = new SmsRouter();
$router->addGateway($twilio);
$router->addGateway($nexmo);

// 在主应用程序中使用 SmsRouter 发送短信
$router->send('1234567890', 'Hello World!', 'TwilioGateway');

?>