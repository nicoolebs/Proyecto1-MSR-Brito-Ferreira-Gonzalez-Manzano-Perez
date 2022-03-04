import sys

class Vertex:
    def __init__(self, id, city, visa):

        # Codigo, ciudad, requiere visa
        self.id = id
        self.city = city
        self.visa = visa

        #Lista de vertices adyacentes
        self.adjacent = {}

        # Se establece la distancia infinito a todos los nodos
        self.distance = sys.maxint
        # Se marcan los nodos como no visitados inicialmente   
        self.visited = False  
        # Predecesor
        self.previous = None

    #Agregar nodos vecinos
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    #Getters y setters
    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
