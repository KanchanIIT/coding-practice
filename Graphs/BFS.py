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

    def BFS(self, start_node):

        queue = list()  # queue can be taken as list. the list.pop(0) will remove and return the 0th elements
        queue.append(start_node)
        self.visited[start_node] = True

        while queue: # return false when the list is empty
            v = queue.pop(0)  # the pop operation will remove and return the specified index in python
            print(v)
            for u in self.adj_list[v]:
                if not self.visited[u]:
                    queue.append(u)
                    self.visited[u] = True


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.BFS(2)
