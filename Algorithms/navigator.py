import random


def dijkstra(graph, src):
    visited = []
    distance = {src: 0}
    node = list(range(len(graph)))
    if src in node:
        node.remove(src)
        visited.append(src)
    else:
        return None
    for i in node:
        distance[i] = graph[src][i]
    v = src
    while node:
        _distance = float('inf')
        for i in visited:
            for j in node:
                if graph[i][j] > 0:
                    if _distance > distance[i] + graph[i][j]:
                        _distance = distance[j] = distance[i] + graph[i][j]
                        v = j
        visited.append(v)
        node.remove(v)
    return distance


aves = [str(i) + "ave" for i in range(1, 3)]
streets = [str(i) + "street" for i in range(1, 3)]
crossroads = [ave + " " + st for st in streets for ave in aves]

crossroads_matrix = []
for i in crossroads:
    _list = []
    for j in crossroads:
        if i == j:
            _list.append(0)
        elif abs(aves.index(i.split(" ")[0]) - aves.index(j.split(" ")[0])) == 1 \
                and streets.index(i.split(" ")[1]) == streets.index(j.split(" ")[1]) \
                or abs(streets.index(i.split(" ")[1]) - streets.index(j.split(" ")[1])) == 1 \
                and aves.index(i.split(" ")[0]) == aves.index(j.split(" ")[0]):
            _list.append(random.randint(1, 7))
        else:
            _list.append(float("inf"))
    crossroads_matrix.append(_list)


def min_way(src, destination, table):
    return dijkstra(table, src)[destination]


for i in crossroads_matrix:
    print(i)

print(min_way(0, 3, crossroads_matrix))
