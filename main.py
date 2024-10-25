class Pair:
    def __init__(self, vertex_num):
        self.is_visited = False
        self.vertex_num = vertex_num
    def get_value(self):
        return self.vertex_num


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
            for row in range(self.size, new_size): #adding new rows
                self.matrix.append([Pair(0)]*new_size)
            for row in range(0, self.size): #adding new columns for old rows
                for column in range(self.size, new_size):
                    self.matrix[row].append(Pair(0))
            self.size = new_size
        self.matrix[start-1][end-1] = Pair(1)

    def print(self):
        for row in range(self.size):
            for column in range(self.size):
                print(self.matrix[row][column].get_value(), end=" ")
            print()

    def BFS(self):
        

my_graph = Graph()
my_graph.add_edge(1, 3)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 5)
my_graph.add_edge(2, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(5, 4)
my_graph.print()
