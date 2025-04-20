import sqlite3

db = sqlite3.connect("blog.db")

db.execute("DROP TABLE IF EXISTS account")
db.execute('CREATE TABLE account (username TEXT, password TEXT)')
db.execute("INSERT INTO account (username, password) VALUES ('admin', 'password')")

db.commit()
db.close()

# https://capcrowgames.itch.io/dont-feed-it/download/eyJleHBpcmVzIjoxNzQ1MTIyNjk2LCJpZCI6MzQ3MTc5MH0%3d.Zsf2Ile3oSLmT7XuirM5tbVVgYg%3d