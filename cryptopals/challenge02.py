#Need to convert from "base" format into bytes so that it is in the computer readable version
#meaning, b'1c0111001f010100061a024b53535009181c' to /x1c/x01/x11... etc
#Iterate over individual bytes to XOR (can't do it in a chunk!) so use zip python package which pairs
#the bytes (first in a, first in b, second in a, second in b) in a tuple.

import challenge01
import codecs


def XOR(first,second):
    #adaversion:
    #xored = bytes([a^b] for (a,b) in zip(x,y)])
    xored = []
    for a,b in zip(first,second):
        xored.append(a^b)
    return bytes(xored)#.decode("utf-8") #this removes the b' in front of the string

def BytesToHex(input):
    output = codecs.encode(input, 'hex')
    return output

if __name__ == '__main__':
    input1 = b'1c0111001f010100061a024b53535009181c'
    input2 = b'686974207468652062756c6c277320657965'
    input1converted = challenge01.HextoBytes(input1)
    input2converted = challenge01.HextoBytes(input2)
    print(input1converted)
    print(input2converted)
    result = XOR(input1converted , input2converted)
    print(BytesToHex(result))


    #should return 746865206b696420646f6e277420706c6179