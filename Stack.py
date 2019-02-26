"""
My Stack implmentation
Stacks are First In, Last Out

"""
class Stack:
    def __init__(self):
        self.stack = list()
    
    def __repr__(self):
        return repr(self.stack)
    
    def pop_stack(self):
        # Return the First element of the stack.
        return self.stack.pop(0)
    
    def push_stack(self, data):
        self.stack.append(data)
    
    def find_in_stack(self, data):
        for s in self.stack:
            if s == data:
                return s
        return None
        
