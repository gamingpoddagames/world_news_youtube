from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
import random, os

STOCK_DIR = "stock_videos"
VOICE_DIR = "voice_clips"
OUTPUT_DIR = "videos"

def make_videos(headlines):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for idx, headline in enumerate(headlines):
        stock_category = random.choice(os.listdir(STOCK_DIR))
        video_file = random.choice(os.listdir(os.path.join(STOCK_DIR, stock_category)))
        clip = VideoFileClip(os.path.join(STOCK_DIR, stock_category, video_file)).subclip(0,5)  # short clip

        txt_clip = TextClip(headline, fontsize=30, color='white', bg_color='black', size=clip.size)
        txt_clip = txt_clip.set_duration(clip.duration).set_position('bottom')

        voice_file = random.choice(os.listdir(VOICE_DIR))
        audio_clip = AudioFileClip(os.path.join(VOICE_DIR, voice_file))

        final_clip = CompositeVideoClip([clip, txt_clip]).set_audio(audio_clip)
        final_clip.write_videofile(os.path.join(OUTPUT_DIR, f"news_{idx}.mp4"), fps=24)
