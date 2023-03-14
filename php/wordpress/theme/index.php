<?php get_header(); ?>

<div id="content">

    <?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>

        <div class="post">

            <h2><?php the_title(); ?></h2>

            <div class="entry">

                <?php the_content(); ?>

            </div>

        </div>

    <?php endwhile; endif; ?>

</div>

<?php get_footer(); ?>



<!-- 
WordPress 是一款非常灵活且功能强大的内容管理系统。下面是一些常用的 WordPress 函数和页面的介绍：

常用函数：

bloginfo()：输出 WordPress 博客的信息，例如站点名称、URL、描述等。
wp_head()：在 WordPress 页面的头部输出代码，通常用于添加 CSS 或 JavaScript 文件。
wp_footer()：在 WordPress 页面的底部输出代码，通常用于添加 JavaScript 或其他底部内容。
the_post()：将当前文章对象设置为下一篇文章并返回文章对象。
the_title()：输出当前文章的标题。
the_content()：输出当前文章的内容。
get_template_part()：加载 WordPress 主题中的指定部分文件。
wp_nav_menu()：输出 WordPress 主题中的导航菜单。
get_post_meta($post->ID, 'meta_key', true) ) 获取自定字段
 -->