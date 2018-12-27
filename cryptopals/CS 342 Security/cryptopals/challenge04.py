#Finding the single byte XOR amongst a file of 60 char strings listed per line


def generatePlainTexts(file):
    sixtycharstrs = []
    sixtycharkeys = []
    sixtycharMaxScore = []
    for line in file.readlines():
        line = line.strip()
        #print(line.strip())
        plainTexts = challenge03.generatePlainText(line)
        print(plainTexts)
        scores = challenge03.scoreThis(plainTexts)
        print(scores)
        plaintext, key, maxScore = challenge03.findTheOne(scores, plainTexts)
        sixtycharstrs.append(plaintext)
        sixtycharkeys.append(key)
        sixtycharMaxScore.append(maxScore)
    #print(sixtycharMaxScore)
    print(findTheSixtyOne(sixtycharstrs, sixtycharkeys, sixtycharMaxScore))


def findTheSixtyOne(sixtycharstrs, sixtycharkeys, sixtycharMaxScore):
    #iterate through to find the maximum score, associated plaintext, and key
    maxScore = 0
    plaintext = ""
    key = 0
    for i in range(0, len(sixtycharMaxScore)-1):
        if sixtycharMaxScore[i] > maxScore:
            maxScore = sixtycharMaxScore[i]
            #print("hi")
            plaintext = sixtycharstrs[i]
            key = sixtycharkeys[i]
    #print(maxScore)
    return plaintext, key, maxScore

if __name__ == '__main__':
    str = '0e3647e8592d35514a081243582536ed3de6734059001e3f535ce6271032'
    print(len(str))
    file = open('challenge4.txt' ,'r')
    generatePlainTexts(file)