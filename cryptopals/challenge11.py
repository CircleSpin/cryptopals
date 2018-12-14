#Write a function that encrypts data under an unknown key ---
# that is, a function that generates a random key and encrypts under it.

# Ada hints: have the block be a repeated AAAAA long enough so that no matter the buffer there will be a repeated byte
import os
from random import randint
import challenge10

def randomAESkey():
    return os.urandom(16) #Write a function to generate a random AES key; that's just 16 random bytes.
    # buf = '\x00' + ''.join(chr(random.randint(0, 255)) for _ in range(4)) + '\x00'
    # print(type(buf))
    # return bytes(buf,ascii)

def appendbuffer(plaintext): #Under the hood, have the function append 5-10 bytes
#  (count chosen randomly) before the plaintext and 5-10 bytes after the plaintext.
    bufplaintext = ''
    startbuf = randint(5, 10)
    endbuf = randint(5, 10)
    for i in range (0, startbuf):
        bufplaintext = bufplaintext + "\x00"
    bufplaintext += plaintext
    for i in range(0, endbuf):
        bufplaintext = bufplaintext + "\x00"
    return bufplaintext

def encryption_oracle(input): #Write a function that encrypts data under an unknown key
#  --- that is, a function that generates a random key and encrypts under it.
    key = randomAESkey()
    input = appendbuffer(input)
    choice = rand(2) #decide CBC or EBC
    if (choice == 0):
        challenge10.EBCencrypt(input, key)
    if (choice == 1):





if __name__ == '__main__':
    print('hello')
    print(appendbuffer('hi'))

# can use challenge 8 to find the repeat


    #challenge 14: random number of bytes should be larger than the block size, write function that unpads function
        #challenge 14 cont. can keep random number constant
    #challenge 16: def(message, BLOCKSIZE = 16) allows for adjustability.
    #challenge 13: uid can be constant
