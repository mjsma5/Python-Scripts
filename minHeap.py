class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def get_item(self):
        return self.item


class Heap:
    def __init__(self, size):
        self.heap = []
        self.size = size

    def push(self, item, value):
        if len(self.heap) == self.size:
            self.extract(item, value)
        else:
            self.insert(item, value)
        assert len(self.heap) <= self.size

    def extract(self, item, value):
        self.heap[0] = [item, value]
        index = 0
        while True:
            child = self.child(index)   # define lesser child
            if not child:
                break
            else:
                if self.heap[index][1] > self.heap[child][1]:  # check if parent is greater than child
                    tmp = self.heap[index]
                    self.heap[index] = self.heap[child]
                    self.heap[child] = tmp
                    index = child
                else:
                    break
    
    def insert(self, item, value): 
        self.heap.append([item, value])
        index = len(self.heap) - 1
        while True:
            parent = self.get_parent(index)
            if index != 0:
                if self.heap[index][1] < self.heap[parent][1]:  # check if parent is greater than child
                    tmp = self.heap[index]
                    self.heap[index] = self.heap[parent]
                    self.heap[parent] = tmp
                    index = parent
                else:
                    break
            else:
                break

    def get_parent(self, index):
        if index % 2 == 0:
            parent = (index - 2) / 2
        else:
            parent = (index - 1) / 2
        return parent

    def child(self, root): # identifies lesser child if one exists
        if len(self.heap)-1 < 2 * root + 1: # check for existing children
            if len(self.heap)-1 < 2 * root + 2: # check for 1 child
                if self.heap[2 * root + 1][1] <= self.heap[2 * root + 2][1]:    # check for lesser child
                    return 2 * root + 1
                else:
                    return 2 * root + 2
            else:
                return 2 * root + 1
        else:
            return False

    def __iter__(self):
        return self
