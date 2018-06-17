class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def getPossibleLists(tree):
    if (tree == None):
        return [[]]
    
    leftLists = getPossibleLists(tree.left)
    rightLists = getPossibleLists(tree.right)

    ret = []
    for left in leftLists:
        for right in rightLists:
            mergeLists(left, right, [tree.data], ret)
    return ret

# Take two lists and create all possible in-order combinations of the two lists and store them in ret
def mergeLists(left, right, prefix, ret):
    if not left:
        ret.append(prefix + right)
        return
    elif not right:
        ret.append(prefix + left)
        return
    
    mergeLists(left[1:], right, prefix+[left[0]], ret)
    mergeLists(left, right[1:], prefix+[right[0]], ret)


node0 = Tree(0)
node2 = Tree(2)
node4 = Tree(4)
node1 = Tree(1)
node1.left = node0
node1.right = node2

node3 = Tree(3)
node3.left = node1
node3.right = node4

result = getPossibleLists(node3)
for LoL in result:
    print (LoL)