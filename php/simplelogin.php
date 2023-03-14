<?php
// 连接 SQLite 数据库
$db = new SQLite3('database.sqlite');

// 处理登录请求
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  // 获取表单数据
  $username = $_POST['username'];
  $password = $_POST['password'];

  // 查询数据库中是否有匹配的用户
  $stmt = $db->prepare('SELECT * FROM users WHERE username=:username AND password=:password');
  $stmt->bindValue(':username', $username, SQLITE3_TEXT);
  $stmt->bindValue(':password', $password, SQLITE3_TEXT);
  $result = $stmt->execute();

  // 如果找到匹配的用户，设置会话变量并重定向到欢迎页面
  if ($result->fetchArray()) {
    session_start();
    $_SESSION['username'] = $username;
    header('Location: welcome.php');
    exit();
  }
}
?>

<!-- 登录表单 -->
<form method="POST">
  <label for="username">用户名:</label>
  <input type="text" id="username" name="username" required>

  <label for="password">密码:</label>
  <input type="password" id="password" name="password" required>

  <button type="submit">登录</button>
</form>
