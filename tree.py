"""
Create Tree class
Trees are non-linear data structures, comprised of nodes.
"""

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data: # the values going to the left
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
                    
            elif data > self.data: # the values going to the right
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
                    
            else:
                self.data = data
    
    def print_tree(self):
        if self.left:
            self.left.print_tree() # Recursive call
        print(self.data)
        if self.right:
            self.right.print_tree() # Recursive call
            
    def find_node(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.find_node(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.find_node(data, self)
        else:
            return self, parent
        
