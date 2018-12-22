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
    strbytes = bytes(plaintext, 'ascii')  # convert the given message into bytes
    startchunk = b''
    endchunk = b''
    startbuf = randint(5, 10)
    endbuf = randint(5, 10)
    for i in range (0, startbuf):
        startchunk = startchunk + b'\x00'
    for i in range(0, endbuf):
        endchunk = endchunk + b'\x00'
    return startchunk + strbytes + endchunk

def CBCencrypt(ciphertext,key,IV):
    plaintext = b''
    n = 16
    chunked = [ciphertext[i:i + n] for i in range(0, len(ciphertext), n)] # chunk the ciphertext into bytes of 16
    #print(chunked)
    prevchunk = b''
    for chunk in chunked:
        echunk = challenge7.EBCencrypt(chunk, key) # pass that into EBC encrypt
        if chunk == chunked[0]: # first chunk will XOR with IV
            ciphertext += challenge02.XOR(echunk,IV)
        else:
            ciphertext += challenge02.XOR(echunk,prevchunk) # for each chunk following will XOR with previous 16 ciphertext chunk
        prevchunk = chunk
    return ciphertext

def encryption_oracle(input): #Write a function that encrypts data under an unknown key
#  --- that is, a function that generates a random key and encrypts under it.
    key = randomAESkey()
    input = appendbuffer(input)
    choice = random.randint(0,1) #decide CBC or EBC
    input = challenge10.autoPad16(input)
    input = input.decode("utf-8")
    if (choice == 0):
        print(challenge10.EBCencrypt(input, key))
    if (choice == 1): #CBC the other half (just use random IVs each time for CBC)
        iv = randomAESkey() #generate an IV using randomAES key
        print(CBCencrypt(input,key,iv))


if __name__ == '__main__':
    print(appendbuffer('hi'))
    print(appendbuffer('thereshouldbepaddingonme'))

    print(encryption_oracle("thisisaninput"))



# can use challenge 8 to find the repeat


    #challenge 14: random number of bytes should be larger than the block size, write function that unpads function
        #challenge 14 cont. can keep random number constant
    #challenge 16: def(message, BLOCKSIZE = 16) allows for adjustability.
    #challenge 13: uid can be constant
