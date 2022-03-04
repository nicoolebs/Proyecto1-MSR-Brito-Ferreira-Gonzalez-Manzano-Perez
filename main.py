from dijkstra import *
from graph import *
from node import *
from data import *

if __name__ == '__main__':

    #Crear el grafo
    g = createGraph()

    frm = input('Ingrese el código del aeropuerto de origen: ')
    to = input('Ingrese el código del aeropuerto de destino: ')
    visa = input('¿Posee VISA? \n1. SI \n2. NO \n\n')
    route = input('¿Qué criterio desea considerar a la hora del viaje? \n1. Costo mínimo \2. Número de vuelos mínimo \n\n')

    if route == 1:
        dijkstra_min_cost(g, g.get_vertex(frm), g.get_vertex(to), visa) 
    else:
        dijkstra_min_steps(g, g.get_vertex(frm), g.get_vertex(to), visa) 

    #Reconstruir el camino
    target = g.get_vertex(to)
    path = [target.get_id()]
    shortest(target, path)

    if route == 1:
        print ('El costo mínimo de ' + frm + ' a ' + to + ' es de ' + target.get_distance()))
        print ('El camino a tomar será ' %(path[::-1]))
    else:
        print ('El número mínimo de vuelos de ' + frm + ' a ' + to + ' es de ' + target.get_distance()))
        print ('El camino a tomar será ' %(path[::-1]))
