<?php
require_once('phpqrcode/qrlib.php');

// Default values for QR code colors
$bgColor = 0xFFFFFF; // White
$fgColor = 0x000000; // Black
$frameColor = 0x000000; // Black
$innerFrameColor = 0xFFFFFF; // White
?>
<form method="post">
    <p>
        <label>Text:</label>
        <input type="text" name="text">
    </p>
    <p>
        <label>Telephone:</label>
        <input type="tel" name="tel">
</p>
<p>
    <label>SMS:</label>
    <input type="tel" name="sms[tel]" placeholder="Telephone">
    <input type="text" name="sms[message]" placeholder="Message">
</p>
<p>
    <label>VCard:</label>
    <input type="text" name="vcard[name]" placeholder="Name">
    <input type="tel" name="vcard[phone]" placeholder="Phone">
    <input type="text" name="vcard[company]" placeholder="Company">
    <input type="url" name="vcard[url]" placeholder="Website">
    <input type="text" name="vcard[title]" placeholder="Title">
    <input type="email" name="vcard[email]" placeholder="Email">
    <input type="text" name="vcard[address]" placeholder="Address">
</p>
<p>
    <label>URL:</label>
    <input type="url" name="url">
</p>
<p>
    <label>WiFi:</label>
    <input type="text" name="wifi[ssid]" placeholder="SSID">
    <input type="password" name="wifi[password]" placeholder="Password">
    <select name="wifi[security]">
        <option value="WPA">WPA</option>
        <option value="WPA2">WPA2</option>
    </select>
</p>
<p>
    <label>Background Color:</label>
    <input type="color" name="bgColor" value="#FFFFFF">
</p>
<p>
    <label>Image Color:</label>
    <input type="color" name="fgColor" value="#000000">
</p>
<p>
    <label>Frame Color:</label>
    <input type="color" name="frameColor" value="#000000">
</p>
<p>
    <label>Inner Frame Color:</label>
    <input type="color" name="innerFrameColor" value="#FFFFFF">
</p>
<p>
    <input type="submit" value="Generate QR Code">
</p>
</form>
<?php
// Check if user has submitted the form
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // Check if user has set custom colors
        if (isset($_POST['bgColor'])) {
            $bgColor = hexdec($_POST['bgColor']);
        }
        if (isset($_POST['fgColor'])) {
            $fgColor = hexdec($_POST['fgColor']);
        }
        if (isset($_POST['frameColor'])) {
            $frameColor = hexdec($_POST['frameColor']);
        }
        if (isset($_POST['innerFrameColor'])) {
            $innerFrameColor = hexdec($_POST['innerFrameColor']);
        }
        // Check which type of QR code to generate
        if (isset($_POST['text'])) {
            $text = $_POST['text'];
            QRcode::png($text, 'qrcode.png', QR_ECLEVEL_Q, 10, 2, false, $bgColor, $fgColor, $frameColor, $innerFrameColor);
        } elseif (isset($_POST['tel'])) {
            $tel = $_POST['tel'];
            $text = 'tel:' . $tel;
            QRcode::png($text, 'qrcode.png', QR_ECLEVEL_Q, 10, 2, false, $bgColor, $fgColor, $frameColor, $innerFrameColor);
    } elseif (isset($_POST['sms'])) {
        $sms = $_POST['sms'];
        $tel = $sms['tel'];
        $message = $sms['message'];
        $text = 'smsto:' . $tel . ':' . $message;
        QRcode::png($text, 'qrcode.png', QR_ECLEVEL_Q, 10, 2, false, $bgColor, $fgColor, $frameColor, $innerFrameColor);
    } elseif (isset($_POST['vcard'])) {
        $vcard = $_POST['vcard'];
        $name = $vcard['name'];
        $phone = $vcard['phone'];
        $company = $vcard['company'];
        $url = $vcard['url'];
        $title = $vcard['title'];
        $email = $vcard['email'];
        $address = $vcard['address'];
        $text = "BEGIN:VCARD\nVERSION:2.1\nN:{$name}\nTEL;CELL:{$phone}\nORG:{$company}\nURL:{$url}\nTITLE:{$title}\nEMAIL:{$email}\nADR:{$address}\nEND:VCARD";
        QRcode::png($text, 'qrcode.png', QR_ECLEVEL_Q, 10, 2, false, $bgColor, $fgColor, $frameColor, $innerFrameColor);
    } elseif (isset($_POST['url'])) {
        $url = $_POST['url'];
        QRcode::png($url, 'qrcode.png', QR_ECLEVEL_Q, 10, 2, false, $bgColor, $fgColor, $frameColor, $innerFrameColor);
    } elseif (isset($_POST['wifi'])) {
        $wifi = $_POST['wifi'];
        $ssid = $wifi['ssid'];
        $password = $wifi['password'];
        $security = $wifi['security'];
        $text = "WIFI:S:{$ssid};T:{$security};P:{$password};;";
        QRcode::png($text, 'qrcode.png', QR_ECLEVEL_Q, 10, 2, false, $bgColor, $fgColor, $frameColor, $innerFrameColor);
    }
    // Output the generated QR code to the user
    echo '<img src="qrcode.png" alt="QR Code">';
}
?>