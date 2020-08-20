import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import base64

def rsakeys():
    length = 1024
    privatekey = RSA.generate(length, Random.new().read)
    publickey = privatekey.publickey()
    return privatekey, publickey

def sign(privatekey, data):
    return base64.b64encode(str((privatekey.sign(data, ''))[0]).encode())

def verify(publickey, data, sign):
    return publickey.verify(data,(int(base64.b64decode(sign)),))


# Generating keys
privatekey, publickey = rsakeys()

# Text to encrypt
text = b"Hello from Whitespots!"

# Digital signature
signature = sign(privatekey, text)
print('signature: %s' % signature)

# Check the signature
verified = verify(publickey, text, signature)
print('verified: %s' % verified)
