  """
Create Queue.py
a Queue is a first in first out data structure.
"""

class Queue:
    def __init__(self):
        self.queue = list()
    
    def add_to_que(self, data):
        self.queue.append(data)
    
    def remove_from_queue(self):
        return self.queue.pop(len(self.queue)-1)
    
    def __repr__(self):
        return repr(self.queue)

    
