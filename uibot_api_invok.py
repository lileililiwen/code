import requests
import json

api_key = 'YOUR_API_KEY'
prompt_text = 'YOUR_PROMPT_TEXT'

data = {
    'model': 'text-davinci-002',
    'prompt': prompt_text,
    'temperature': 0.7,
    'max_tokens': 60
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, data=json.dumps(data))

print(response.json())