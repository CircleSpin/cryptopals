#Point of this exercise is to realize that you need to convert hex -> bytes -> base64
#Having these as separate methods is good so you can import and use them for future exercises


import codecs

def HextoBytes(input):
    output = codecs.decode(input, 'hex')
    return output

def Bytesto64(input):
    b64 = codecs.encode(input,'base64')
    return b64

def Hexto64(hex):
    bytes = HextoBytes(hex)
    b64 = Bytesto64(bytes)#.decode()
    return b64

#Desired: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

if __name__ == '__main__':
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(Hexto64(hex))
