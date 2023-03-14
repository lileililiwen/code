<?php

#// 连接到 SQLite 数据库，如果不存在则创建
$db = new SQLite3('shorten.db');
$db->exec('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, url TEXT, short TEXT)');
#在 shorten.php 文件中，添加一个函数 generateShortURL，该函数会生成一个随机的短网址字符串。在此示例中，我们将使用 6 个字符的字符串作为短网址。
function generateShortURL() {
    $chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    $short = '';
    for ($i = 0; $i < 6; $i++) {
        $index = rand(0, strlen($chars) - 1);
        $short .= $chars[$index];
    }
    return $short;
}
#接下来，创建一个名为 shorten 的路由，处理用户的 URL 输入并生成相应的短网址。在此示例中，我们将使用 PHP 的 $_POST 方法接收用户输入。

if (isset($_POST['url'])) {
    $url = $_POST['url'];
    $stmt = $db->prepare('SELECT * FROM urls WHERE url=:url');
    $stmt->bindValue(':url', $url, SQLITE3_TEXT);
    $result = $stmt->execute();
    $row = $result->fetchArray();
    if ($row) {
        // 如果已经存在，则返回已有的短网址
        $short = $row['short'];
    } else {
        // 如果不存在，则生成新的短网址
        $short = generateShortURL();
        $stmt = $db->prepare('INSERT INTO urls (url, short) VALUES (:url, :short)');
        $stmt->bindValue(':url', $url, SQLITE3_TEXT);
        $stmt->bindValue(':short', $short, SQLITE3_TEXT);
        $stmt->execute();
    }
    // 返回短网址，并在跳转前展示谷歌广告
    echo '<html><head><title>广告页面</title></head><body><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><script>(adsbygoogle = window.adsbygoogle || []).push({});</script><meta http-equiv="refresh" content="3;URL=' . $row['url'] . '"></body></html>';
    exit();
}
#最后，创建一个名为 redirect 的路由，将短网址重定向到相应的原始 URL。

if (isset($_GET['short'])) {
    $short = $_GET['short'];
    $stmt = $db->prepare('SELECT * FROM urls WHERE short=:short');
    $stmt->bindValue(':short', $short, SQLITE3_TEXT);
    $result = $stmt->execute();
    $row = $result->fetchArray();
    if ($row) {
        // 如果存在，则重定向到原始 URL
        header('Location: ' . $row['url']);
        exit();
    }
}