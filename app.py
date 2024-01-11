from flask import Flask, request, session, jsonify, url_for , redirect, render_template,Blueprint
import mysql.connector
from modules.mysqloperations import Model
from routes.api import api

app = Flask(__name__)


@app.route("/", methods= ['GET', 'POST'])
def home():
    db = Model()
    tasks = db.displayTask()
    return  render_template("todolist.html", tasks=tasks)

@app.route("/message", methods=['POST','GET'])
def message():
    return render_template("message.html")

@app.route("/returnhome", methods=['GET', 'POST'])
def return_home():
    return redirect(url_for("home"))




app.register_blueprint(api)


if __name__ == '__main__':
    app.run(debug = True, port = 5500)