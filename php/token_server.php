<?php
// 获取机器码和token
$machineCode = $_GET['machineCode'];
$token = $_POST['token'];

// 校验token
$result = checkToken($machineCode, $token);

// 返回校验结果
echo $result ? 'true' : 'false';

// 校验token的函数
function checkToken($machineCode, $token) {
  // 这里假设密钥为'my_secret_key'
  $secretKey = 'my_secret_key';

  // 获取当前时间戳
  $timestamp = time();

  // 从token中解析出token生成时间和签名
  list($generatedTimestamp, $signature) = explode('|', $token);

  // 计算token失效时间，这里假设token有效期为1天
  $expires = strtotime('+1 day', (int)$generatedTimestamp);

  // 判断token是否已过期
  if ($timestamp > $expires) {
    return false;
  }

  // 生成本地token
  $localToken = generateToken($machineCode, $secretKey, $generatedTimestamp);

  // 比较本地token和客户端传来的token
  return $localToken == $token;
}

// 生成token的函数
function generateToken($machineCode, $secretKey,$generatedTimestamp) {
    // 计算签名
    $signature = md5($machineCode . $secretKey . $generatedTimestamp);
    
    // 将签名和token生成时间拼接成token
    return $generatedTimestamp . '|' . $signature;
    }
?>