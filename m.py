class Queue:
    def __init__(self, memory):
        self.size = 0
        self.start = 0
        self.end = 0
        self.memory = memory
        self.values = [-1] * self.memory

    def push(self, value):
        if self.size == 0:
            self.values[self.end] = value
            self.size += 1
        else:
            self.end += 1
            if self.end == self.memory:
                self.end = 0
            self.values[self.end]
            self.size += 1

    def pop(self):
        self.size -= 1
        self.start += 1
        if self.end < self.start:
            self.end = self.start
        result = self.values[self.start - 1]
        self.values[self.start - 1] = -1
        return result

    def is_empty(self):
        return self.size == 0

class Graph:
    def __init__(self):
        self.is_oriented = True
        self.size = 0
        self.matrix = []

    def add_edge(self, start, end):
        if start > self.size or end > self.size:
            if start < end:
                new_size = end
            else:
                new_size = start
            for row in range(self.size, new_size):  # adding new rows
                self.matrix.append([0] * new_size)
            for row in range(0, self.size):  # adding new columns for old rows
                for column in range(self.size, new_size):
                    self.matrix[row].append(0)
            self.size = new_size
        self.matrix[start - 1][end - 1] = 1
    def print(self):
        for row in range(self.size):
            for column in range(self.size):
                print(self.matrix[row][column], end=" ")
            print()

    def BFS(self, start):
        current_vertex = start - 1
        queue_BFS = Queue(self.size)
        queue_BFS.push(start - 1)
        while (queue_BFS.is_empty() == False):
            current_vertex = queue_BFS.pop()
            print(current_vertex)
            visited_vertexes=[]
            for column in range(self.size):
                if self.matrix[current_vertex][column]==1:
                    is_vertex_visited = False
                    for check in visited_vertexes:
                        if current_vertex==check:
                            is_vertex_visited==True
                    if not is_vertex_visited:
                        queue_BFS.push(column)  # MAYBE get_value()-1 ????
                        visited_vertexes.append(column)


my_graph = Graph()
my_graph.add_edge(1, 3)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 5)
my_graph.add_edge(2, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(5, 4)
my_graph.print()
my_graph.BFS(1)
