import feedparser

url='https://anchor.fm/s/cf2ac40/podcast/rss'
NewsFeed=feedparser.parse(url)

entries=NewsFeed.entries

for entry in entries:
    for key in entry.keys():
        print('Key:{0}, Value:{1}'.format(key,entry[key]))