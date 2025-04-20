import sqlite3

db = sqlite3.connect("blog.db")
db.execute("DROP TABLE IF EXISTS posts")
db.execute("CREATE TABLE posts(author_id, title TEXT, content TEXT, likes INTEGER)")

db.execute("INSERT INTO posts (author_id, title, content, likes) VALUES (1, 'Cats', 'I like cats', 100)")
db.execute("INSERT INTO posts (author_id, title, content, likes) VALUES (2, 'Dogs', 'I like dogs', 2000), (3, 'Zebras', 'I like zebras', 30000)")

result = db.execute("SELECT rowid, title, author_id, content, likes FROM posts").fetchall()
print(result)

#<, >, <=, >=, = ==, <>, NOT likes = 1000
result = db.execute("SELECT title, likes FROM posts WHERE likes < 1000").fetchall()
print(result)

result = db.execute("SELECT min(likes), max(likes), count(likes) FROM posts WHERE likes > 1000").fetchall()
print(result)

db.execute("DROP TABLE IF EXISTS account")
db.execute("CREATE TABLE account(name TEXT, password TEXT, age INTEGER, post_count INTEGAR)")
db.execute("INSERT INTO account (name, password, age, post_count) VALUES ('Tim', 'passw', 500, 1), ('Jim', 'passw1', 6, 100), ('Kate', 'passw', 5, 52)")
result = db.execute("SELECT rowid, name, password, age, post_count FROM account").fetchall()
print(result)

result = db.execute("SELECT min(age), avg(post_count), sum(post_count) FROM account").fetchall()
print(result)

#db.execute("UPDATE account SET name='Katey', age=5 WHERE name = 'Kate'")
#result = db.execute('SELECT rowid, name, password, age, post_count FROM account').fetchall()

result = db.execute("SELECT name, title, content FROM account JOIN posts ON author_id = account.rowid").fetchall()
print(result)

db.execute("DROP TABLE IF EXISTS comments")
db.execute("CREATE TABLE comments (author_id INTEGER, content TEXT, likes INTEGER)")
db.execute("INSERT INTO comments (author_id, content, likes) VALUES (1, 'Comment A', 100), (2, 'Comment B', 200), (2, 'Comment C', 300)")

result = db.execute("SELECT name, content FROM comments JOIN account ON author_id = account.rowid").fetchall()
print(result)
