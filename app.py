from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {
        "title": "Meu primeiro post",
        "body": "Esse post é o primeiro post do blog",
        "author": "Bianca Ribeiro",
        "created": datetime(2022, 8, 17)
    },
    {
        "title": "Meu segundo post",
        "body": "Esse post é o segundo post do blog",
        "author": "Bianca Ribeiro",
        "created": datetime(2022, 8, 17)
    },
    {
        "title": "Meu terceiro post",
        "body": "Esse post é o terceiro post do blog",
        "author": "Bianca Ribeiro",
        "created": datetime(2022, 8, 17)
    }
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)