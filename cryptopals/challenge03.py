import challenge01
import string

def generatePlainText(message):
    messages = []
    bMessage = challenge01.HextoBytes(message)
    for i in range(0,255):
        messages.append(XORwKey(i, bMessage))
    return messages

def XORwKey(key,message):
    xored = []
    for a in message:
            xored.append(a ^ key)
    return bytes(xored)

def scoreThis(messages):
    scores = []
    for m in messages:
        score = 0
        for c in m:
            c = chr(c)
            if not(c in string.printable):
                score-=10
            #else:
                #print(c)
            if c.upper() == 'E' or c.upper() == 'T' or c.upper() == 'A' or c.upper() == 'O':
                #print(c)
                score+=2
            elif c.upper() == 'I' or c.upper() == 'N' or c.upper() == 'S' or c.upper() == 'R':
                #I N S R H D
                score += 1
        scores.append(score)
    return scores

def findTheOne(scores, plaintexts):
    #iterate through to find the maximum score, associated plaintext, and key
    maxScore = -10000000
    plaintext = ""
    key = 0;
    print(scores)
    for i in range (0, 255):
        if scores[i] > maxScore:
            maxScore = scores[i]
            #print("hi")
            plaintext = plaintexts[i]
            key = i
    #print(maxScore)
    return plaintext, key, maxScore

def decodeHex(hexString):
    plainTexts = generatePlainText(hexString)
    scores = scoreThis(plainTexts)
    return findTheOne(scores, plainTexts)

if __name__ == '__main__':
    hexString = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    plainTexts = generatePlainText(hexString)
    #print(plainTexts)
    scores = scoreThis(plainTexts)
    #print(max(scores))
    print(findTheOne(scores,plainTexts))
