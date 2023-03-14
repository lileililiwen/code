<?php
$api_key = 'YOUR_API_KEY';
$prompt_text = 'YOUR_PROMPT_TEXT';

$data = array(
    'model' => 'text-davinci-002',
    'prompt' => $prompt_text,
    'temperature' => 0.7,
    'max_tokens' => 60
);

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.openai.com/v1/engines/davinci-codex/completions',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => json_encode($data),
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer '.$api_key
  ),
));

$response = curl_exec($curl);

curl_close($curl);

echo $response;
?>