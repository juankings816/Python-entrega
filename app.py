from flask import Flask, render_template, sessions, redirect, url_for
from functools import wraps
import pymongo

app = Flask(__name__)

app.secret_key="1234"

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client.todoPY