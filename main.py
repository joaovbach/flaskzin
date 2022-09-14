from requests import request
from flask import Flask, render_template, request, jsonify, url_for, redirect, sessions
import sqlite3
import os

app = Flask(__name__)
jaTentou = False
app.config['TESTE'] = ""
app.config['confirmaSenha']=""

def pegaUser(name,pas):
    with sqlite3.connect("banco.db")as con:
        cur = con.cursor()
        newname = "'"+pas+"'"
        txtSQL = "SELECT username FROM accounts WHERE pass =" + newname
        senha = cur.execute(txtSQL).fetchall()
        if len(senha)>0:
            return True
        else:
            return False

def registerUser(name,senha):
    print(name)
    with sqlite3.connect("banco.db") as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO accounts VALUES ('{name}','{senha}','false')")
        con.commit()

@app.route("/", methods = ['GET', 'POST'])
def index(*args):
    if request.method == 'GET':
        print("get")

    return render_template('index.html', txt = app.config['TESTE'])
    
    
    
@app.route("/home")
def home():

    date = request.args.get('username',None)
    pas = request.args.get('password',None)
    var = pegaUser(date,pas)
    if var:
        return render_template('home.html')
    else:
        app.config['TESTE'] = "senha incorreta"
        return redirect('/')
    

@app.route("/register")
def register():
    return render_template('regist.html')

@app.route("/finishregister")
def finishRegister():
    app.config['TESTE'] = ""
    nome = str(request.args.get('name', None))
    senha = str(request.args.get('senha',None))
    conf = str(request.args.get('confirm',None))

    if senha == conf:
         registerUser(nome,senha)
         app.config['confirmaSenha'] = ""
         return redirect('/')
    else:
        app.config['confirmaSenha'] = "senhas incorretas"
        return render_template('regist.html',resul = app.config['confirmaSenha'])


