adjacent_nodes = {
    'a' : [('b', 4), ('c', 3)],
    'b' : [('e', 12), ('f', 5)],
    'c' : [('d', 7), ('e', 10)],
    'd' : [('e', 2)],
    'e' : [('g', 5)],
    'f' : [('g', 16)]
    }

heuristic_values = {
    'a' : 14,
    'b' : 12,
    'c' : 11,
    'd' : 6,
    'e' : 4,
    'f' : 11,
    'g' : 0
    }

def a_star_algorithm(start_node, stop_node):
        open_list = [start_node]

        g = {}

        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + heuristic_values[v] < g[n] + heuristic_values[n]:
                    n = v;

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {} with the length of {}'.format(reconst_path,
                                                                  g[stop_node]))
                return reconst_path


            for (m, weight) in adjacent_nodes[n]:

                if m not in open_list:
                    open_list.append(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

            open_list.remove(n)

        print('Path does not exist!')
        return None

start_node, stop_node = input("Enter the starting node and ending node : ").split()
a_star_algorithm(start_node, stop_node)
