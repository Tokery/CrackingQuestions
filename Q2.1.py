def removeDup(linktList):
    seen = []
    index = 0
    for a in range(0, len(linktList)):
        element = linktList[index]
        if element in seen:
            del linktList[index]
        else:
            seen.append(element)
            index += 1
    return linktList

def removeDupNoBuffer(linktList):
    linktList.sort()
    index = 0
    for a in range(0, len(linktList)-1):
        if (linktList[index] == linktList[index+1]):
            del [linktList[index+1]]
        else:
            index += 1
    return linktList
myList = [4, 2, 3, 2, 4, 5, 11, 11]
secondList = [2,2,2,2,2,2,2]

print (removeDup(secondList))
print (removeDupNoBuffer(secondList))
