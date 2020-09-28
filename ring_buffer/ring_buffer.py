class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.index = 0

    def append(self, item):
        # if there are less than self.length add item to list 
        # if len(self) is greater than == self.capacity -1
        # item = self.append(0)
        if len(self.list) < self.capacity:
            self.list.append(item)
        else:
            if self.index == len(self.list):
                self.index = 0
            self.list[self.index] = item
            self.index +=1


    def get(self):
        return self.list