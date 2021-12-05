from flask import Flask, render_template
from datetime import datetime as dt
from main import get_posts

app = Flask(
    __name__, static_url_path="", static_folder="static", template_folder="templates"
)

posts = get_posts()


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
