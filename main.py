import sys


def graph(txtfile_name):
    try:
        file_object = open(txtfile_name, "r")
    except FileNotFoundError:
        print("ERROR! Can't read \"", txtfile_name, "\" file\nYou probably wrote wrongly your txt file", sep='')
        exit()
    file_object = open(txtfile_name, "r")
    capacity = list()
    node_destinations = {}

    for line in file_object.readlines():
        capacity.append(list(int(i) for i in line.split(',')))

    for node in range(len(capacity)):
        node_destinations[node] = list()

    for node, sizes in enumerate(capacity):
        for destination, size in enumerate(sizes):
            if size > 0:
                node_destinations[node].append(destination)

    return capacity, node_destinations


def print_graph(matrix, dest):
    for line in matrix:
        for element in line:
            print(element, end=" ")
        print("")
    print(dest)


def bfs(capacity, neighbors, flows, start, end):
    length = len(capacity)
    parents = [-1 for i in range(length)]
    parents[start] = -2
    list_of_floats = [0 for i in range(length)]
    list_of_floats[start] = 1000

    queue = list()
    queue.append(start)

    while queue:
        node = queue.pop(0)
        for dest_node in neighbors[node]:
            if capacity[node][dest_node] - flows[node][dest_node] > 0 and parents[dest_node] == -1:
                parents[dest_node] = node
                list_of_floats[dest_node] = min(list_of_floats[node], capacity[node][dest_node] - flows[node][dest_node])
                if dest_node == end:
                    return list_of_floats[end], parents
                else:
                    queue.append(dest_node)
    return 0, parents


def edmonds_karp(capacity, neighbors, start, end):
    print_graph(capacity, neighbors)

    flow = 0
    flows = [[0 for i in range(len(capacity))] for j in range(len(capacity))]
    while True:
        max, parent = bfs(capacity, neighbors, flows, start, end)
        if max == 0:
            break
        flow = flow + max
        v = end
        while v != start:
            u = parent[v]
            flows[u][v] = flows[u][v] + max
            flows[v][u] = flows[v][u] - max
            v = u
    return flow


if __name__ == "__main__":
    matrix, dest = graph("example.txt")

    print("Flow we can send in example graph:", edmonds_karp(matrix, dest, 0, len(matrix) - 1))

    if (len(sys.argv)-1) != 0:
        user_file = sys.argv[1]
    else:
        exit()

    matrix, dest = graph(user_file)

    print("Flow we can send in your graph:", edmonds_karp(matrix, dest, 0, len(matrix) - 1))
