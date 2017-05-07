class Graph:
    def __init__(self):
        self.vertices = {}
        self.distance = {}
        self.partitions = []

    def add_edge(self, key, definition):
        if key in self.vertices:
            self.vertices[key].append(definition)
        else:
            self.vertices[key] = [definition]
            self.distance[key] = None

    def reset_distance(self):
        for n in self.vertices:
            self.distance[n] = None



