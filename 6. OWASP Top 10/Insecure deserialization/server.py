import pickle
import base64
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/", methods=['GET', "POST"])
def home():
    response = make_response('No data was specified. Try to pass some values via ?pickled=')
    if request.args.get('pickled'):
        try:
            data = base64.urlsafe_b64decode(request.args.get('pickled'))
            deserialized = pickle.loads(data)
            response = make_response('Thanks for your data')
        except:
            response = make_response('En error occured. Use base64 for your data')
    response.headers['Content-Type'] = 'text/plain'
    return response


app.run(host='0.0.0.0', port=5000)
