from requests import request
from flask import Flask, render_template, request, jsonify, url_for, redirect
import sqlite3

app = Flask(__name__)


def pegaUser(name):
    with sqlite3.connect("banco.db")as con:
        cur = con.cursor()
        senha = cur.execute("SELECT pass FROM accounts WHERE username='"+str(name)+"'").fetchall()
        if len(senha)>0:
            return True
        else:
            return False
        

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        print("get")
    return render_template("index.html")

@app.route("/home")
def home():
    date = request.args.get('username',None)
    var = pegaUser(date)
    if var:
        return render_template("home.html", username = "existe")
    else:
        return render_template("home.html", username = "nao existe")
