"""
My implementation of a Singly Linked List.

TODO: Work on remove_last() and remove_first() methods.
TODO: Create a doubly linked list.
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return repr(self.data)
    

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        
    def prepend(self, head):
        if head == None:
            raise Exception
        if self.head == None:
            self.head = Node(head)
            
    def add_new_head(self, new_head):
        self.head = Node(new_head, self.head)
    
    def print_elements(self):
        if self.head == None:
            return None
        if self.head == self.tail:
            return self.head
        curr = self.head
        while curr:
            print(repr(curr), "-->")
            curr = curr.next
            if curr == None:
                print("end of the list!")
                break
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)
    
    def find(self, element):
        curr = self.head
        while curr and curr.data != element:
            curr = curr.next
        
        return curr
    
    def remove(self, item):
        if not item:
            raise Exception
        
        curr = self.head
        prev = None
        while curr and curr.data != item:
            prev = curr
            curr = curr.next
        
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
        
