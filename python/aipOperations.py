#百度ai相关sdk演示
from aip import AipSpeech

APP_ID = 'your_app_id'
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
with open('audio.wav', 'rb') as f:
    audio_data = f.read()

# 识别本地文件
result = client.asr(audio_data, 'wav', 16000, {
    'dev_pid': 1536,
})

print(result)