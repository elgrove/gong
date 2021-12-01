from jinja2 import Template, Environment, PackageLoader, select_autoescape
from datetime import datetime as dt


env = Environment(loader=PackageLoader("main"), autoescape=select_autoescape)

template = env.get_template("index.html")

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

html_template_string = template.render(posts=posts)

print(html_template_string)
