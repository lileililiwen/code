<?php
session_start();

// 微信开放平台应用的 AppID 和 AppSecret
$wechatAppID = 'your_wechat_app_id';
$wechatAppSecret = 'your_wechat_app_secret';

// 回调地址，微信授权成功后将跳转到此地址
$redirectUrl = 'http://example.com/callback.php';

// 微信授权登录页面 URL
$authorizeUrl = 'https://open.weixin.qq.com/connect/oauth2/authorize';

// 获取 access_token 和 openid 的 API URL
$accessTokenUrl = 'https://api.weixin.qq.com/sns/oauth2/access_token';

// 获取用户信息的 API URL
$userInfoUrl = 'https://api.weixin.qq.com/sns/userinfo';

// 拼接微信授权登录页面 URL
$authorizeUrl .= '?appid=' . urlencode($wechatAppID);
$authorizeUrl .= '&redirect_uri=' . urlencode($redirectUrl);
$authorizeUrl .= '&response_type=code';
$authorizeUrl .= '&scope=snsapi_userinfo';
$authorizeUrl .= '&state=' . $_SERVER['REQUEST_URI'];

// 检查用户是否已经登录
if (!isset($_SESSION['user'])) {
    // 如果用户没有登录，重定向到微信授权登录页面
    header('Location: ' . $authorizeUrl);
    exit;
}

// 用户已经登录，输出用户信息
$user = $_SESSION['user'];
echo '欢迎您，' . $user['nickname'] . '！<br>';
echo '<img src="' . $user['headimgurl'] . '">';

?>