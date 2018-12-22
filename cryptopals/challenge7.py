# -*- coding: utf-8 -*-
# You need a function that does ECB
# It’s a wrapper—you’ll use a library that actually does the encryption
# But if that library doesn’t have an interface that looks like function(message,key) you’re going to want one
from Crypto.Cipher import AES
import base64

def EBCdecrypt(message, key):
    cipher = AES.new(key,AES.MODE_ECB)
    #cipher =  #Salsa20.new(key)
    plaintext = cipher.decrypt(message)
    return plaintext  # A byte string you must send to the receiver too

if __name__ == '__main__':
    message = open('challenge7.txt', 'r')
    dmessage = base64.b64decode(message.read())
    print(EBCdecrypt(dmessage,'YELLOW SUBMARINE'))
    print("hello")

