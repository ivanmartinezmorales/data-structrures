'''
Learning about linked lists!

First, I created a class for nodes. The node holds data for every item in the linked list.
Then in the singlyLinked class, __init__ declares the head. 
'''

# Creating a node:

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
# Creating the single linked list        
class singlyLinked:
    def __init__(self):
        self.head = None
    
    # Method to traverse LL
    def printList(self):
        printValue = self.head
        while printValue is not None:
            print(printValue.data)
            printValue = printValue.next
            
    def insertFirst(self, new_node):
        newNode = Node(new_node)
        
  
