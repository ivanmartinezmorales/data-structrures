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
    
    # Method to remove a given node in the linked list.
    def removeNode(self, node_to_remove):
        headValue = self.head
        if (headValue is not None):
            if (headValue.data == node_to_remove):
                self.head = headValue.next
                headValue = None
                return
            
        while (headValue is not None):
            if headValue.data == node_to_remove:
                break
            prev = headValue
            headValue = headValue.next
            
        if (headValue == None):
            return
        
        prev.next = headValue.next
        headValue = None
'''
Here, I am calling our linked list, performing the following operations:
-Creating the linked list as our_list
-Creating three nodes, and linking them together. (l1, l2, l3)
'''
our_list = singlyLinked()
our_list.head = ("first item")

l2 = Node("second item")
l3 = Node("third item")

# Linking the three Nodes together
our_list.head.next = l2
l2.next = l3

# Inserting a Node at the beginning of the list:
our_list.insertFirst("zero-th item")

# Inserting a node at the end of the list:
our_list.insertLast("fourth item")

# Inserting in the middle of the list:
our_list.head.next = l3
our_list.insertInside(our_list.head.next, "weird item")

# Removing the weird node we just created:
our_list.removeNode("weird item")

# Printing our final list:
our_list.print_list()


