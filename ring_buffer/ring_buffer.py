class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldestIndex = 0

    def append(self, item):
        if len(self.storage) != self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.oldestIndex] = item
            if self.oldestIndex == self.capacity - 1:
                self.oldestIndex = 0
            else:
                self.oldestIndex += 1
            
            

    def get(self):
        return self.storage
