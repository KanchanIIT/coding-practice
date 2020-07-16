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

        print (v)
        self.visited[v] = True

        for u in self.adj_list[v]:
            if not self.visited[u]:
                self.DFS_Util(u)


    def DFS(self, start_node):

        # following is for all the nodes
        # for node in range(self.V):
        #     if not self.visited[node]:
        #         self.DFS_Util(node)

        if not self.visited[start_node]:
            self.DFS_Util(start_node)



if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.DFS(2)
