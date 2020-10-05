from flask import Flask
app = Flask(__name__)


@app.route('/')
def get_news():
    return 'no news to display'
if __name__=='__main':
    app.run(debug=True)