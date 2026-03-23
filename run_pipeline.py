import news_fetcher
import video_maker
import shutil
import os

# Clear old videos safely
if os.path.exists("videos"):
    if os.path.isdir("videos"):
        shutil.rmtree("videos")  # remove old folder
    else:
        os.remove("videos")      # remove old file if exists by mistake

# Generate videos
headlines = news_fetcher.get_headlines()
video_maker.make_videos(headlines)
