import feedparser

RSS_FEEDS = [
    "http://feeds.bbci.co.uk/news/rss.xml",
    "http://feeds.reuters.com/reuters/worldNews",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

def get_headlines():
    headlines = []
    for feed in RSS_FEEDS:
        parsed = feedparser.parse(feed)
        for entry in parsed.entries[:3]:  # smaller for GitHub Actions limits
            headlines.append(entry.title)
    return headlines
