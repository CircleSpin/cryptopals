def addPadding(message, desirelength):
    # if (type(message) != type(b'\x04')):
    strbytes = bytes(message, 'ascii')#convert the given message into bytes
    # print(len(strbytes))
    # print(len(message))
    padmessage = strbytes
    fours = b'\x04'
    # print(fours)
    # print(desirelength)
    if (len(strbytes) < desirelength):
        addLength = desirelength - len(strbytes)
        for i in range (0, addLength):
            padmessage = padmessage + fours
            # print(padmessage)
        return padmessage
    else:
        print("The desirelength is less than the message length")
        return padmessage
    #determine the length of the unpadded message in bytes
    #determine the amount of padding that should be added in bytes
    #add the appropriate amount of padding of bytes


if __name__ == '__main__':
    print(addPadding("YELLOW SUBMARINE", 20))