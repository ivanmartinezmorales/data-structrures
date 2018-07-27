'''
Created a binary search tree in like 15 minutes... sorry for mistakes :)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data) # using recursion??
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data) # using recursion? hmm
        else:
            self.data = data
           
'''

'''
