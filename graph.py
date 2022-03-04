from node import *

class Graph:

    def __init__(self):
        #Lista de vertices del grafo
        self.vert_dict = {}

    #si no explota se quita
    def __iter__(self):
        return iter(self.vert_dict.values())

    #Metodo para agregar un vertice al grafo
    def add_vertex(self, node):

        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    #Metodo para obtener un vertice del grafo
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    #Metodo para agrerar una arista al grafo
    def add_edge(self, frm, to, cost = 0):

        #Se asignan ambos vertices como vecinos y se colocan los costos de ida y vuelta
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    #Getter
    def get_vertices(self):
        return self.vert_dict.keys()

