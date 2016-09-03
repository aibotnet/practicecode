from Crypto import Random
from Crypto.Cipher import AES
import sys

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)

# def get_random_key(SIZE):
#     # create random key for encryption random
#     import os
#     return os.urandom(SIZE)

def get_AES_key(SIZE, SECRET_KEY):
    import hashlib
    return hashlib.md5(SECRET_KEY).hexdigest()[:SIZE]

SECRET_KEY = get_AES_key(32, sys.argv[3])
if sys.argv[1]=='enc':
    encrypt_file(sys.argv[2], SECRET_KEY)
elif sys.argv[1]=='dec':
    decrypt_file(sys.argv[2], SECRET_KEY)
else:
    print 'Try : python secure.py command filepath key'

#python secure.py command filepath key
