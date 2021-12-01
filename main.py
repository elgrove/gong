from jinja2 import Template, Environment, PackageLoader, select_autoescape
from datetime import datetime as dt
import frontmatter
import os
from shutil import copytree
import mistune

md2html = mistune.Markdown()

env = Environment(loader=PackageLoader("main"), autoescape=select_autoescape)
template = env.get_template("index.html")

post_files = ["posts/" + f for f in os.listdir("posts")]

posts = [frontmatter.load(p) for p in post_files]

# cycle through posts and create list of dicts called posts


posts_web = []


for f, p in zip(post_files, posts):
    d = dict(
        date=f[6:16],  # take date from filename
        template=p.metadata["template"],
        title=p.metadata["title"],
        subtitle=p.metadata["subtitle"],
        content=md2html(p.content),
    )
    posts_web.append(d)


html_template_string = template.render(posts=posts_web)


with open("build/index.html", "w") as f:
    f.write(html_template_string)

os.system("cp -r static/ build/")
