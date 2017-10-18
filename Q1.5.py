def checkOneEdit(original, edited):
    # Compare lengths
    if (abs(len(original) - len(edited)) > 2):
        return False

    # Char-to-char comparison
    minLength = min(len(original), len(edited))
    differences = 0
    originalIsLonger = False
    if (len(edited) < len(original)):
        originalIsLonger = True
    index1 = 0
    index2 = 0
    for i in range (0, minLength - 1):
        if (original[index1] != edited[index2]):            
            differences += 1
            if (differences > 1):
                return False
            if (originalIsLonger):
                index1 += 1
                continue
            elif (len(edited) > len(original)):
                index2 += 1
                continue
        index1 += 1
        index2 += 1
        
    return True

print (checkOneEdit("pale", "ple"))
print (checkOneEdit("pales", "pale"))
print (checkOneEdit("spale", "pale"))
print (checkOneEdit("pale", "bale"))
print (checkOneEdit("pale", "bake"))
