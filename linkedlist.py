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
    
    # printing linked list
    def printList(self):
        printValue = self.head
        while printValue is not None:
            print(printValue.data)
            printValue = printValue.next
            
    # Inserting at the beginning of the existing list
    def insertFirst(self, new_node):
        newNode = Node(new_node)
        NewNode.next = self.head
        self.head = newNode
        
    # Inserting at the end of the linked list    
    def insertLast(self, new_node):
        newNode = Node(new_node)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newNode
        
    # method to insert a node in the middle of the list    
    def insertInside(self, middle_node, new_node):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        
        newNode = Node(new_node)
        newNode.next = middle_node.next
        middle_node.next = newNode
    
    def removeNode(self, node_to_remove):
        
   
