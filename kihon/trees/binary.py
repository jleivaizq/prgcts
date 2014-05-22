MAX_SIZE = 1000

class BinaryTree:

    def __init__(self, *args, **kwargs):
        self.base = [None] * MAX_SIZE
        self.root_index = 1
        
    def left(self, i):
        return i << 1

    def add_left(self, i, value):
        ## check size
        self.base[i << 1] = value

    def right(self, i): 
        return i << 1 | 1
    
    def add_right(self, i, value):
        ## check size
        self.base[i << 1 | 1] = value

    def _add(self, index, value):
        if self.base[index] == None:
            self.base[index] = value
        else:
            if value < self.base[index]:
                self._add(self.left(index), value)
            else:
                self._add(self.right(index), value)

    def add(self, value):
        self._add(self.root_index, value)

    def extend(self, value_list):
        for item in value_list:
            self.add(item)

    def to_str(self, i):
        if self.base[i] == None:
            return '-'
        else:
            return '{} -> ({}, {})'.format(self.base[i], 
                    self.to_str(self.left(i)),
                    self.to_str(self.right(i)))

    def __str__(self):
        return self.to_str(self.root_index)


