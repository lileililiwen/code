<?php

session_start();

// 判断用户是否已经登录
if (!isset($_SESSION['user'])) {
    // 如果用户未登录，则重定向到CAS Server进行登录
    header("Location: http://localhost/cas.php");
    exit();
}

// 应用程序业务逻辑代码
echo "欢迎" . $_SESSION['user'] . "访问应用程序1！";

?>