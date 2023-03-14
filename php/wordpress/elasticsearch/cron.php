<!-- 将 sync-posts.php 文件上传到 WordPress 主题目录中，并激活该主题。就可以定时来跑同步了 -->
<?php

// 定义一个新的定时任务
function sync_posts_task() {
    // 调用之前编写的同步脚本，将文章数据同步到 Elasticsearch 中
    include_once 'syncToElasticSearch.php';
}

// 将定时任务添加到 WordPress 中
function add_sync_posts_task() {
    // 每小时执行一次任务
    $interval = 60 * 60;
    // 将定时任务添加到 WordPress 中
    wp_schedule_event( time(), $interval, 'sync_posts_task' );
}

// 在 WordPress 初始化时添加定时任务
add_action( 'init', 'add_sync_posts_task' );

?>