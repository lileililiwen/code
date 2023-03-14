<!DOCTYPE html>
<html>
<head>
    <title><?php wp_title(); ?></title>
    <?php wp_head(); ?>
</head>
<body>

<header>
    <h1><?php bloginfo('name'); ?></h1>
    <nav>
        <?php wp_nav_menu(); ?>
    </nav>
</header>