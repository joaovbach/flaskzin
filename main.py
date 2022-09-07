from requests import request
from flask import Flask, render_template, request, jsonify, url_for, redirect, sessions
import sqlite3

app = Flask(__name__)
jaTentou = False
condicao = "dsa"

def pegaUser(name):
    with sqlite3.connect("banco.db")as con:
        cur = con.cursor()
        senha = cur.execute("SELECT pass FROM accounts WHERE username='"+str(name)+"'").fetchall()
        if len(senha)>0:
            return True
        else:
            return False

def registerUser(name):
    print(name)
    with sqlite3.connect("banco.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO accounts VALUES ("+"'"+str(name)+"','123','false')")
        con.commit()

def testee():
    date = request.args.get('username',None)
    var = pegaUser(date)
    if var:
        return "existe"
    else:
        return "nao existe"

@app.route("/", methods = ['GET', 'POST'])
def index(*args):
    
    if request.method == 'GET':
        print("get")
        

    
    return render_template('index.html', txt = testee())
    
    
    #return render_template("index.html")

@app.route("/home")
def home():
    #date = request.args.get('username',None)
    #var = pegaUser(date)
    #if var:
        #return render_template("home.html", username = "existe")
    #else:
        #return render_template("home.html", username = "nao existe")
    #testes = 12
    #return redirect(url_for('/',teste=testes))

    return redirect('/')

@app.route("/register")
def register():
    date = request.args.get('username',None)
    var = pegaUser(date)
    if var:
        return redirect('/', txt = "existe")
    else:
        return redirect('/', txt = "nao existe")
    #return redirect('/',)
    #return render_template("regist.html")

@app.route("/finishregister")
def finishRegister():
    nome = str(request.args.get('name', None))
    registerUser(nome)
    return redirect('/')

