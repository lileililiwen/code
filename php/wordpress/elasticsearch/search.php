<?php
// 获取搜索关键词
$search_query = get_search_query();

// 使用 Elasticsearch 进行搜索

//插件提供了配置es的服务器地址，所以可以直接用代码获取，而不用在代码中写死地址
// // 初始化配置项
// EP_Config::init();

// // 获取配置项中的 Elasticsearch 连接地址
// $hosts = EP_Config::factory()->get('host');

// // 设置 Elasticsearch 连接地址为 localhost:9200
// EP_Config::factory()->set_host(array('http://localhost:9200'));



$results = Elasticsearch\ClientBuilder::create()
    ->setHosts(['http://localhost:9200'])
    ->build()
    ->search([
        'index' => 'wordpress',
        'body' => [
            'query' => [
                'multi_match' => [
                    'query' => $search_query,
//                     post_title^2 是 Elasticsearch 中的一种查询语法，表示对 post_title 字段进行全文搜索，并指定权重为 2，即在计算搜索得分时，该字段的权重是其他字段的两倍。
// 在 Elasticsearch 中，可以对搜索结果进行打分，打分规则通常包括搜索关键词在字段中出现的频率、位置等信息。指定权重可以影响打分结果，提高某些字段的权重，让搜索结果更加准确。
// 在 WordPress 中，post_title 是文章标题字段，post_content 是文章内容字段。因此，使用 post_title^2 表示在搜索时，文章标题的权重是文章内容的两倍。
                    'fields' => ['post_title^2', 'post_content']
                ]
            ]
        ]
    ]);

// 遍历搜索结果并输出
foreach ($results['hits']['hits'] as $result) {
    $post = get_post($result['_source']['id']);
    ?>
    <h2><a href="<?php echo get_permalink($post); ?>"><?php echo $post->post_title; ?></a></h2>
    <p><?php echo $post->post_excerpt; ?></p>
    <?php
}
?>

<!-- $results 的结构如下：
// array(
//     'took' => 2,
//     'timed_out' => false,
//     '_shards' => array(
//         'total' => 5,
//         'successful' => 5,
//         'skipped' => 0,
//         'failed' => 0
//     ),
//     'hits' => array(
//         'total' => array(
//             'value' => 1,
//             'relation' => 'eq'
//         ),
//         'max_score' => 0.2876821,
//         'hits' => array(
//             array(
//                 '_index' => 'my_index',
//                 '_type' => '_doc',
//                 '_id' => '1',
//                 '_score' => 0.2876821,
//                 '_source' => array(
//                     'title' => 'My Document Title',
//                     'content' => 'This is the content of my document.'
//                 )
//             )
//         )
//     )
// );
// 下面是对 $results 结构的解释：

// took: 搜索请求耗时（以毫秒为单位）
// timed_out: 是否超时
// _shards: 请求使用的分片信息
// total: 总共的分片数量
// successful: 成功的分片数量
// skipped: 跳过的分片数量
// failed: 失败的分片数量
// hits: 搜索结果信息
// total: 搜索结果的总数量
// value: 搜索结果的数量
// relation: 匹配规则（eq：完全匹配，gte：大于等于，gt：大于）
// max_score: 最大得分
// hits: 包含匹配的文档信息
// _index: 文档所在的索引名称
// _type: 文档类型
// _id: 文档 ID
// _score: 文档得分
// _source: 文档的原始数据
// 需要注意的是，$results 的结构可能会根据 Elasticsearch 版本和查询语句不同而有所变化。 -->