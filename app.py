from flask import Flask, render_template, session, flash, redirect, url_for
from functools import wraps
import pymongo

app = Flask(__name__)

app.secret_key="1234"

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client.todoPY

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash('You need to login first')
            return redirect('/')
    return wrap

#routes
from user import routes


# Definir una ruta de inicio
@app.route('/')
def home():
    return render_template('login.html')


@app.route('/register/')
def register():
    return render_template('register.html')


@app.route('/perfil/')
@login_required
def perfil():
    return render_template('perfil.html')