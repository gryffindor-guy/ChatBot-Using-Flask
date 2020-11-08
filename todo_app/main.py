from flask import Flask, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
bot = ChatBot(
    'Hedwig',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

@app.route("/")
def introduce():
    # from data.about import bot
    return render_template("index.html", data = "Hi")

@app.route("/get")
def get_bot_response():
    if request.method == "POST":
        userText = request.args.get('chat-input')
        result = bot.get_response(userText)
        return render_template("base.html", data = result)
    else :
        return render_template("base.html")