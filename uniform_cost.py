from collections import defaultdict
from priority_queue import PriorityQueue
import math



class Uniform_Cost:
 
    def __init__(self):
        self.matrix = defaultdict(list)
        self.graph = defaultdict(list)
        self.X = 0
        self.Y = 0
        self.constant = 0
 
    def add_weighted_edge(self,u,v,w):
        self.graph[u].append({"node": v, "weight": w})

    def append_H_value(self, H_value):
        self.H.append(H_value)

    def uniform_cost(self):
        pi = self.uniform_cost_procedure(self.X)

        path = []
        path.append(self.Y)
        self.matrix[math.floor(self.Y / self.constant)][self.Y % self.constant] = 'X'
        end = pi[self.Y]    
        while end != -1:
            self.matrix[math.floor(end / self.constant)][end % self.constant] = 'X'
            path.append(end)
            end = pi[end]

        # return return_path

    def uniform_cost_procedure(self, x):

        G = []
        for i in range(0, (max(self.graph) + 1)):
            G.append(math.inf)
        G[x] = 0

        last = [-1] * (max(self.graph) + 1)

        queue = PriorityQueue()

        queue.insert((0, x))
 
        while not queue.isEmpty():

            x = queue.delete(1)
            
            queue_node = x[1]

            # looking at the neighboors
            for i in self.graph[queue_node]:
                visit_node = i.get("node")
                visit_weight = i.get("weight")
                current_distance = visit_weight + G[queue_node]
                if current_distance < G[visit_node]:
                    G[visit_node] = current_distance
                    last[visit_node] = queue_node
                    queue.insert((G[visit_node], visit_node))

        return last