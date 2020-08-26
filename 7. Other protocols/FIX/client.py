import socket
from simplefix import *

host = '127.0.0.1'
port = 11310
target = 'TARGET'
sender = 'SENDER'

for x in range(0, 4):
    msg = FixMessage()
    msg.begin_string = b'FIX.4.2'
    msg.message_type = b'1'
    msg.append_pair(34, '2')
    msg.append_pair(49, sender)
    msg.append_pair(56, target)
    msg.append_pair(112, str(x))
    msg.append_time(52)
    buffer = msg.encode(False)
    s = socket.socket()
    s.connect((host, port))
    s.send(buffer)
