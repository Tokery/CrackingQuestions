def isSorted(stack):
    prevItem = stack[0]
    for item in stack:
        if item < prevItem:
            return False
    return True

def sortWithTwoStacks(stack1):
    if (not stack1 or isSorted(stack1)):
        return
    smallitem = stack1.pop()
    stack2 = []
    stack2.append(smallitem)

    
    for loopItem in reversed(stack1):
        item = stack1.pop()

        if (item >= smallitem):
            stack2.append(item)
            smallitem = item
        else:
            itemspopped = 0
            for stack2item in reversed(stack2):
                if (item >= stack2item):
                    break
                temp = stack2.pop()
                stack1.append(temp)
                itemspopped += 1

            stack2.append(item)
            while (itemspopped > 0):
                smallitem = stack1.pop()
                stack2.append(smallitem)
                itemspopped -= 1

    for x in range(0, len(stack2)):
        item = stack2.pop()
        stack1.append(item)
    # For testing only
    for item in reversed(stack1):
        print(item)

    

stack = [7,11,3,2,14]
sortWithTwoStacks(stack)
