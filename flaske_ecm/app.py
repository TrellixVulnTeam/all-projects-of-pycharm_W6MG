import flask
from flask import Flask
app= Flask(__name__)
@app.route('/')
def index():
    print('hello world')

index()

