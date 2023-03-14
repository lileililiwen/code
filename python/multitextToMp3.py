import boto3
from google.cloud import texttospeech
import azure.cognitiveservices.speech as speechsdk
import os

# 指定要转换为音频的文本文件
input_file = 'input.txt'

# 指定要保存音频文件的文件夹
output_dir = 'output'

# 指定默认音色
default_voice = 'Joanna'

# 创建AWS Polly客户端
polly = boto3.client('polly')

# 创建Google Text-to-Speech客户端
google_tts_client = texttospeech.TextToSpeechClient()

# 创建Microsoft Azure TTS客户端
azure_tts_key = '<your-azure-tts-key>'
azure_tts_region = '<your-azure-tts-region>'
azure_tts_client = speechsdk.SpeechSynthesizer(
    subscription_key=azure_tts_key,
    region=azure_tts_region
)

# 让客户选择要使用的TTS服务
tts_service = input('Which TTS service would you like to use? (1) AWS Polly, (2) Google Text-to-Speech, (3) Microsoft Azure Cognitive Services ')

# 为每一行生成音频文件
with open(input_file, 'r') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    # 创建TTS请求
    if tts_service == '1':  # AWS Polly
        response = polly.synthesize_speech(
            Text=line,
            VoiceId=default_voice,
            OutputFormat='mp3'
        )
        # 将音频文件写入本地文件夹中
        filename = f'{i}_aws.mp3'
        with open(os.path.join(output_dir, filename), '
