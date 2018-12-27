import challenge02

def repeatingXOR(string, key):
    strbytes = bytes(string, 'ascii') # convert the given string into bytes so individual bytes can be examined
    kbytes = bytes(key, 'ascii')
    xored = []
    for i in range (0, len(string)- 1): # loop through the string, XORing with I, C, E, repeatedly
        xored.append(XORBytewKey(kbytes[i % len(key)], strbytes[i])) # can do this through mod
    xoredb = bytes(xored) # change the int output into bytes
    hexm = challenge02.BytesToHex(xoredb) # convert those bytes into hex
    return hexm

def XORBytewKey(key,byte):
    return (key ^ byte)

if __name__ == '__main__':
    inString = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    print(repeatingXOR(inString, 'ICE'))

# expected output:
# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
# a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f