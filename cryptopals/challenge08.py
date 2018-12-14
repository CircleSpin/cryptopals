#Confusion about the conceptual approach to solving this problem...
#given that there is only one byte that has been encoded with xor,
#Doesn't that mean that there will be no repeating bytes?

#Answer to confusion: each line in the file represents one encrypted plaintext.
#There will be repeats amongst the line itself.


def findtheEBC(file):
    for line in file: # for line in file
        #print(len(line))
        n = 16
        chunked = []
        for i in range(0, len(line), n): # chunk into 16 bytes, storing in tuple?
            chunk = line[i:i + n]
            if chunk in chunked:# if there's a repeated element
                return line # return that line
            else:
                chunked.append(chunk)
            #print(chunked)

if __name__ == '__main__':
    file = open('challenge8.txt', 'r')
    print(findtheEBC(file))
    print("hello")