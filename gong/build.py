from jinja2 import Template, Environment, PackageLoader, select_autoescape
from datetime import datetime as dt
import frontmatter
import os
from shutil import copytree
import mistune

md2html = mistune.Markdown()

# packageloader wants the name of the directory in which to look for the template directory
env = Environment(loader=PackageLoader("build"), autoescape=select_autoescape)
home_template = env.get_template("index.html")
post_template = env.get_template("post.html")


def get_posts():
    # cycle through posts and create list of dicts called posts
    post_files = ["posts/" + f for f in os.listdir("posts")]

    load_posts = [frontmatter.load(p) for p in post_files]

    posts = []

    for f, p in zip(post_files, load_posts):
        d = dict(
            filename=f[6:],
            path=f[6:-3],
            date=f[6:16],  # take date from filename
            template=p.metadata["template"],
            title=p.metadata["title"],
            subtitle=p.metadata["subtitle"],
            content=md2html(p.content),
        )
        posts.append(d)

    return posts


def build_home(posts):
    html_template_string = home_template.render(posts=posts)
    os.system("rm -rf build/*")
    with open("build/index.html", "w") as f:
        f.write(html_template_string)
    os.system("cp -r static/ build/")


def build_posts(posts):
    os.system("mkdir build/posts")
    for post in posts:
        html_template_string = post_template.render(post=post)
        with open(f"build/posts/{post['path']}.html", "w") as f:
            f.write(html_template_string)


def build(posts):
    posts = get_posts()
    html_template_string = home_template.render(posts=posts)
    os.system("rm -rf build/*")
    with open("build/index.html", "w") as f:
        f.write(html_template_string)
    os.system("cp -r static/ build/")
    os.system("mkdir build/posts")
    for post in posts:
        html_template_string = post_template.render(post=post)
        with open(f"build/posts/{post['path']}.html", "w") as f:
            f.write(html_template_string)
