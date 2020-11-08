from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def introduce():
    # from data.about import bot
    return render_template("index.html")

