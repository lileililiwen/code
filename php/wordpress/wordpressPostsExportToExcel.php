<?php
require_once('wp-load.php'); // 导入WordPress的核心文件

// 查询所有文章
$args = array(
    'post_type' => 'post',
    'post_status' => 'publish',
    'posts_per_page' => -1, // 查询所有文章
);
$query = new WP_Query($args);

// 创建Excel文件
require_once 'vendor/autoload.php'; // 导入PHPExcel库
$objPHPExcel = new \PHPExcel();
$objPHPExcel->getProperties()->setCreator('WordPress'); // 设置作者
$objPHPExcel->getProperties()->setTitle('WordPress Posts'); // 设置标题

// 创建表头
$objPHPExcel->setActiveSheetIndex(0)
    ->setCellValue('A1', 'ID')
    ->setCellValue('B1', '标题')
    ->setCellValue('C1', '发布时间')
    ->setCellValue('D1', '内容');

// 循环输出文章
$i = 2; // 从第二行开始输出文章内容
while ($query->have_posts()) {
    $query->the_post();
    $post_id = get_the_ID();
    $post_title = get_the_title();
    $post_date = get_the_date();
    $post_content = get_the_content();

    $objPHPExcel->setActiveSheetIndex(0)
        ->setCellValue('A' . $i, $post_id)
        ->setCellValue('B' . $i, $post_title)
        ->setCellValue('C' . $i, $post_date)
        ->setCellValue('D' . $i, $post_content);

    $i++;
}

// 设置列宽
$objPHPExcel->getActiveSheet()->getColumnDimension('A')->setWidth(10);
$objPHPExcel->getActiveSheet()->getColumnDimension('B')->setWidth(50);
$objPHPExcel->getActiveSheet()->getColumnDimension('C')->setWidth(20);
$objPHPExcel->getActiveSheet()->getColumnDimension('D')->setWidth(100);

// 设置表格样式
$style = array(
    'font' => array(
        'bold' => true,
        'size' => 12,
    ),
    'alignment' => array(
        'horizontal' => \PHPExcel_Style_Alignment::HORIZONTAL_CENTER,
    ),
    'borders' => array(
        'allborders' => array(
            'style' => \PHPExcel_Style_Border::BORDER_THIN,
        ),
    ),
    'fill' => array(
        'type' => \PHPExcel_Style_Fill::FILL_GRADIENT_LINEAR,
        'rotation' => 90,
        'startcolor' => array(
            'argb' => 'FFA0A0A0',
        ),
        'endcolor' => array(
            'argb' => 'FFFFFFFF',
        ),
    ),
);
$objPHPExcel->getActiveSheet()->getStyle('A1:D1')->applyFromArray($style);

// 输出Excel文件
$objWriter = \PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
$objWriter->save('wordpress_posts.xlsx');