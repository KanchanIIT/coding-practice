"""

1. add opposite color of parent node, to each of the vertex while traversing.
2. and check for all connected node does anyone have same color
    1. if any connected vertex has same color return False
    2. else continue
3. return true

"""

########## NEED TO CHECK THE CODE FOR CORRECTNESS ############

# simply use dictionary for adj list

class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.adj_list = dict()
        self.adj_list = {i: list() for i in range(self.V)}
        self.visited = [False] * self.V

        # initialise with invalid color -1. use color 1 and 0
        self.color = [-1] * self.V

    def addEdge(self, src, dest):
        # directed graph
        self.adj_list[src].append(dest)
        # for indirected graph add the opposite
        # self.adj_list[dest].append(src)

    # recursive solution without stack
    def DFS_Util(self, v):

        print("parent node:", v)
        self.visited[v] = True
        for u in self.adj_list[v]:
            print("child node:", u)
            # if any other connected node has same color
            if self.color[u] == self.color[v]:
                return False
            if not self.visited[u]:
                # assign the opposite color of the parents
                self.color[u] = 1 - self.color[v]
                self.DFS_Util(u)

    def bipartiteDetection(self):
        # following is for all the nodes
        for node in range(self.V):
            if not self.visited[node]:
                # initialize the first node color as 1
                self.color[node] = 1
                if not self.DFS_Util(node):
                    return False
        return True


if __name__ == "__main__":
    # g = Graph(4)
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)
    #
    # print (g.bipartiteDetection()) # not bipartite

    g = Graph(5)
    g.addEdge(0, 3)
    g.addEdge(0, 4)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(2, 4)

    print(g.bipartiteDetection())  # bipartite
