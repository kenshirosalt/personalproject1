from flask import Flask, render_template, request
import os

blog_posts = [
                {"pid": 0,
                "title": "efee",

                "content": "placeholdder"
                },
                {"pid": 1,
                "title": "efeee",
                "author": "ken",
                "content": "plaaceholdder"
                }
            ]

def hello_world():
    return render_template("index.html")


def cat_page():
    value = request.args.get('pid')
    if value == None:
        #localhost:5000/blog
        return render_template("show_posts.html", blog_posts=blog_posts)
    else:
        #localhost:5000/blog?pid=0
        #localhost:5000/blog?pid=1
        #...
        pid = int(value)
        for p in blog_posts:
            if p["pid"] == pid:
                return render_template("posts.html", blog_data=p)
    return render_template("show_posts.html", blog_posts=blog_posts)

def posts():
    return render_template("posts.html")

def createposts():
    return render_template("createposts.html")

def createacc():
    return render_template("createacc.html")

def login():
    return render_template("login.html")





app = Flask(__name__, template_folder=os.getcwd(), static_folder=os.getcwd())

app.add_url_rule("/home", "hello_world", hello_world)
app.add_url_rule("/blog", "blog", cat_page)
app.add_url_rule("/posts", "posts", posts)
app.add_url_rule("/login", "login", login)
app.add_url_rule("/createacc", "createacc", createacc)
app.add_url_rule("/createposts", "createpost", createposts)


app.run()