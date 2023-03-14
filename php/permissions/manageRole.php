<?php
// 连接数据库
$conn = mysqli_connect("localhost", "root", "", "mydb");

// 角色列表
$sql = "SELECT * FROM roles";
$result = mysqli_query($conn, $sql);

while ($row = mysqli_fetch_assoc($result)) {
    echo $row['role_name'] . " - " . $row['description'] . "<br>";
}

// 添加角色
$role_name = "admin";
$description = "系统管理员";
$permission_ids = "1,2,3";

$sql = "INSERT INTO roles (role_name, description, permission_ids) VALUES ('$role_name', '$description', '$permission_ids')";
mysqli_query($conn, $sql);

// 删除角色
$role_id = 1;

$sql = "DELETE FROM roles WHERE id=$role_id";
mysqli_query($conn, $sql);
?>