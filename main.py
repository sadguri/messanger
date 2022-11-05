# Flask - библиотека для создания веб-сервера
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
all_messages = []


@app.route("/")
def hello_world():
    return "<p>Hello, welcome to <b>Skill</b> <i>Messenger</i></p>"


# API для получения сообщений
# /get_messages => {"messages": [...]}
@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


def add_message(sender, text):
    # time: подставить автоматически
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M"),
    }
    # append - добавить элемент в список
    all_messages.append(new_message)


add_message("Mike", "test")
add_message("John", "hello")


# API для отправки сообщений /send_message?sender=Mike&text=Hello
@app.route("/send_message")
def send_message():
    sender = request.args["sender"]  # ToDO: error here, sender vs name
    text = request.args["text"]
    add_message(sender, text)

    return {"result": True}


@app.route("/chat")
def chat_page():
    return render_template("form.html")


app.run(debug=True)