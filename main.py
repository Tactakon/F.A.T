import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
    books = [
        "How Difficult Can This Be?",
        "Its So Much Work to Be Your Friend",
        "The Motivation Breakthrough"
    ]
    pic = [
        "OIP.webp",
        "OIP 2.webp",
        "OIP 3.webp"
    ]
    return flask.render_template("index.html", books=books, pic=pic)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
