import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import base64

def rsakeys():
    length = 1024
    privatekey = RSA.generate(length, Random.new().read)
    publickey = privatekey.publickey()
    return privatekey, publickey

def encrypt(rsa_publickey, plain_text):
    cipher_text = rsa_publickey.encrypt(plain_text, 32)[0]
    b64cipher = base64.b64encode(cipher_text)
    return b64cipher

def decrypt(rsa_privatekey, b64cipher):
    decoded_ciphertext = base64.b64decode(b64cipher)
    plaintext = rsa_privatekey.decrypt(decoded_ciphertext)
    return plaintext

# Generating keys
privatekey, publickey = rsakeys()

# Text to encrypt
text = b"Hello from Whitespots!"

# Encrypted (cipher) text
cipher_text = encrypt(publickey, text)
print('\ncipher_text: %s' % cipher_text)

# Decryption
decrypted = decrypt(privatekey, cipher_text)
print('\ndecrypted: %s' % decrypted)
