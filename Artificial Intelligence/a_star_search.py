def sortLast(val):
    return val[-1]


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

queue = []
initial_list = []
total = 0

while True:
    for key, value in edges.items():
        temp_list = initial_list
        temp_total = total
        if key == initial_vertex:
            temp_total = temp_total + value[1] + vertices[value[0]]
            temp_list.append(value[0])
            temp_list.append(temp_total)
            queue.append(temp_list)

    queue.sort(key = sortLast, reverse = True)
    initial_list = queue.pop()
    if initial_list[-2] == goal_vertex:
        break
    total = initial_list.pop()
    initial_vertex = initial_list[-1]


print("The path is :", ini_vertex, end = " ")
for i in initial_list:
    if i != initial_list[-1]:
        print( i, end = " ")
        
print("\nThe total cost is : ", initial_list[-1])
