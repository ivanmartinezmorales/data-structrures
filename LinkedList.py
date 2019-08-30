class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def setHead(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return 
        self.insertBefore(self.head, node)
    
    def insertBefore(self, node, newNode):
        if newNode == self.head and newNode == self.tail:
            return
        self.remove(newNode)
        newNode.prev = node.prev
        newNode.next = node
        
        if node.prev is None:
            self.head = newNode
        else:
            node.prev.next = newNode
        node.prev = newNode
    
    def insertAfter(self, node, newNode):
        if newNode == self.head and newNode == self.tail:
            return
        self.remove(newNode)
        newNode.prev = node
        newNode.next = node.next
        if node.next is None:
            self.tail = newNode
        else:
            node.next.prev = newNode
        node.next = newNode

    def insertAtPosition(self, position, newNode):
        if position == 1:
            self.setHead(newNode)
            return
        node = self.head
        currentPosition = 1
        while node is None and currentPosition != position:
            node = node.next
            currentPosition += 1
        
        if node is not None:
            self.insertBefore(node, newNode)
        else:
            self.setTail(newNode)
        
    def removeNodesWithValue(self, value):
        cursor = self.head
        while cursor is not None and cursor.value != value:
            cursorToRemove = cursor
            cursor = cursor.next
            if cursorToRemove.value == value:
                self.removeNodeBindings(cursorToRemove)
    
    def remove(self, node):
        if (node == self.head):
            self.head = self.head.next
        if (node == self.tail):
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        cursor = self.head
        while cursor is not None and cursor.value != value:
            cursor = cursor.next
        
        return cursor is not None
    
    def removeNodeBindings(self, node):
        # Helper method for removing a node from a given position.
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        
        node.prev = None
        node.next = None 
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None 

    def __repr__(self):
        return f"Node(Value: {self.value}. Next: {self.next})"
    