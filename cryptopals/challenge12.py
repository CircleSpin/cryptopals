# -*- coding: utf-8 -*-
import challenge10
import challenge01

def byteAutoPad(message):
    if(len(message) % 16 != 0):
        mul16fits = len(message)//16 #integer division python magic
        desiredlen = 16 * (mul16fits+1)
        fours = b'\x04'
        padmessage = message
        if (len(message) < desiredlen):
            addLength = desiredlen - len(message)
            for i in range (0, addLength):
                padmessage = padmessage + fours
        return padmessage
    return message

# Copy your oracle function to a new function that encrypts buffers under ECB mode using a consistent but unknown key (for instance, assign a single random key, once, to a global variable).

#AES-128-ECB(your-string || unknown-string, random-key)
def encryption_oracle(input, key): #Write a function that encrypts data under an unknown key
#  --- that is, a function that generates a random key and encrypts under it.
    # print('the key is', key)
    print(input)
    input = appendbuffer(input)
    print(input)
    choice = randint(0,1) #decide CBC or EBC
    #print(type(input))
    input = byteAutoPad(input)
    # print("worky")
    input = input.decode("utf-8")
    # if (choice == 0):
    print('EBC')
    return challenge10.EBCencrypt(input, key)
    
def appendstring(known, unknown): #input string concat with "hidden" message in b'
    decoded = base64.b64decode(unknown)
    decodedstr = decoded.decode("utf-8") 
    appendedstr =  known + decodedstr
    return appendedstr
    
def findblocksize(unknownstring, key):
    #Feed identical bytes of your-string to the function 1 at a time --- start with 1 byte ("A"), then "AA", then "AAA" and so on. 
    #Discover the block size of the cipher. You know it, but do this step anyway.
    #continue to input A.... (know that it is supposed to be 16...)
    #find the length of the unknownstring
    print(len(unknownstring))
    #continue to add A until the you reach a multiple of 16?
    
    aye = 'A'
    discoveredblocksize = 0
    while(discoveredblocksize != 48): #haven't discovered the chain size
        aye += 'A'
        print(len(aye))
        plaintext = appendstring(aye, unknownstring)
        ciphertext = encryption_oracle(plaintext, key)
        print(ciphertext)
        discoveredblocksize += 1
        #if: #decide when you have discovered the blocksize
    #call appendstr and loop
    
    
# def createDictionary(): #keep track of all possible byte outputs.


if __name__ == '__main__':
    print('hi i am 12')
    key = randomAESkey() #Should I hardcode this?
    # b"\x84>V\x0e\xe8\x04\x98'\xa9\xaakO\xefp:1"
    known = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    unknown = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg"
    plaintext = appendstring(known,unknown)
    ciphertext = encryption_oracle(plaintext, key)
    print(ciphertext)
    findblocksize(unknown, key)

