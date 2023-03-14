<?php
// 连接数据库
$conn = mysqli_connect("localhost", "root", "", "mydb");

// 权限列表
$sql = "SELECT * FROM permissions";
$result = mysqli_query($conn, $sql);

while ($row = mysqli_fetch_assoc($result)) {
    echo $row['permission_name'] . " - " . $row['description'] . "<br>";
}

// 添加权限
$permission_name = "view_users";
$description = "查看用户列表";
$role_ids = "1,2";

$sql = "INSERT INTO permissions (permission_name, description, role_ids) VALUES ('$permission_name', '$description', '$role_ids')";
mysqli_query($conn, $sql);

// 删除权限
$permission_id = 1;

$sql = "DELETE FROM permissions WHERE id=$permission_id";
mysqli_query($conn, $sql);
?>