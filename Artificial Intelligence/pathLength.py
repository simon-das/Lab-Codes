def pathLength(x, y):
    i = 0
    s = 0
    for i in range(len(neighbour)):
        if neighbour[i][0] == x:
            z = neighbour[i][1]
            if z == y:
                return neighbour[i][2]
            elif pathLength(z, y) != -1:
                return neighbour[i][2] + pathLength(z, y)
            else:
                continue
    return -1

            
#main

neighbour = [('i', 'a', 35), ('i', 'b', 45), ('a', 'c', 20), ('a', 'd', 30),
             ('b', 'd', 25), ('b', 'e', 35), ('b', 'f', 27), ('c', 'd', 30),
             ('c', 'g', 47), ('d', 'g', 30), ('e', 'g', 25)]

print("input the vertices : ")
x = input()
y = input()
print(pathLength(x, y))
