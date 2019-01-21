# from bitarray import bitarray
import challenge03

def hammingDistance(a,b): # The Hamming distance the number of differing bits.
    abits = ''.join(format(ord(x), '08b') for x in a) #convert the strings into their bit equivalents
    bbits = ''.join(format(ord(x), '08b') for x in b)
    # print("length of abits is ", len(abits))
    # print("length of bbits is ", len(bbits))
    counts = 0
    for i in range(0,len(abits)): #determine how many differing bits there are
        if (abits[i] != bbits[i]):
            # print(abits[i], bbits[i])
            counts += 1
    # print(abits)
    # print(bbits)
    return counts

def findKeysize(ciphertext): #Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
    # For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes,
    # and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
    allKsizes = {}
    for ksize in range(2,41):
        chunked = [ciphertext[j:j + ksize] for j in range(0, (2*ksize), ksize)] #get first two len ksizes (2, 41) chunks
        # chunked.append(chunk)
        # print('chunked:', chunked)
        distance = hammingDistance(chunked[0], chunked[1])
        normdistance = distance / ksize
        # print('the norm distance between the two chunks is', normdistance)
        allKsizes[ksize] = normdistance #store the ksize and the normdistance
    # print('Hi, i am allKsizes')
    # print(allKsizes)

    #2-3 minimum keysizes in minkeylist
    minkeyslist = []
    for i in range (0, 3): #three times
        minkey = min(allKsizes, key=allKsizes.get)
        # print('the minimum key is of type', type(minkey), 'and is', minkey)
        minkeyslist.append(minkey)
        # remove the min entry from the dictionary after to find the next minimum?
        del allKsizes[minkey]
        #store minimum keysizes and return them.
    # print('the minimum keys are', minkeyslist)
    return minkeyslist

# Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
def makeBlocks(keysizes, ciphertext):
    blocks = []
    #print("Ikhrdjyckjvkjh", keysizes)
    for key in keysizes:
        chunked = [ciphertext[j:j + key] for j in range(0, len(ciphertext), key)]
        #print(chunked)
        # TODO: format to return blocks
        blocks.append(chunked)
    print('poppoooo')
    print(blocks)
    return blocks #ADA QUESTION: Should this return a list of keyvalues, or just the optimal? Instructions confusing.


# Now transpose the blocks: make a block that is the first byte of every block,
# and a block that is the second byte of every block, and so on.
def transBlocks(blockList): #passed in 3 lists of blocks
    allblocks = []
    for blocks in blockList: #for each list
        #blocks = ['abc', ]
        # print('heee')
        # print(blocks)
        transblock = []
        for j in range (0, len(blocks[0])): #iterate through keysize
            transblock.append('') #Do I need to declare this outside?
            for i in range (0, len(blocks)): #iterating through the number of blocks
                if (j < len(blocks[i])):
                    transblock[j] += blocks[i][j]
        allblocks.append(transblock)
        # print(transblock)
    # print(len(blocks))
    return allblocks


        # #?? How do I iterate through i (0, lengthofablock) without declaring the block first (and iterating through)
        # for i in range(0, len(block)): #create transBlocks, number should of them is keysize (len is different)
        #     transblocks = []
        #     for block in range (0, len(blocks)): #for each block
        #         transblock += block[i] #take the ith of every entry...
        #     transblocks.append(transblock)
        #     print(transblocks)

def decodeBlocks(allblocks):
    finalPlaintext = ''
    finalScore = 0
    for blocks in allblocks:
        maxPlaintext = ''
        maxAvgScore = 0
        for block in blocks:
            print(len(block))
            if (len(block) % 2 == 1): #cannot decode something thats not divisble by 2
                print('REEE')
                maxAvgScore = -1000
                break
            plaintext, key, maxScore = challenge03.decodeHex(block)
            maxAvgScore += maxScore
            maxPlaintext += chr(key)
            print(maxPlaintext)
        maxAvgScore /= len(blocks)
        if (maxAvgScore > finalScore):
            finalPlaintext = maxPlaintext
            finalScore = maxAvgScore
    return finalPlaintext


if __name__ == '__main__':
    # print("hello")
    # print(hammingDistance('hello','good'))
    print(hammingDistance('this is a test', 'wokka wokka!!!'))
    # file = open('challenge8.txt', 'r') as
    with open('challenge8.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')
    print (len(data))
    keys = findKeysize(data)
    print(keys)
    blockList = makeBlocks(keys,data)
    # print(blockList)
    #print(transBlocks(blockList))
    for blocks in blockList:
        print(len(blocks))

    print(decodeBlocks(transBlocks(blockList)))

    # print(findKeysize('ABCDEFGHJKLMNOPQRSTUVWXY'))
    # print(findKeysize('THISISATOTALLYREASONABLETEXT!!'))


    # Previous issue: object is not subscriptable (incorrect type, not read as string)
    # solution A: go line by line through the code (for line in file)
    # for line in ciphertext:  # for line in file
    #     n = 16
    #     chunked = []
    #     for i in range(0, len(line), n):  # chunk into 16 bytes, storing in tuple?
    # solution B: read in the file as one line
    # Considering reading as one string rather than line by line:
    # with open('data.txt', 'r') as myfile:
    #     data = myfile.read().replace('\n', '')


