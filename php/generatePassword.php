<?php
  function generate_password($length, $include_symbols = false) {
    // Define character set
    $characters = $include_symbols 
        ? 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~`|}{[]\\:;?><,./-=' 
        : 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    // Generate password
    $password = '';
    for ($i = 0; $i < $length; $i++) {
        $password .= $characters[rand(0, strlen($characters) - 1)];
    }
    return $password;
  }

  // Generate a 12-character password without symbols
  $password1 = generate_password(12);
  echo $password1;

  // Generate a 16-character password with symbols
  $password2 = generate_password(16, true);
  echo $password2;

?>