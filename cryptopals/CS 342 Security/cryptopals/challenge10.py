# 1) Implement CBC mode by hand by taking the ECB function you wrote earlier,
#  making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test),
# and using your XOR function from the previous exercise to combine them.

# 2) The file here is intelligible (somewhat) when CBC decrypted against
# "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)

import challenge01
import challenge02
import challenge09
import challenge7
import base64
from Crypto.Cipher import AES

def EBCencrypt(message, key):
    cipher = AES.new(key,AES.MODE_ECB)
    #cipher =  #Salsa20.new(key)
    ciphertext = cipher.encrypt(message)
    return ciphertext  # A byte string you must send to the receiver too

def autoPad16(message): #add padding as appropriate
    if(len(message) % 16 != 0):
        mul16fits = len(message)//16 #integer division python magic
        desiredlen = 16 * (mul16fits+1)
        # if (type(b'message') != string):
        #     message = string(message)
        return challenge09.addPadding(message, desiredlen)
        #challenge09.addPadding(test, 64)
    return message

def CBCdecrypt(ciphertext,key,IV):
    plaintext = b''
    n = 16
    chunked = [ciphertext[i:i + n] for i in range(0, len(ciphertext), n)] # chunk the ciphertext into bytes of 16
    #print(chunked)
    prevchunk = b''
    for chunk in chunked:
        dchunk = challenge7.EBCdecrypt(chunk, 'YELLOW SUBMARINE') # pass that into EBC decrypt
        if chunk == chunked[0]: # first chunk will XOR with IV
            plaintext += challenge02.XOR(dchunk,IV)
        else:
            plaintext += challenge02.XOR(dchunk,prevchunk) # for each chunk following will XOR with previous 16 ciphertext chunk
        prevchunk = chunk
    return plaintext



    # append the plaintexts together



if __name__ == '__main__':
    test = "This is the message I'm going to encrypt and then decrypt"
    test = autoPad16(test)
    etest = EBCencrypt(test, 'YELLOW SUBMARINE')
    print(challenge7.EBCdecrypt(etest, 'YELLOW SUBMARINE'))

    #message = open('challenge7.txt', 'r')
    #dmessage = base64.b64decode(message.read())
    file = open('challenge10.txt', 'r')
    cfile = base64.b64decode(file.read())#.read())
   #print(challenge01.HextoBytes(file))#convert file in base 64 to bytes
    print(CBCdecrypt(cfile, 'YELLOW SUBMARINE', b'\x00\x00\x00 &c'))



