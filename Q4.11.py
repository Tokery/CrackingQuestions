import random
# In this definition, a single node has a size of 1
class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,i):
        if (not self.root):
            self.root = Node(i)
            self.size += 1
        else:
            self.root.insert(i)
            self.size += 1
    def getRandomNode(self):
        index = random.randint(0, self.size-1)
        if not self.root:
            return None
        return self.root.getIndex(index)

class Node:
    def __init__(self, data):
        self.size = 1
        self.left = None
        self.right = None
        self.data = data

    def getSize(self):
        return self.size
    
    def getIndex(self, index):
        leftSize = 0 if not self.left else self.left.getSize()
        if (index < leftSize):
            return self.left.getIndex(index)
        elif (leftSize == index):
            return self
        else:
            return self.right.getIndex(index - (leftSize + 1))
    
    def insert(self, data):
        # Assuming unique data
        if (data < self.data):
            if (not self.left):
                self.left  = Node(data)
            else:
                self.left.insert(data)
        else:
            if (not self.right):
                self.right = Node(data)
            else:
                self.right.insert(data)
        self.size += 1

    def find(self, data):
        if (data == self.data):
            return self
        elif (data < self.data):
            return None if not self.left else self.left.find(data)
        else:
            return None if not self.right else self.right.find(data)

tree = Tree()
tree.insert(3)
tree.insert(4)
tree.insert(0)
tree.insert(1)

print tree.getRandomNode().data