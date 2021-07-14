from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/iframe')
def iframe():
    return render_template('frame_with_secret.html')
