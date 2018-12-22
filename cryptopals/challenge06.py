# from bitarray import bitarray

# The Hamming distance is just the number of differing bits.
    #How do you determine the number of bits in a given string?


def hammingDistance(a,b):
    abits = ''.join(format(ord(x), 'b') for x in a) #convert the strings into their bit equivalents
    bbits = ''.join(format(ord(x), 'b') for x in b)
    # abits.strip(" ")
    # bbits.strip(" ")
    print("length of abits is ", len(abits))
    print("length of bbits is ", len(bbits))
    counts = 0
    for i in range(0,len(abits) - 1): #figure out how many differing bits there are
        if (abits[i] != bbits[i]):
            print(abits[i], bbits[i])
            counts += 1
    print(abits)
    print(bbits)
    return counts

#Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

if __name__ == '__main__':
    print("hello")
    # print(hammingDistance('hello','good'))
    print(hammingDistance('this is a test', 'wokka wokka!!!'))