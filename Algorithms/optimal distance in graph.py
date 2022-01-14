# Floyd's algorithm поддерживает отрицательные значения
def floyd(c):
    a = c.copy()
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                new_w = a[i][k] + a[k][j]
                if new_w < a[i][j]:
                    a[i][j] = new_w
    return a


c = [[0, 8, 5], [3, 0, float('inf')], [float('inf'), 2, 0]]
print(floyd(c))


# жадный алгоритм не поддерж отриц знач
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
