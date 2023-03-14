<?php // 连接数据库
$conn = mysqli_connect("localhost", "root", "", "mydb");

// 用户列表
$sql = "SELECT * FROM users";
$result = mysqli_query($conn, $sql);

while ($row = mysqli_fetch_assoc($result)) {
    echo $row['username'] . " - " . $row['email'] . "<br>";
}

// 添加用户
$username = "user1";
$password = "123456";
$email = "user1@example.com";

$sql = "INSERT INTO users (username, password, email) VALUES ('$username', '$password', '$email')";
mysqli_query($conn, $sql);

// 删除用户
$user_id = 1;

$sql = "DELETE FROM users WHERE id=$user_id";
mysqli_query($conn, $sql);
?>
