class Node:
    def __init__(self, name, links=None):
        self.name = name
        if not links:
            self.links = [[], []]

    def add_link(self, node, weight):
        self.links[0].append(node)
        self.links[1].append(weight)
        if not (self in node.links[0]):
            node.links[0].append(self)
            node.links[1].append(weight)


def depth(visited, node):
    if not (node in visited):
        visited.append(node)
    else:
        return
    for arg in node.links[0]:
        if not (arg in visited):
            depth(visited, arg)


def width(visited, node):
    if not (node in visited):
        visited.add(node)
    else:
        return
    for arg in node.links[0]:
        if not (arg in visited):
            queue.append(arg)
    while queue:
        width(visited, queue.pop(0))


def edge(edges, node):
    for arg in node.links[0]:
        link_name = (node.name, arg.name)
        if (link_name not in edges[0]) and (link_name[::-1] not in edges[0]):
            edges[0].append(link_name)
            edges[1].append(node.links[1][node.links[0].index(arg)])
            edge(edges, arg)
    return


visited = set()
queue = []
arr = []
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.add_link(b, 5)
b.add_link(d, 5)
d.add_link(e, 7)
b.add_link(c, 8)
c.add_link(e, 11)

depth(arr, a)
print([x.name for x in arr])

width(visited, a)
print([x.name for x in visited])

edges = [[], []]
edge(edges, a)
print(edges)
