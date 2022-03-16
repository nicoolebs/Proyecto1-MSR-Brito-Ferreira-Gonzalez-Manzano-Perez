#Importaciones respectivas
from graph import *


#Función para crear el Grafo
def createGraph():

    #Creación del Grafo "g"
    g = Graph()

    #Vertices de las ciudades del proyecto con sus respectivos códigos, nombres y si necesitan o no visa para entrar
    g.add_vertex('CCS', 'Caracas', False)
    g.add_vertex('AUA', 'Aruba', True)
    g.add_vertex('BON', 'Bonaire', True)
    g.add_vertex('CUR', 'Curazao', True)
    g.add_vertex('SXM', 'San Martín', True)
    g.add_vertex('SDQ', 'Santo Domingo', True)
    g.add_vertex('SBH', 'San Bartolomé', False)
    g.add_vertex('POS', 'Puerto España - Trinidad', False)
    g.add_vertex('BGI', 'Barbados', False)
    g.add_vertex('FDF', 'Fort de France - Martinica', False)
    g.add_vertex('PTP', 'Point a Pitre - Guadalupe', False)

    #Aristas entre las ciudades del proyecto con sus respectivos costos
    g.add_edge('CCS', 'AUA', 40)
    g.add_edge('CCS', 'CUR', 35)
    g.add_edge('CCS', 'BON', 60)
    g.add_edge('AUA', 'CUR', 15)
    g.add_edge('AUA', 'BON', 15)
    g.add_edge('CUR', 'BON', 15)
    g.add_edge('CCS', 'SDQ', 180)
    g.add_edge('SDQ', 'SXM', 50)
    g.add_edge('SXM', 'SBH', 45)
    g.add_edge('CCS', 'POS', 150)
    g.add_edge('CCS', 'BGI', 180)
    g.add_edge('POS', 'BGI', 35)
    g.add_edge('POS', 'SXM', 90)
    g.add_edge('BGI', 'SXM', 70)
    g.add_edge('POS', 'PTP', 80)
    g.add_edge('POS', 'FDF', 75)
    g.add_edge('PTP', 'SXM', 100)
    g.add_edge('PTP', 'SBH', 80)
    g.add_edge('CUR', 'SXM', 80)
    g.add_edge('AUA', 'SXM', 85)

    #Retornando el Grafo
    return g