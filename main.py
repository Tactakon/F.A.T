import flask
app = flask.Flask(__name__)
@app.route('/')

def index():
    books= 'Math', 'Psychology', 'Science', 'Philosophy', 'Geology'
    pic= 'https://th.bing.com/th/id/OIP.Gg9-uVWsH4nQtj0QLGpl1QHaLc?pid=ImgDet&rs=1', 'https://www.coverbrowser.com/image/books-about-psychology/61-2.jpg' , 'https://www.coverbrowser.com/image/science-books/540-7.jpg', 'https://imgv2-1-f.scribdassets.com/img/word_document/431779185/original/126edab196/1595984953?v=1', 'https://images.psbooks.co.uk/images/509925_media-0.jpg'
    return flask.render_template(
    "index.html",
    len=len(books),
    books=books,
    plen=len(pic),
    pic=pic
)
app.run(
debug=True
)
