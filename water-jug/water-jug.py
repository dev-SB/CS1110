class Node:
    def __init__(self, left, right, parent):
        self.left = left
        self.right = right
        self.parent = parent

    def get_value_str(self):
        return str([self.left, self.right])

    def get_value(self):
        return [int(self.left), int(self.right)]


class Graph:
    def __init__(self, root, capacity, required):
        self.root = root
        self.graph = {self.root: []}
        self.capacity = capacity
        self.required = required
        self.res = ''
        self.res_str = []

    def populate_graph_bfs(self):
        nodes = [Node(self.capacity[0], 0, self.root), Node(0, self.capacity[1], self.root)]
        self.graph[self.root] = nodes
        self.graph[nodes[0]] = []
        self.graph[nodes[1]] = []
        bfs(self)
        return

    def populate_graph_dfs(self):
        nodes = [Node(self.capacity[0], 0, self.root)]
        self.graph[self.root] = nodes
        self.graph[nodes[0]] = []

        if not dfs(nodes[0], self):
            nodes = [Node(0, self.capacity[1], self.root)]
            self.graph[self.root] = nodes
            self.graph[nodes[1]] = []

            dfs(nodes[1], self)
        return


def create_res(node, g):
    g.res_str.append('(' + str(node.left) + ',' + str(node.right) + ')')
    if node and node.parent != 0:
        create_res(node.parent, g)
    return


def get_children(capacity, nodes):
    children = []
    node = [nodes.left, nodes.right]
    children.append([0, node[1]])
    children.append([node[0], 0])
    children.append([capacity[0], node[1]])
    children.append([node[0], capacity[1]])

    total = node[0] + node[1]
    left = max(total - capacity[0], 0)
    children.append([total - left, left])

    left = max(total - capacity[1], 0)
    children.append([left, total - left])
    return children


def bfs(g):
    temp_dict_keys = list(g.graph.keys()).copy()
    for parent in temp_dict_keys:
        if not g.graph[parent]:
            children = get_children(g.capacity, parent)
            for i in children:
                if not exists(g.graph, i[0], i[1]):
                    n = Node(i[0], i[1], parent)
                    g.graph[parent].append(n)
                    g.graph[n] = []
                    found = solution_found(g, i)
                    if found:
                        g.res = n
                        return True


def dfs(node, g):
    for i in range(6):
        if i == 0:
            child = [0, node.right]
        elif i == 1:
            child = [node.left, 0]
        elif i == 2:
            child = [g.capacity[0], node.right]
        elif i == 3:
            child = [node.left, g.capacity[1]]
        elif i == 4:
            total = node.left + node.right
            left = max(total - g.capacity[0], 0)
            child = [total - left, left]
        else:
            total = node.left + node.right
            left = max(total - g.capacity[1], 0)
            child = [left, total - left]
        n = check_dfs(g, node, child)
        if solution_found(g, child):
            g.res = n
            return True
        if n:
            if dfs(n, g):
                return True
    return


def check_dfs(g, node, child):
    if not exists(g.graph, child[0], child[1]):
        n = Node(child[0], child[1], node)
        g.graph[node].append(n)
        g.graph[n] = []
        return n
    return None


def solution_found(g, node):
    return g.required == node


def exists(g, left, right):
    for i in g.keys():
        if i.left == left and i.right == right:
            return True
    return False


def main():
    capacity = list(map(int, input('Enter space separated initial capacities').split(' ')))
    required = list(map(int, input('Enter space separated final values').split(' ')))
    n = Node(0, 0, 0)
    print('bfs:')
    g_bfs = Graph(n, capacity, required)
    g_bfs.populate_graph_bfs()
    if g_bfs.res:
        create_res(g_bfs.res, g_bfs)
        print('->'.join(g_bfs.res_str[::-1]))
    else:
        print('Not Found')
    print('dfs:')
    g_dfs = Graph(n, capacity, required)
    g_dfs.populate_graph_dfs()
    if g_dfs.res:
        create_res(g_dfs.res, g_dfs)
        print('->'.join(g_dfs.res_str[::-1]))
    else:
        print('Not Found')


if __name__ == '__main__':
    main()
