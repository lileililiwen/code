<?php

session_start();

// 验证登录信息
function authenticate($username, $password)
{
    // 进行用户认证，这里可以使用数据库、LDAP等方式
    // 如果认证成功，则返回用户名，否则返回false
    if ($username == 'admin' && $password == '123456') {
        return $username;
    } else {
        return false;
    }
}

// CAS登录入口
if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    if ($user = authenticate($username, $password)) {
        $_SESSION['user'] = $user;
        header("Location: http://localhost/app1.php");
        exit();
    } else {
        echo "用户名或密码错误";
    }
}

// CAS单点登录验证
if (isset($_GET['ticket'])) {
    // 获取CAS Server传过来的ticket
    $ticket = $_GET['ticket'];
    // 验证ticket是否有效
    // 这里可以通过curl向CAS Server发送请求进行验证
    // 如果ticket有效，则将用户信息存入session
    if ($ticket == '123456') {
        $_SESSION['user'] = 'admin';
        header("Location: http://localhost/app1.php");
        exit();
    } else {
        echo "ticket无效";
    }
}

?>