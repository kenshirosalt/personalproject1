from flask import Flask, render_template
import os
def hello_world():
    return render_template("index.html")
def cat_page():
    return "<h1>this is a cat</h1>"

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
app.add_url_rule("/cat", "cat", cat_page)
app.add_url_rule("/posts", "posts", posts)
app.add_url_rule("/login", "login", login)
app.add_url_rule("/createacc", "createacc", createacc)
app.add_url_rule("/createposts", "createpost", createposts)


app.run()