vertices = {'i' : 80, 'a' : 55, 'b' : 42, 'c' : 34, 'd' : 25, 'e' : 20, 'f' : 17,
            'g' : 0}
edges = {'i' : ['a', 35], 'i' : ['b', 45], 'a' : ['i', 35], 'a' : ['c', 22],
         'a' : ['d', 32], 'b' : ['i', 45], 'b' : ['d', 28], 'b' : ['e', 36],
          'b' : ['f', 27], 'c' : ['a', 22], 'c' : ['d', 31],
          'c' : ['g', 47], 'd' : ['a', 32], 'd' : ['b', 28], 'd' : ['c', 31],
          'd' : ['g', 30], 'e' : ['b', 36], 'e' : ['g', 26], 'f' : ['b', 27],
            'g' : ['c', 47], 'g' : ['d', 30], 'f' : ['e', 26]}


initial_vertex = 'i'
ini_vertex = initial_vertex
goal_vertex = 'g'
mini = None

total = 0
path = []

while True:
    queue = {}
    cost = {}
    for key, value in edges.items():
        if key == initial_vertex:
            queue[value[0]] = vertices[value[0]]
            cost[value[0]] = value[1]

    mini = min(queue, key = queue.get)
    total = total + cost[mini]
    initial_vertex = mini
    path.append(mini)
    if mini == goal_vertex:
        break

print("The path is :", ini_vertex, end = " ")
for i in path:
    print( i, end = " ")
print("\nThe total cost is : ", total)
