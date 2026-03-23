import news_fetcher
import video_maker

headlines = news_fetcher.get_headlines()
video_maker.make_videos(headlines)
