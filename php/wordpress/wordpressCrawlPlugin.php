<?php
/*
Plugin Name: My Crawler Plugin,
Description: A plugin for crawling and publishing web content
Version: 1.0
Author: Your Name
Author URI: http://www.example.com/
*/

// Include the simple html dom parser library
// 该插件中用到了一个第三方的PHP库simple_html_dom.php，
// 可以在这里下载到该库的最新版本：https://sourceforge.net/projects/simplehtmldom/files/latest/download
//将该库文件放置在插件目录
require_once('simple_html_dom.php');

// Register the plugin activation hook
register_activation_hook(__FILE__, 'my_crawler_plugin_activate');

// Register the plugin deactivation hook
register_deactivation_hook(__FILE__, 'my_crawler_plugin_deactivate');

// Define the plugin activation function
function my_crawler_plugin_activate() {
    // Add the custom cron job on plugin activation
    wp_schedule_event(time(), 'daily', 'simple_scraper');
}

// Define the plugin deactivation function
function my_crawler_plugin_deactivate() {
    // Remove the custom cron job on plugin deactivation
    wp_clear_scheduled_hook('simple_scraper');
}

// Register the custom cron job
add_action('my_crawler_plugin_cron', 'simple_scraper');

// Define the custom cron job function
function simple_scraper() {
    // Get the scraper URL from the plugin settings
    $url = get_option( 'scraper_url' );
    
    // Get the title and content selectors from the plugin settings
    $title_selector = get_option( 'title_selector' );
    $content_selector = get_option( 'content_selector' );
    
    // Load the HTML content of the scraper URL
    $html = file_get_contents( $url );
    
    // Create a new DOM document
    $dom = new DOMDocument();
    
    // Load the HTML content into the DOM document
    @$dom->loadHTML( $html );
    
    // Get the title of the webpage
    $title_element = $dom->querySelector( $title_selector );
    $title = $title_element->textContent;
    
    // Get the content of the webpage
    $content_element = $dom->querySelector( $content_selector );
    $content = $content_element->textContent;
    // Set the target URL to crawl
    $target_url = 'http://www.example.com/';

    // Set the target element selector to extract
    $target_selector = '.content';

    // Get the remote web page content using cURL
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $target_url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $html_content = curl_exec($ch);
    curl_close($ch);

    // Parse the HTML content using the simple html dom parser library
    $html = str_get_html($html_content);

    // Extract the target element from the HTML content
    $target_element = $html->find($target_selector, 0)->innertext;

    // Create a new post with the extracted content
    $post_title = 'My Crawler Plugin Post';
    $post_content = $target_element;
    $post_status = 'publish';
    $new_post_id = wp_insert_post(array(
        'post_title' => $post_title,
        'post_content' => $post_content,
        'post_status' => $post_status
    ));

    // If the post is created successfully, return the post ID
    if ($new_post_id) {
        return $new_post_id;
    } else {
        return false;
    }
}




// Register the plugin menu page
function simple_scraper_menu() {
    add_menu_page( 'Simple Scraper', 'Simple Scraper', 'manage_options', 'simple_scraper', 'simple_scraper_settings' );
}

add_action( 'admin_menu', 'simple_scraper_menu' );

// Define the plugin settings page
function simple_scraper_settings() {
    ?>
    <div class="wrap">
        <h1>Simple Scraper Settings</h1>
        <form method="post" action="options.php">
            <?php settings_fields( 'simple_scraper_settings' ); ?>
            <?php do_settings_sections( 'simple_scraper_settings' ); ?>
            <table class="form-table">
                <tr valign="top">
                    <th scope="row">Scraper URL</th>
                    <td><input type="text" name="scraper_url" value="<?php echo esc_attr( get_option( 'scraper_url' ) ); ?>" /></td>
                </tr>
                <tr valign="top">
                    <th scope="row">Title Selector</th>
                    <td><input type="text" name="title_selector" value="<?php echo esc_attr( get_option( 'title_selector' ) ); ?>" /></td>
                </tr>
                <tr valign="top">
                    <th scope="row">Content Selector</th>
                    <td><input type="text" name="content_selector" value="<?php echo esc_attr( get_option( 'content_selector' ) ); ?>" /></td>
                </tr>
            </table>
            <?php submit_button(); ?>
        </form>
    </div>
    <?php
}

// Register the plugin settings
function simple_scraper_register_settings() {
    register_setting( 'simple_scraper_settings', 'scraper_url' );
    register_setting( 'simple_scraper_settings', 'title_selector' );
    register_setting( 'simple_scraper_settings', 'content_selector' );
}

add_action( 'admin_init', 'simple_scraper_register_settings' );












?>