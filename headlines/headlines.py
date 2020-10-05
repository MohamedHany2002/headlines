from flask import Flask
app = Flask(__name__)
import feedparser
RSS_FEEDS = {
            'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn':'http://rss.cnn.com/rss/edition.rss',
            'fox':'http://feeds.foxnews.com/foxnews/latest',
            'iol':'http://www.iol.co.za/cmlink/1.640'
            }

@app.route('/')
@app.route('/<publication>')
def get_news(publication='bbc'):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_item = feed['entries'][0]
    return first_item.get("title")
if __name__=='__main':
    app.run(debug=True)