<?php
    // 引入 ElasticPress API
    use ElasticPress\Elasticsearch;

    // 获取 WordPress 文章列表
    $posts = get_posts( array(
        'post_type' => 'post', // 要索引的文章类型
        'posts_per_page' => -1, // 获取所有文章
    ) );

    // 获取 Elasticsearch 连接对象
    $elasticsearch = Elasticsearch::factory();

    // 循环遍历文章并进行索引
    foreach ( $posts as $post ) {
        // 创建索引数据
        $data = array(
            'post_title' => $post->post_title, // 文章标题
            'post_content' => $post->post_content, // 文章内容
            'post_date' => $post->post_date, // 发布日期
            'post_author' => $post->post_author, // 作者 ID
            // 其他自定义字段
        );

        // 索引文章数据到 Elasticsearch 中
        $elasticsearch->index( 'my_index', '_doc', $data, $post->ID );
    }
?>

<!-- elasticSerach提供的api,
wpes_index_post( $post_id ): 该 API 可以将指定的 WordPress 文章索引到 Elasticsearch 中。

wpes_delete_post( $post_id ): 该 API 可以从 Elasticsearch 中删除指定的 WordPress 文章索引。

wpes_search( $query ): 该 API 可以在 Elasticsearch 中搜索文档，返回匹配的结果。

wpes_get_mapping(): 该 API 可以获取 Elasticsearch 中已索引文档的映射（mapping），包括索引、字段类型、分词器等信息。

wpes_create_index(): 该 API 可以创建 Elasticsearch 索引，指定索引名称、分片数量、副本数量、映射等参数。

wpes_delete_index(): 该 API 可以删除 Elasticsearch 索引，删除后该索引中的文档及映射都将被删除。

wpes_bulk_index( $posts ): 该 API 可以批量索引 WordPress 文章到 Elasticsearch 中，以提高索引效率。

wpes_refresh_index(): 该 API 可以刷新 Elasticsearch 索引，使之立即生效，而不必等待默认的自动刷新。

这些 API 可以通过 Elasticsearch 插件提供的 PHP 函数调用，以实现对 Elasticsearch 的索引、搜索、删除、创建、删除等操作，使得 WordPress 开发者能够更方便地使用 Elasticsearch，以提升网站的搜索性能和用户体验。 -->