
### A Star Algorithm ###


from a_star import A_Star
from uniform_cost import Uniform_Cost

size = 5

matrix = [
    ["X", "-", "-", "#", "Y"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

g = A_Star()
error = False
g.constant = size

g.matrix = matrix

    #tenho a matriz, falta construir o grafo em si

for i in range(0,g.constant):
    for j in range(0,g.constant):
        if g.matrix[i][j] != "#":
            node_char = g.matrix[i][j]
            node = (j+(i*g.constant))
            # print("Node:", node)
            if node_char == 'X':
                g.X = node
            if node_char == 'Y':
                g.Y_position = (i,j)
                g.Y = node
            if j+1 < g.constant and g.matrix[i][j+1] != '#':
                r = g.matrix[i][j+1]
                r_node = ((j+1)+(i*g.constant))
                # print("R_node:", r_node)
                g.add_weighted_edge(node, r_node, 1)
            if j-1 >= 0 and g.matrix[i][j-1] != '#':
                l = g.matrix[i][j-1]
                l_node = ((j-1)+(i*g.constant))
                # print("L_node:", l_node)
                g.add_weighted_edge(node, l_node, 1)
            if i-1 >= 0 and g.matrix[i-1][j] != '#':
                t = g.matrix[i-1][j]
                t_node = (j+((i-1)*g.constant))
                # print("T_node:", t_node)
                g.add_weighted_edge(node, t_node, 1)
            if i+1 < g.constant and g.matrix[i+1][j] != '#':
                b = g.matrix[i+1][j]
                b_node = (j+((i+1)*g.constant))
                # print("B_node:", b_node)
                g.add_weighted_edge(node, b_node, 1)


if not error:
    # print("X e Y:", g.X, g.Y)
    # print("Graph:", g.graph)
    g.a_star()
    print("Y position:", g.Y_position)
    print("Saída:")
    for i in range(0,g.constant):
        for j in range(0,g.constant):
            print(g.matrix[i][j], end=" ")
        print()
    

g = Uniform_Cost()
error = False
g.constant = size

g.matrix = matrix

# n = int(input())
# g.constant = n

# for i in range(0, g.constant):        
#     for j in range(0, g.constant):
#         a = int(input())
#         if a!='#' and a!='-' and a!='X' and a!='Y':
#             print("Simbolo Inválido!!!")
#             error = True
#             break

#         g.matrix[i].append(a)
    
    #tenho a matriz, falta construir o grafo em si

for i in range(0,g.constant):
    for j in range(0,g.constant):
        if g.matrix[i][j] != "#":
            node_char = g.matrix[i][j]
            node = (j+(i*g.constant))
            # print("Node:", node)
            if node_char == 'X':
                g.X = node
            if node_char == 'Y':
                g.Y = node
            if j+1 < g.constant and g.matrix[i][j+1] != '#':
                r = g.matrix[i][j+1]
                r_node = ((j+1)+(i*g.constant))
                # print("R_node:", r_node)
                g.add_weighted_edge(node, r_node, 1)
            if j-1 >= 0 and g.matrix[i][j-1] != '#':
                l = g.matrix[i][j-1]
                l_node = ((j-1)+(i*g.constant))
                # print("L_node:", l_node)
                g.add_weighted_edge(node, l_node, 1)
            if i-1 >= 0 and g.matrix[i-1][j] != '#':
                t = g.matrix[i-1][j]
                t_node = (j+((i-1)*g.constant))
                # print("T_node:", t_node)
                g.add_weighted_edge(node, t_node, 1)
            if i+1 < g.constant and g.matrix[i+1][j] != '#':
                b = g.matrix[i+1][j]
                b_node = (j+((i+1)*g.constant))
                # print("B_node:", b_node)
                g.add_weighted_edge(node, b_node, 1)


if not error:
    # print("X e Y:", g.X, g.Y)
    # print("Graph:", g.graph)
    g.uniform_cost()
    print("Saída:")
    for i in range(0,g.constant):
        for j in range(0,g.constant):
            print(g.matrix[i][j], end=" ")
        print()
    