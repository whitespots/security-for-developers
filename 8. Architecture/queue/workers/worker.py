import time
from redis import Redis
from rq import Queue, Connection
from rq.worker import HerokuWorker as Worker

listen = ['high', 'default', 'low']

conn = Redis(host='redis', port=6379, db=0)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()