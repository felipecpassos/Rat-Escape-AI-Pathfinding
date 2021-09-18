from collections import defaultdict
from priority_queue import PriorityQueue
import math



class Matrix_Pathfinding:
 
    def __init__(self):
        self.matrix = defaultdict(list)
        self.graph = defaultdict(list)
        self.X = 0
        self.Y = 0
 
    def add_weighted_edge(self,u,v,w):
        self.graph[u].append({"node": v, "weight": w})

    def append_H_value(self, H_value):
        self.H.append(H_value)

    def uniform_cost(self):
        pi = self.uniform_cost_procedure(self.X)

        path = []
        path.append(self.Y)
        end = pi[self.Y]
        while end != -1:
            path.append(end)
            end = pi[end]
        path.reverse()
        return_path = ""
        for i in path:
            if (i == self.Y):
                return_path = return_path + str(i)
            else:
                return_path = return_path + str(i) + "-"


        return return_path

    def uniform_cost_procedure(self, x):

        #A*
            # F = []
            # for i in self.graph:
            #     F.append(math.inf)
            # F[x] = 0
        G = []
        for i in range(0, (max(self.graph) + 1)):
            G.append(math.inf)
        G[x] = 0

        last = [-1] * (max(self.graph) + 1)

        queue = PriorityQueue()

        queue.insert((0, x))
 
        while not queue.isEmpty():

            x = queue.delete()
            
            queue_node = x[1]

            # print("Olha o node: ", queue_node)

            # looking at the neighboors
            for i in self.graph[queue_node]:
                visit_node = i.get("node")
                visit_weight = i.get("weight")
                # print("Olha o visited node e weight:", i)
                current_distance = visit_weight + G[queue_node]
                # print("current distance: ", current_distance)
                if current_distance < G[visit_node]:
                    G[visit_node] = current_distance
                    last[visit_node] = queue_node
                    queue.insert((G[visit_node], visit_node))

        # print("F:", F)
        # print("G:", G)
        # print("last: ", last)
        return last


### A Star Algorithm ###
g = Matrix_Pathfinding()
error = False
constant = 4

for i in range(0, constant):
    abcd = input()
    a = abcd.split(" ")[0]
    b = abcd.split(" ")[1]
    c = abcd.split(" ")[2]
    d = abcd.split(" ")[3]
    if a!='#' and a!='-' and a!='X' and a!='Y':
        print("Simbolo Inválido!!!")
        error = True
        break
    if b!='#' and b!='-' and b!='X' and b!='Y':
        print("Simbolo Inválido!!!")
        error = True
        break
    if c!='#' and c!='-' and c!='X' and c!='Y':
        print("Simbolo Inválido!!!")
        error = True
        break
    if d!='#' and d!='-' and d!='X' and d!='Y':
        print("Simbolo Inválido!!!")
        error = True
        break

    g.matrix[i].append(a)
    g.matrix[i].append(b)
    g.matrix[i].append(c)
    g.matrix[i].append(d)

for i in range(0,constant):
    for j in range(0,constant):
        if g.matrix[i][j] != "#":
            node_char = g.matrix[i][j]
            node = (j+(i*4))
            # print("Node:", node)
            if node_char == 'X':
                g.X = node
            if node_char == 'Y':
                g.Y = node
            if j+1 < 4 and g.matrix[i][j+1] != '#':
                r = g.matrix[i][j+1]
                r_node = ((j+1)+(i*4))
                # print("R_node:", r_node)
                g.add_weighted_edge(node, r_node, 1)
            if j-1 >= 0 and g.matrix[i][j-1] != '#':
                l = g.matrix[i][j-1]
                l_node = ((j-1)+(i*4))
                # print("L_node:", l_node)
                g.add_weighted_edge(node, l_node, 1)
            if i-1 >= 0 and g.matrix[i-1][j] != '#':
                t = g.matrix[i-1][j]
                t_node = (j+((i-1)*4))
                # print("T_node:", t_node)
                g.add_weighted_edge(node, t_node, 1)
            if i+1 < 4 and g.matrix[i+1][j] != '#':
                b = g.matrix[i+1][j]
                b_node = (j+((i+1)*4))
                # print("B_node:", b_node)
                g.add_weighted_edge(node, b_node, 1)

if not error:
    # print("Matrix:", g.matrix)
    # print("X e Y:", g.X, g.Y)
    # print("Graph:", g.graph)
    print("Path:", g.uniform_cost())
    