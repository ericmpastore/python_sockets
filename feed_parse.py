import feedparser
import time

feed = feedparser.parse("http://news.un.org/feed/subscribe/en/news/topic/economic-development/feed/rss.xml")

print(f"Number of RSS posts: {len(feed.entries)} \n")

while True:
    print("############ Begin Feed #################\n\n")
    for post in feed.entries:
        print(f"{post.title}\n{post.link}\n\n")

    print("########### End Feed #############\n\n")

    time.sleep(30)