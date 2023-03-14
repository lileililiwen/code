<?php
    // =========================
    // 文章和页面相关函数
    // =========================

    // 获取当前文章或页面的对象
    $post = get_post();

    // 获取当前文章或页面的标题
    $title = get_the_title($post);

    // 获取当前文章或页面的内容
    $content = get_the_content();

    // 获取当前文章或页面的发布日期
    $date = get_the_date('Y-m-d', $post);

    // 获取当前文章或页面的链接
    $link = get_permalink($post);

    // =========================
    // 分类和标签相关函数
    // =========================

    // 获取当前文章或页面的分类列表
    $categories = get_the_category($post);

    // 获取当前文章或页面的标签列表
    $tags = get_the_tags($post);

    // 获取指定分类的所有文章
    $posts = get_posts(array('category' => 5));

    // 获取指定标签的所有文章
    $posts = get_posts(array('tag' => 'wordpress'));

    // =========================
    // 用户和评论相关函数
    // =========================

    // 获取当前用户的 ID
    $user_id = get_current_user_id();

    // 获取当前用户的用户名
    $user_name = wp_get_current_user()->user_login;

    // 获取当前文章或页面的评论列表
    $comments = get_comments(array('post_id' => $post->ID));

    // 获取当前文章或页面的评论数
    $comment_count = get_comments_number($post);

    // 添加评论回复表单
    comment_form(array(
        'title_reply' => '发表评论',
        'comment_notes_before' => '',
        'comment_notes_after' => '',
    ));

    // =========================
    // 媒体和图像相关函数
    // =========================

    // 获取当前文章或页面的特色图像
    $image = get_the_post_thumbnail($post);

    // 调整图像大小并生成缩略图
    $image = wp_get_attachment_image_src( $attachment_id, 'thumbnail' );

    // 上传图像并将其附加到文章
    $attachment_id = media_handle_upload('image', $post->ID);
    set_post_thumbnail($post, $attachment_id);

    // 获取图像的属性和元数据
    $image_meta = wp_get_attachment_metadata($attachment_id);
    $image_alt = get_post_meta($attachment_id, '_wp_attachment_image_alt', true);

    // =========================
    // 其他常用函数
    // =========================

    // 检查用户是否拥有指定的权限
    if (current_user_can('edit_posts')) {
        // 允许用户编辑文章
    }

    // 检查当前页面是否为登录页面
    if (is_page('login')) {
        // 显示登录表单
    }

    // 获取当前 WordPress 版本号
    $version = get_bloginfo('version');



    $prev_post = get_adjacent_post(false, '', true); // 获取上一篇文章对象
    $next_post = get_adjacent_post(false, '', false); // 获取下一篇文章对象

    if ($prev_post) {
        // 如果存在上一篇文章，则输出上一篇文章的标题和链接
        $prev_link = get_permalink($prev_post->ID);
        $prev_title = get_the_title($prev_post->ID);
        echo '<a href="' . $prev_link . '">' . $prev_title . '</a>';
    }

    if ($next_post) {
        // 如果存在下一篇文章，则输出下一篇文章的标题和链接
        $next_link = get_permalink($next_post->ID);
        $next_title = get_the_title($next_post->ID);
        echo '<a href="' . $next_link . '">' . $next_title . '</a>';
    }



    //面包屑导航
    function get_breadcrumbs() {
        // 获取当前页面的 ID 和类型
        $object_id = get_queried_object_id();
        $object_type = get_queried_object_type();
    
        $breadcrumbs = array(); // 初始化面包屑导航数组
    
        // 添加首页链接
        $breadcrumbs[] = '<a href="' . home_url() . '">首页</a>';
    
        if ($object_type == 'term') {
            // 如果当前页面为分类或标签页面，则获取分类或标签的层级结构
            $term = get_queried_object();
            $ancestors = get_ancestors($term->term_id, $term->taxonomy);
    
            // 遍历分类或标签的层级结构，并添加到面包屑导航中
            foreach (array_reverse($ancestors) as $ancestor) {
                $ancestor_term = get_term($ancestor, $term->taxonomy);
                $breadcrumbs[] = '<a href="' . get_term_link($ancestor_term) . '">' . $ancestor_term->name . '</a>';
            }
    
            // 添加当前分类或标签链接
            $breadcrumbs[] = '<a href="' . get_term_link($term) . '">' . $term->name . '</a>';
        } elseif ($object_type == 'post') {
            // 如果当前页面为文章或页面，则获取其分类列表
            $categories = get_the_category();
    
            if ($categories) {
                // 如果文章或页面有分类，则获取其最后一个分类的层级结构
                $last_category = end($categories);
                $ancestors = get_ancestors($last_category->term_id, 'category');
    
                // 遍历最后一个分类的层级结构，并添加到面包屑导航中
                foreach (array_reverse($ancestors) as $ancestor) {
                    $ancestor_category = get_category($ancestor);
                    $breadcrumbs[] = '<a href="' . get_category_link($ancestor_category) . '">' . $ancestor_category->name . '</a>';
                }
    
                // 添加最后一个分类的链接
                $breadcrumbs[] = '<a href="' . get_category_link($last_category) . '">' . $last_category->name . '</a>';
            }
        }
    
        // 添加当前页面标题
        $breadcrumbs[] = get_the_title($object_id);
    
        // 将面包屑导航数组拼接为字符串并输出
        echo '<div class="breadcrumbs">' . implode(' > ', $breadcrumbs) . '</div>';
    }
?>