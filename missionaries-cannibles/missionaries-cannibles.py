class Node:
    def __init__(self, m, c, side):
        self.m = m
        self.c = c
        self.side = side

    def get_value_str(self):
        return str([self.m, self.c, self.side])

    def get_value(self):
        return [self.m, self.c, self.side]


class Graph:
    def __init__(self, root):
        self.root = root
        self.res = []
        self.graph = {str(self.root.get_value()): []}
        self.nodes = []

    def print_res(self):
        if len(self.res) > 0:
            self.res.append(self.root.get_value_str())
            print('->'.join(self.res[::-1]))
        else:
            print('Not Found')
        quit()

    def dfs(self, parent, count_0, count_1):
        found = False
        child = None
        count_0 = 0
        count_1 = 0
        while not found:
            child = get_child_node(parent, count_0, count_1)
            if parent.side == 0:
                count_0 += 1
            else:
                count_1 += 1
            if (child.m == 0 or child.m == 3 or (
                    child.m - child.c == 0)) and child.get_value_str() not in self.nodes:
                self.graph[parent.get_value_str()] = child.get_value_str()
                self.graph[child.get_value_str()] = []
                self.nodes.append(child.get_value_str())
                if child.m == 0 and child.c == 0 and child.side == 0:
                    found = True
                    self.res.append(child.get_value_str())
                    return
                self.dfs(child, count_0, count_1)
                self.res.append(child.get_value_str())
                return
        else:
            self.res.append(child.get_value_str())
            return

    def bfs(self):
        pass

    def populate_graph(self):
        self.dfs(self.root, 0, 0)


def get_child_node(parent, count_0, count_1):
    if parent.side == 0:
        if count_0 == 0:
            child = Node(parent.m + 1, parent.c, 1)
        elif count_0 == 1:
            child = Node(parent.m, parent.c + 1, 1)
        elif count_0 == 2:
            child = Node(parent.m + 2, parent.c, 1)
        elif count_0 == 3:
            child = Node(parent.m, parent.c + 2, 1)
        elif count_0 == 4:
            child = Node(parent.m + 1, parent.c + 1, 1)
    else:
        if count_1 == 0:
            child = Node(parent.m - 2, parent.c, 0)
        elif count_1 == 1:
            child = Node(parent.m, parent.c - 2, 0)
        elif count_1 == 2:
            child = Node(parent.m - 1, parent.c - 1, 0)
    return child


def main():
    mis, can = map(int, input().split(' '))
    n = Node(mis, can, 1)
    g = Graph(n)
    g.populate_graph()
    g.print_res()


if __name__ == '__main__':
    main()
