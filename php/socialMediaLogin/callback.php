<?php

session_start();

// 微信开放平台应用的 AppID 和 AppSecret
$wechatAppID = 'your_wechat_app_id';
$wechatAppSecret = 'your_wechat_app_secret';

// 回调地址，微信授权成功后将跳转到此地址
$redirectUrl = 'http://example.com/callback.php';

// 获取 access_token 和 openid 的 API URL
$accessTokenUrl = 'https://api.weixin.qq.com/sns/oauth2/access_token';

// 获取用户信息的 API URL
$userInfoUrl = 'https://api.weixin.qq.com/sns/userinfo';

// 如果微信授权成功，将返回 code 和 state 参数
if (isset($_GET['code']) && isset($_GET['state'])) {
    // 检查 state 参数是否与当前页面 URL 相同，防止 CSRF 攻击
    if ($_GET['state'] != $_SERVER['REQUEST_URI']) {
        header('HTTP/1.1 400 Bad Request');
        echo 'Invalid request.';
        exit;
    }

    // 构造获取 access_token 和 openid 的 API 请求
    $accessTokenParams = array(
        'appid' => $wechatAppID,
        'secret' => $wechatAppSecret,
        'code' => $_GET['code'],
        'grant_type' => 'authorization_code'
    );
    $accessTokenUrl .= '?' . http_build_query($accessTokenParams);

    // 发送 API 请求，并解析
    $response = file_get_contents($access_token_url);
    $response = json_decode($response, true);
 
    if (isset($response['access_token']) && isset($response['openid'])) {
        $access_token = $response['access_token'];
        $openid = $response['openid'];
    
        // 获取用户信息
        $user_info_url = 'https://api.weixin.qq.com/sns/userinfo';
        $user_info_url .= '?access_token=' . $access_token;
        $user_info_url .= '&openid=' . $openid;
        $user_info_url .= '&lang=zh_CN';
    
        $user_info = file_get_contents($user_info_url);
        $user_info = json_decode($user_info, true);
    
        // 在此处将用户信息写入数据库或将用户登录状态存储到 Session 中
        $_SESSION['user_info'] = $user_info;
    
        // 跳转到用户的主页
        header('Location: http://yourdomain.com/user.php');
        exit;
    } else {
        echo '获取 access_token 和 openid 失败';
    }
  
}
// 如果未获得 access_token，则跳转到微信授权页面获取
if (!isset($_GET['code'])) {
    $authorize_url = 'https://open.weixin.qq.com/connect/oauth2/authorize';
    $authorize_url .= '?appid=' . $app_id;
    $authorize_url .= '&redirect_uri=' . urlencode($redirect_uri);
    $authorize_url .= '&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect';
    header('Location: ' . $authorize_url);
    exit;
}
 
