from flask import Flask, render_template, request, redirect, session, flash
import os




users = [{"uid": 0, "name": "tim", "password": "passw"},
        {"uid": 0, "name": "jim", "password": "passw1"},
        {"uid": 0, "name": "kate", "password": "passw3"}]

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
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        blog_post = {"pid": len(blog_posts), "content": content, "title": title }
        blog_posts.append(blog_post)
        return redirect("/blog?pid=" + str(blog_post["pid"]))
    else:
        return render_template("createposts.html")

def createacc():
    return render_template("createacc.html")

def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        error = "incorrect"
        uid = -1
        for user in users:
            if user["name"] == name and user['password'] == password:
                error = None
                uid = user['uid']

        if error is None:
            session.clear()
            session["uid"] = str(uid)
            return redirect('/home')
        else:
            flash(error)
            return render_template("login.html")
    else:
        return render_template("login.html")


def logout():
    session.clear()
    return redirect("/home")


app = Flask(__name__, template_folder=os.getcwd(), static_folder=os.getcwd())
app.config.from_mapping(SECRET_KEY='my_dev_key')

app.add_url_rule("/home", "hello_world", hello_world)
app.add_url_rule("/blog", "blog", cat_page)
app.add_url_rule("/posts", "posts", posts)
app.add_url_rule("/login", "login", login, methods=["GET", "POST"])
app.add_url_rule("/createacc", "createacc", createacc)
app.add_url_rule("/createposts", "createpost", createposts, methods=["GET", "POST"])
app.add_url_rule("/logout", "logout", logout, methods=["POST"])

app.run()