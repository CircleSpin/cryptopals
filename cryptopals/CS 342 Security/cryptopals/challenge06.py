# from bitarray import bitarray

# The Hamming distance is just the number of differing bits.
    #How do you determine the number of bits in a given string?


def hammingDistance(a,b):
    abits = ''.join(format(ord(x), '08b') for x in a) #convert the strings into their bit equivalents
    bbits = ''.join(format(ord(x), '08b') for x in b)
    # abits.strip(" ")
    # bbits.strip(" ")
    print("length of abits is ", len(abits))
    print("length of bbits is ", len(bbits))
    counts = 0
    for i in range(0,len(abits)): #figure out how many differing bits there are
        if (abits[i] != bbits[i]):
            print(abits[i], bbits[i])
            counts += 1
    print(abits)
    print(bbits)
    return counts

def findKeysize(ciphertext):
    allKsizes = {}
    for ksize in range(2,41): #Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
        # For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes,
# and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
        chunked = [ciphertext[i:i + ksize] for i in range(0, (2*ksize + 1), ksize)] # chunk the ciphertext into bytes of 1# 6
        distance = hammingDistance(chunked[0], chunked[1])
        normdistance = distance / ksize
        allKsizes['ksize'] = normdistance
        #find a way to store the normdistance and ksize (dictionary?)
        #quick way to find the smallest normdistance amongst the set

    # The KEYSIZE with the smallest normalized edit distance is probably the key.
        # You could proceed perhaps with the smallest 2-3 KEYSIZE values.
        # Or take 4 KEYSIZE blocks instead of 2 and average the distances.
    mintotal = 0
    for i in range (0, 5): #four times
        minkey = min(allKsizes, key=allKizes.get)
        mintotal += mintotal + key
        # remove the min entry from the dictionary after to find the next minimum?
        del d[minkey]
    avtotal = mintotal / 4
    # min(d, key=d.get)
    return avtotal




if __name__ == '__main__':
    print("hello")
    # print(hammingDistance('hello','good'))
    print(hammingDistance('this is a test', 'wokka wokka!!!'))