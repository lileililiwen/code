<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // 检查上传文件是否存在错误
    if ($_FILES['file']['error'] != UPLOAD_ERR_OK) {
        die('上传失败：' . $_FILES['file']['error']);
    }

    // 检查上传文件的类型和大小
    $allowed_types = ['image/jpeg', 'image/png', 'image/gif'];
    $max_size = 1024 * 1024; // 1MB
    $file_type = $_FILES['file']['type'];
    $file_size = $_FILES['file']['size'];
    if (!in_array($file_type, $allowed_types) || $file_size > $max_size) {
        die('上传失败：不支持的文件类型或文件过大');
    }

    // 将上传的文件移动到指定目录
    $target_dir = './uploads/';
    $target_file = $target_dir . basename($_FILES['file']['name']);
    move_uploaded_file($_FILES['file']['tmp_name'], $target_file);

    echo '上传成功：' . $target_file;
}
?>

<form method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <button type="submit">上传</button>
</form>