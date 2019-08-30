class IterativeBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        while True:
            if value < current.value:
                if current.value is None:
                    current.left = IterativeBST(value)
                else:
                    current = current.left
            else:
                if current.value is None:
                    current.right = IterativeBST(value)
                else:
                    current = current.right

        return self
    
    def contains(self, target):
        current = self
        if current.value > target:
            current = current.right
        elif current.value < target:
            current = current.left
        else:
            return True

        return False

    def remove(self, value, parent=None):
        current = self
        while current is not None:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                if current.left is not None and current.right is not None:
                    current.value = current.right.getMinValue()
                    current.right.remove(current.value, current)

                elif parent.left == current:
                    parent.left = current.left is current.left is not None else current.right
            
            return self


    def getMinValue(self):
        current = self
        while current.left is not None:
            current = current.left 
        return current.value


class RecursiveBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = RecursiveBST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = RecursiveBST(value)
            else:
                self.right.insert(value)
        
        return self

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True
    
    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value >  self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                # no children (sadface)
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    self.value = None 
            
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right is self:
                parent.right = self.left if self.left is not None else self.right
        
        return self 

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()