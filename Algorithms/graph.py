graph_old = {1: [4, 3], 2: [4, 5], 3: [1, 6], 4: [1, 5], 5: [2, 4, 7], 6: [3, 7], 7: [5, 6]}
graph_new = {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [5], 5: [4], 6: [7], 7: [6]}
g = {1: [2], 2: [1, 3], 3: [2], 4: [], 7: [], 5: [6], 6: [5]}


def depth(graph, visited, key=1):
    if key not in visited:
        visited.append(key)
    else:
        return
    for arg in graph[key]:
        if not (arg in visited):
            depth(graph, visited, arg)


# print(graph.keys())
# a = []
# depth(a)
# print(a)


# def width(key):
#     if not (key in visited):
#         visited.add(key)
#     else:
#         return
#     for arg in graph[key]:
#         if not (arg in visited):
#             queue.append(arg)
#     while queue:
#         width(queue.pop(0))

#
# visited = set()
# queue = []
# width(1)
# print(visited)


def components(graph):
    counter = 0
    all_visited = []
    for i in graph.keys():
        new_visited = []
        depth(graph, new_visited, key=i)
        new_visited.append(i)
        if set(new_visited) not in all_visited:
            counter += 1
            all_visited.append(set(new_visited))
    return counter


print(components(g))


def max_links(adjacency_matrix):
    ones = []
    for i in range(len(adjacency_matrix)):
        counter = 0
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                counter += 1
        ones.append((counter, i,))
    ones.sort(key=lambda x: x[1], reverse=True)
    return ones[0][1]


g1 = {1: [], 2: [1, 3], 3: [1, 2]}


def half_linked(graph):
    peaks = []
    for i in graph.keys():
        peaks.append(i)
    for i in graph.keys():
        visited = []
        depth(graph, visited, key=i)
        if set(visited) == set(peaks):
            return True
    return False


print(max_links([[0, 3, 1], [0, 0, 1], [0, 1, 1]]))
print(half_linked(g1))
