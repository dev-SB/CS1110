import copy


class Grid:
    def __init__(self, grid, blank_r, blank_c, parent):
        self.grid_value = grid
        self.blank_r = blank_r
        self.blank_c = blank_c
        self.parent = parent

    def get_value_str(self):
        return str(self.grid_value)

    def get_value(self):
        return self.grid_value


# {parent:[children objects with attributes]}
# {child.value:[]}
class Graph:
    def __init__(self, root):
        self.root = root
        self.graph = {root: []}

    def append_children(self, parent, children, rows, cols):
        for i in range(4):
            if children[i] and not exists(children[i], self.graph):
                c = Grid(children[i], rows[i], cols[i], parent)
                self.graph[parent].append(c)
                self.graph[c] = []


def exists(value, g):
    for i in g.keys():
        if i.grid_value == value:
            return True
    return False


def main():
    # use 0 for blank
    grid_in = list(map(int, input(
        'Grid values (0 for blank) space separated, result is sorted grid with space at last:').split(' ')))
    # grid_in = [1, 2, 3, 0, 4, 6, 7, 5, 8]
    print('Determining Solution...')
    grid_sol = sorted(grid_in)
    grid_sol = grid_sol[1:9] + [grid_sol[0]]
    blank_r = 0
    blank_c = 0
    for i in range(len(grid_in)):
        if grid_in[i] == 0:
            blank_c = i % 3
            if i <= 2:
                blank_r = 0
            elif i <= 5:
                blank_r = 1
            else:
                blank_r = 2
            break
    grid = Grid([[grid_in[i + j] for j in range(3)] for i in range(0, 9, 3)], blank_r, blank_c, 0)
    grid_sol = [[grid_sol[i + j] for j in range(3)] for i in range(0, 9, 3)]
    g = Graph(grid)
    if check([grid.get_value()], grid_sol):
        print_res(g.root)
    else:
        print(bfs(g, grid_sol, 1))


def bfs(g, grid_sol, depth):
    temp_dict_keys = list(g.graph.keys()).copy()
    for i in temp_dict_keys:
        if not g.graph[i]:
            nodes, rows, cols = op(i.get_value(), i.blank_r, i.blank_c)
            g.append_children(i, nodes, rows, cols)
            if check(nodes, grid_sol):
                print_res(i)
                print(grid_sol)
                return depth
    return bfs(g, grid_sol, depth + 1)


def print_res(node):
    val = node.parent
    if val != 0:
        print_res(val)
        print(node.grid_value)
        print(' ' * 15, '^')
    else:
        print(node.grid_value)
        print(' ' * 15, '^')
        return


def check(val, grid_sol):
    for i in val:
        if i == grid_sol:
            return True
    return False


def op(node, row, col):
    nodes = [copy.deepcopy(node), copy.deepcopy(node), copy.deepcopy(node), copy.deepcopy(node)]
    rows = [row for _ in range(0, 4)]
    cols = [col for _ in range(0, 4)]
    assign_none = []
    # left
    if cols[0] != 0:
        nodes[0][rows[0]][cols[0]], nodes[0][rows[0]][cols[0] - 1] = nodes[0][rows[0]][cols[0] - 1], nodes[0][rows[0]][
            cols[0]]
        cols[0] = cols[0] - 1
    else:
        assign_none.append(0)
    #     right
    if cols[1] != 2:
        nodes[1][rows[1]][cols[1]], nodes[1][rows[1]][cols[1] + 1] = nodes[1][rows[1]][cols[1] + 1], nodes[1][rows[1]][
            cols[1]]
        cols[1] = cols[1] + 1
    else:
        assign_none.append(1)
    #     up
    if rows[2] != 0:
        nodes[2][rows[2]][cols[2]], nodes[2][rows[2] - 1][cols[2]] = nodes[2][rows[2] - 1][cols[2]], nodes[2][rows[2]][
            cols[2]]
        rows[2] = rows[2] - 1
    else:
        assign_none.append(2)
    #     down
    if rows[3] != 2:
        nodes[3][rows[3]][cols[3]], nodes[3][rows[3] + 1][cols[3]] = nodes[3][rows[3] + 1][cols[3]], nodes[3][rows[3]][
            cols[3]]
        rows[3] = rows[3] + 1
    else:
        assign_none.append(3)
    for i in assign_none:
        rows[i] = None
        cols[i] = None
        nodes[i] = None
    return nodes, rows, cols


if __name__ == '__main__':
    main()
