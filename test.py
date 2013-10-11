from time import time
from pymongo import Connection
from pymongo.database import Database
import datetime

t = time()
db = Connection('mongodb://test:123456@ds049858.mongolab.com:49858/heroku_app18586342')['heroku_app18586342']
print time() - t
collection = db.test

posts = db.posts
t = time()
tmp = []
for i in range(1, 500):
    post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
    tmp.append(post)
    posts.insert(tmp)
print (time() - t)

t = time()
print db.collection_names()
print time() - t

t = time()
db.posts.find()
print time() - t


import socket
HOST = '173.255.112.112'    # The remote host
PORT = 80              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t = time()
s.connect((HOST, PORT))
print time() - t


