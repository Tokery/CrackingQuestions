def replaceStr(inputStr, realSize):
    newIndex = len(inputStr) - 1
    input = list(inputStr)
    for i in range(realSize - 1, -1, -1):
        print input[i]
        if (input[i] == " "):
            input[newIndex] = "0"
            input[newIndex - 1] = "2"
            input[newIndex - 2] = "%"
            newIndex -= 3
        else:
            input[newIndex] = input[i]
            newIndex -= 1
    inputStr = ''.join(input)
    print (inputStr)

replaceStr("Mr John Smith    ", 13)