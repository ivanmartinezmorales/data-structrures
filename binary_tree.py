'''
B I N A R Y T R E E S

A tree is a data structure were nodes are connected by their edges.
Here are some properties:

One node is the root node
Each node is associated with one parent node.
Each node can have n number of children.

In order to create a tree, we will create nodes. The nodes will be their own class
they will have the following variables:
- left
- right
- data
'''

class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

'''
Function to insert 
'''
    def insert(self, data):
        if self.data:
            if data < self.data: 
            # if our inserted node is less than the parent node, then insert left
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
            # if our inserted data is greater than our parent node, insert right.
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
            
            
