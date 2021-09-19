# Modified implementation of PriorityQueue using tuple as value
import math


class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
    
    # for popping an element based on Priority
    def delete(self, type):
        try:
            min = 0
            for i in range(len(self.queue)):
                # acessing the second element ([0]) in the tuple: the heuristic of the node
                if self.queue[i][type] < self.queue[min][type]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print('ERRAO')
            exit()

    def clear(self):
        while not self.isEmpty():
            self.delete(0)