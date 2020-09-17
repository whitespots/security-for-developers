from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    print('Webhook triggered')
    return 'This is a webhook already'


@app.route('/webhook')
def webhook():
    print('Webhook triggered')
    return 'And this is a webhook'
