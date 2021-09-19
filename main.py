
import time
from copy import deepcopy
from datetime import timedelta

from a_star import A_Star
from uniform_cost import Uniform_Cost

maze_size = 8

matrix_input = [
    ["X", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["#", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["Y", "-", "-", "-", "-", "-", "-", "-"]
]

a_star = A_Star()
uniform_cost = Uniform_Cost()

a_star.constant = maze_size
a_star.matrix = deepcopy(matrix_input)

uniform_cost.constant = maze_size
uniform_cost.matrix = deepcopy(matrix_input)

error = False


###############################################################         A Star          ########################################################################
#tenho a matriz, falta construir o grafo em si

for i in range(0,a_star.constant):
    for j in range(0,a_star.constant):
        if a_star.matrix[i][j] != "#":
            node_char = a_star.matrix[i][j]
            node = (j+(i*a_star.constant))
            # print("Node:", node)
            if node_char == 'X':
                a_star.X = node
            if node_char == 'Y':
                a_star.Y_position = (i,j)
                a_star.Y = node
            if j+1 < a_star.constant and a_star.matrix[i][j+1] != '#':
                r = a_star.matrix[i][j+1]
                r_node = ((j+1)+(i*a_star.constant))
                # print("R_node:", r_node)
                a_star.add_weighted_edge(node, r_node, 1)
            if j-1 >= 0 and a_star.matrix[i][j-1] != '#':
                l = a_star.matrix[i][j-1]
                l_node = ((j-1)+(i*a_star.constant))
                # print("L_node:", l_node)
                a_star.add_weighted_edge(node, l_node, 1)
            if i-1 >= 0 and a_star.matrix[i-1][j] != '#':
                t = a_star.matrix[i-1][j]
                t_node = (j+((i-1)*a_star.constant))
                # print("T_node:", t_node)
                a_star.add_weighted_edge(node, t_node, 1)
            if i+1 < a_star.constant and a_star.matrix[i+1][j] != '#':
                b = a_star.matrix[i+1][j]
                b_node = (j+((i+1)*a_star.constant))
                # print("B_node:", b_node)
                a_star.add_weighted_edge(node, b_node, 1)


if not error:
    # print("X e Y:", a_star.X, a_star.Y)
    # print("Graph:", a_star.graph)
    a_star_start_time = time.perf_counter()
    a_star.a_star()
    a_star_end_time = time.perf_counter()
    print("Saída A*:")
    for i in range(0,a_star.constant):
        for j in range(0,a_star.constant):
            print(a_star.matrix[i][j], end=" ")
        print()
    print("Nós considerados:", a_star.visited_list)
    print("Qtde:", len(a_star.visited_list))
    print('Tempo de execução:', a_star_end_time - a_star_start_time)
    
#clear queue (confirmar se vai precisar)

###############################################################         Uniform Cost          ########################################################################
    
#tenho a matriz, falta construir o grafo em si

error = False

for i in range(0,uniform_cost.constant):
    for j in range(0,uniform_cost.constant):
        if uniform_cost.matrix[i][j] != "#":
            node_char = uniform_cost.matrix[i][j]
            node = (j+(i*uniform_cost.constant))
            if node_char == 'X':
                uniform_cost.X = node
            if node_char == 'Y':
                uniform_cost.Y = node
            if j+1 < uniform_cost.constant and uniform_cost.matrix[i][j+1] != '#':
                r = uniform_cost.matrix[i][j+1]
                r_node = ((j+1)+(i*uniform_cost.constant))
                uniform_cost.add_weighted_edge(node, r_node, 1)
            if j-1 >= 0 and uniform_cost.matrix[i][j-1] != '#':
                l = uniform_cost.matrix[i][j-1]
                l_node = ((j-1)+(i*uniform_cost.constant))
                uniform_cost.add_weighted_edge(node, l_node, 1)
            if i-1 >= 0 and uniform_cost.matrix[i-1][j] != '#':
                t = uniform_cost.matrix[i-1][j]
                t_node = (j+((i-1)*uniform_cost.constant))
                uniform_cost.add_weighted_edge(node, t_node, 1)
            if i+1 < uniform_cost.constant and uniform_cost.matrix[i+1][j] != '#':
                b = uniform_cost.matrix[i+1][j]
                b_node = (j+((i+1)*uniform_cost.constant))
                uniform_cost.add_weighted_edge(node, b_node, 1)


if not error:
    # print("X e Y:", uniform_cost.X, uniform_cost.Y)
    # print("Graph:", uniform_cost.graph)
    uniform_cost_start_time = time.perf_counter()
    uniform_cost.uniform_cost()
    uniform_cost_end_time = time.perf_counter()
    print("Saída Custo Uniforme:")
    for i in range(0,uniform_cost.constant):
        for j in range(0,uniform_cost.constant):
            print(uniform_cost.matrix[i][j], end=" ")
        print()
    print("Nós considerados:", uniform_cost.visited_list)
    print("Qtde:", len(uniform_cost.visited_list))
    print('Tempo de execução:',uniform_cost_end_time - uniform_cost_start_time)
    



    
# for i in range(0, uniform_cost.constant):        
#     for j in range(0, uniform_cost.constant):
#         a = int(input())
#         if a!='#' and a!='-' and a!='X' and a!='Y':
#             print("Simbolo Inválido!!!")
#             error = True
#             break

#         uniform_cost.matrix[i].append(a)