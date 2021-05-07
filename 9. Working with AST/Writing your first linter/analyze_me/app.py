from flask import Flask
import functions
import requests
import ast

app = Flask(__name__)


@app.route('/')
def hello():
    if functions.check_200(functions.request_google()):
        return 'ok'
    return 'google_unreachable'


app.run()
