# simply use dictionary for adj list

class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.adj_list = dict()
        self.adj_list = {i: list() for i in range(self.V)}
        self.visited = [False] * self.V

    def addEdge(self, src, dest):
        # directed graph
        self.adj_list[src].append(dest)
        # for indirected graph add the opposite
        # self.adj_list[dest].append(src)

    ## recursive solution without stack
    def DFS_Util(self, v):

        self.visited[v] = True

        for u in self.adj_list[v]:
            if self.visited[u]:
                return True
            else:
                self.DFS_Util(u)

    def detectCycle(self):

        # following is for all the nodes
        for node in range(self.V):
            if not self.visited[node]:
                if self.DFS_Util(node):
                    return True
        return False


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print(g.detectCycle())  # has cycle

    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(2, 3)
    print(g.detectCycle())  # has no cycle
