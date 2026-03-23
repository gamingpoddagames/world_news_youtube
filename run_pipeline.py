import news_fetcher
import video_maker
import shutil
import os

# Clear old videos to avoid GitHub folder conflict
if os.path.exists("videos"):
    shutil.rmtree("videos")

headlines = news_fetcher.get_headlines()
video_maker.make_videos(headlines)
