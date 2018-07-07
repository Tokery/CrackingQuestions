def shift(sequenceList):
    sequenceList[2] = sequenceList[1]
    sequenceList[1] = sequenceList[0]
    sequenceList[0] = 0


def getMaxSequence(n):
    currentLongest = 1
    lastThreeSequences = [0, 0, 0]
    currentSearch = 0

    for x in range(0, n.bit_length()):
        if (n & 1 != currentSearch):        
            if (currentSearch == 1):
                currentLongest = max(currentLongest, findLongestSequence(lastThreeSequences))
            currentSearch = n & 1
            shift(lastThreeSequences)
        lastThreeSequences[0] += 1
        n = n >> 1
    
    # Just in case we end on a zero
    if (currentSearch == 0):
        # Ensure that the sequence going to findLongest is 1s 0s 1s
        shift(lastThreeSequences)
    currentLongest = max(currentLongest, findLongestSequence(lastThreeSequences))

    return currentLongest

def findLongestSequence(sequenceList):
    # The incoming sequence tuple will be length of 1s 0s 1s
    if (sequenceList[1] == 1):
        return sequenceList[0] + sequenceList[2] + 1
    elif (sequenceList[1] > 1):
        # Add a '1' to each of the adjacent sequences of 1 and return the max
        return max(sequenceList[0], sequenceList[2]) + 1
    else:
        # No zeros so far
        return max(sequenceList[0], sequenceList[2])

print getMaxSequence(108)