class Graph:
    def __init__(self, i: int = 0, j: int = 0, count_nodes: int = 0, count_edges: int = 0, adj_list=None) -> None:
        if adj_list is None:
            adj_list = {}
        self.count_nodes = count_nodes
        self.count_edges = count_edges
        self.adj_list = adj_list
        self.i = i
        self.j = j

        if not adj_list:
            for i in range(self.i):
                for j in range(self.j):
                    adj_list[i, j] = []

    def add_directed_edge(self, a: tuple, arg2: tuple):
        self.adj_list[a].append(arg2)
        self.count_edges += 1

    def depth_search(self, start: tuple, end: tuple):
        desc = {}
        for i in self.adj_list:
            desc[i] = 0
        S = [start]
        R = [start]
        desc[start] = 1
        while len(S) != 0:
            u = S[-1]
            desempilhar = True
            for v in self.adj_list[u]:
                if v == end:
                    R.append(v)
                    return R
                if desc[v] == 0:
                    desempilhar = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
                    break
            if desempilhar:
                S.pop()
                R.pop()
        return R
