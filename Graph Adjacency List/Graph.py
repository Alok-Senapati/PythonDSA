from queue import SimpleQueue

class Graph:
    def __init__(self, no_of_vertices):
        self.__graph = [[] for i in range(no_of_vertices)]
        self.__no_of_vertices = no_of_vertices
        self.__no_of_edges = 0
    
    def add_edge(self, u, v):
        self.__graph[u].append(v)
        self.__graph[v].append(u)
        self.__no_of_edges += 1
        
    def __str__(self):
        output = ''
        for i in range(len(self.__graph)):
            output += str(i) + ' --> ' + ','.join(map(str, self.__graph[i])) + '\n'
        return output

    def get_no_of_vertices(self):
        return self.__no_of_vertices
    
    def get_no_of_edges(self):
        return self.__no_of_edges
    
    def is_edge(self, u, v):
        return v in self.__graph[u]
    
    def get_adjacent(self, u):
        return self.__graph[u]
    
    def remove_edge(self, u, v):
        self.__graph[u].remove(v)
        self.__graph[v].remove(u)

    def bfs(self, s):
        visited = [False] * len(self.__graph)

        q = SimpleQueue()
        visited[s] = True
        q.put(s)

        while not q.empty():
            front = q.get()
            print(front, end=" ")

            for node in self.get_adjacent(front):
                if not visited[node]:
                    visited[node] = True
                    q.put(node)

    def __dfc_rec(self, s, visited):
        visited[s] = True
        print(s, end=" ")
        for v in self.__graph[s]:
            if not visited[v]:
                self.__dfc_rec(v, visited)

    def dfs(self, s):
        visited = [False] * len(self.__graph)
        self.__dfc_rec(s, visited)


if __name__ == '__main__':
    graph = Graph(8)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 5)
    graph.add_edge(4, 6)
    graph.add_edge(3, 7)
    graph.add_edge(2, 6)
    print(graph)
    print(graph.is_edge(2, 3))
    graph.bfs(0)
    print()
    graph.dfs(0)
