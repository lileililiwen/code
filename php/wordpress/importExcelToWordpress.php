<?php
// WordPress 初始化
require_once('wp-load.php');

// 定义 Excel 文件路径和 WordPress 分类 ID
$excel_path = '/path/to/excel/file.xlsx';
$category_id = 1;

// 加载 PHPExcel 库
require_once('PHPExcel/Classes/PHPExcel.php');

// 创建 PHPExcel 对象并读取 Excel 文件
$objPHPExcel = PHPExcel_IOFactory::load($excel_path);

// 获取数据工作表
$data_sheet = $objPHPExcel->getActiveSheet();

// 获取数据行数和列数
$row_count = $data_sheet->getHighestDataRow();
$col_count = PHPExcel_Cell::columnIndexFromString($data_sheet->getHighestDataColumn());

// 循环读取 Excel 数据并插入 WordPress
for ($row = 2; $row <= $row_count; $row++) {
    // 获取 Excel 中的标题和内容
    $title = $data_sheet->getCellByColumnAndRow(0, $row)->getValue();
    $content = $data_sheet->getCellByColumnAndRow(1, $row)->getValue();

    // 创建文章对象
    $post = array(
        'post_title' => $title,
        'post_content' => $content,
        'post_status' => 'publish',
        'post_category' => array($category_id),
    );

    // 插入文章到 WordPress
    wp_insert_post($post);
}

// 完成导入
echo '导入完成';