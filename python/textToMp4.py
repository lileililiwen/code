import requests
import os
from PIL import Image
from moviepy.editor import *
import re

# TTS API
def text_to_speech(text):
    url = "https://api.openai.com/v1/speeches/gpt3-tts"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"
    }
    data = {
        "text": text
    }
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        speech_url = response.json()["data"]["url"]
        return speech_url
    else:
        return None

# Image search API
def search_image(text):
    url = "https://api.openai.com/v1/images/gpt3"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"
    }
    data = {
        "text": text
    }
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        image_url = response.json()["data"]["url"]
        return image_url
    else:
        return None

# Download image from URL
def download_image(url, filename):
    response = requests.get(url)
    if response.ok:
        with open(filename, "wb") as f:
            f.write(response.content)
        return True
    else:
        return False

# Calculate segment duration based on text length
def get_segment_duration(text):
    # Average reading speed in words per minute
    reading_speed = 200
    # Average word length in characters
    average_word_length = 5
    # Calculate segment duration in seconds
    word_count = len(re.findall(r'\w+', text))
    duration = (word_count * average_word_length) / (reading_speed * 60)
    return duration

# Generate video from text
def generate_video(text):
    # Split text into segments
    text_segments = re.findall(r".{1,100}(?:\s|$)", text)
    # Remove leading/trailing whitespace from each segment
    text_segments = [segment.strip() for segment in text_segments]
    clips = []
    for i, segment in enumerate(text_segments):
        # Calculate segment duration
        duration = get_segment_duration(segment)
        # Convert text to speech
        speech_url = text_to_speech(segment)
        if not speech_url:
            return None
        # Search for image
        image_url = search_image(segment)
        if not image_url:
            return None
        # Download and process image
        image_filename = f"image_{i}.jpg"
        if not download_image(image_url, image_filename):
            return None
        image = Image.open(image_filename)
        # Generate video clip
        video_clip = ImageClip(image).set_duration(duration)
        clips.append(video_clip)
        # Generate audio clip
        audio_clip = AudioFileClip(speech_url).set_duration(duration)
        clips.append(audio_clip)
        # Clean up temporary files
        os.remove(image_filename)
    # Combine video and audio clips
    final_clip = concatenate_videoclips(clips)
    # Export final video
    final_clip.write_videofile("output.mp4")
    return True

# Example usage
text_segments ="在这个示范代码中，我们将输入的文字切分为两个时间段，分别为2秒和3秒。对于每个时间段，我们都会生成相应的图像和声音，并将它们合并成视频。在最后，我们将所有视频片段合并成一个完整的视频，并输出为文件。你可以根据需要修改输入的时间段。"
generate_video(text_segments)