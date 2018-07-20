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
        
