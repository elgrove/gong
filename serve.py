from flask import Flask, render_template, current_app
from datetime import datetime as dt
from build import get_posts

app = Flask(__name__, static_url_path="", static_folder="build")

posts = get_posts()


@app.route("/")
def index():
    return current_app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(debug=True)
