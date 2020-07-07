class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = [None] * capacity
        self.capacity_counter = 0
    def append(self, item):
        if self.capacity_counter < self.capacity:
            self.list[self.capacity_counter] = item
            self.capacity_counter = self.capacity_counter+1
        else:
            self.capacity_counter = 0
            self.list[self.capacity_counter] = item


    def get(self):
        for i in range(self.capacity):
            if self.list[i] == None:
                self.list[i].remove(None)
        return self.list