from flask import Flask, render_template, request
from flask_sockets import Sockets
from http.cookies import SimpleCookie


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/')
def echo_socket(ws):
    # Origin security check
    if ws.origin != 'http://localhost:5000':
        # return False
        pass

    # Cookie security check
    try:
        rawdata = ws.handler.headers.get('Cookie')
        cookie = SimpleCookie()
        cookie.load(rawdata)
        if cookie:
            pass
    except Exception as ex:
        pass

    while not ws.closed:
        message = ws.receive()
        # Vulnerable point
        if 'token=1' in ws.handler.path:
            ws.send('Hi Alice. This is a private message for you!')
        else:
            ws.send('I don\'t know you')


@app.route('/')
def hello():
    return render_template('client.html')


if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()