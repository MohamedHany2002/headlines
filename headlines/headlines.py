from flask import Flask,render_template,request
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
    items = feed['entries']
    return render_template('home.html',items=items)

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query.lower() in RSS_FEEDS:
        query='bbc'
    feed = feedparser.parse(RSS_FEEDS[query.lower()])
    items = feed['entries']
    return render_template('home.html',items=items,searched=query)



if __name__=='__main':
    app.run(debug=True)