
### A Star Algorithm ###


from uniform_cost import Uniform_Cost


g = Uniform_Cost()
error = False

for i in range(0, g.constant):
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

    #tenho a matriz, falta construir o grafo em si

for i in range(0,g.constant):
    for j in range(0,g.constant):
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
    # print("X e Y:", g.X, g.Y)
    # print("Graph:", g.graph)
    g.uniform_cost()
    print("Saída:")
    for i in range(0,g.constant):
        for j in range(0,g.constant):
            print(g.matrix[i][j], end=" ")
        print()
    