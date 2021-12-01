from flask import Flask, render_template
from datetime import datetime as dt

app = Flask(__name__)


posts = [
    {
        "title": "Title Text 1",
        "datetime": dt.now(),
        "content": "This is an example of a blog post with small amount of text.",
    },
    {
        "title": "Title Text 2",
        "datetime": dt.now(),
        "content": "This is an example of a blog post with small amount of text.",
    },
]


@app.route("/")
def index():
    return render_template("index.html", posts=posts)
