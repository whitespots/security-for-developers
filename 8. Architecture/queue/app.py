import time
from redis import Redis
from rq import Queue
from flask import Flask

app = Flask(__name__)

queue = Queue(
    connection=Redis(
        host='redis',
        port=6379
    ),
    default_timeout='3h'
)


@app.route('/')
def hello():
    for x in range(1, 10):
        queue.enqueue(time.sleep, 10, result_ttl=7200)
    return 'Look at http://localhost:9181/'
