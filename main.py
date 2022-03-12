#Importaciones respectivas
from dijkstra import *
from graph import *
from node import *
from data import *

if __name__ == '__main__':

    #Se crea el grafo g
    g = createGraph()

    #Inicio del proyecto

    #Bienvenida
    print ('------------------------------------------------------------------------------------')
    print ('|                 ¡Bienvenido a la Agencia de Viajes Metro Travel!                 |')
    print ('|                                                                                  |')
    print ('|                 En Metro Travel nos especializamos en viajes desde               |')
    print ('|           el Aeropuerto de Maiquetía hacia diversas Islas del Mar Caribe         |')
    print ('------------------------------------------------------------------------------------')

    #Separador en la consola
    print ('\n')
 
    #Destinos en la consola
    print ('----------------------------------------------------------------------------------')
    print ('|                         Los destinos que ofrecemos son:                        |')
    print ('|                                                                                |')
    print ('|  Caracas                   Código del Aeropuerto: CCS      No requiere VISA    |')
    print ('|  Aruba                     Código del Aeropuerto: AUA      Requiere VISA       |')
    print ('|  Bonaire                   Código del Aeropuerto: BON      Requiere VISA       |')
    print ('|  Curazao                   Código del Aeropuerto: CUR      Requiere VISA       |')
    print ('|  San Martín                Código del Aeropuerto: SXM      Requiere VISA       |')
    print ('|  Santo Domingo             Código del Aeropuerto: SDQ      Requiere VISA       |')
    print ('|  San Bartolomé             Código del Aeropuerto: SBH      No requiere VISA    |')
    print ('|  Puerto España-Trinidad    Código del Aeropuerto: POS      No requiere VISA    |')
    print ('|  Barbados                  Código del Aeropuerto: BGI      No requiere VISA    |')
    print ('|  Fort de France-Martinica  Código del Aeropuerto: FDF      No requiere VISA    |')
    print ('|  Point a Pitre-Guadalupe   Código del Aeropuerto: PTP      No requiere VISA    |')
    print ('|                                                                                |')
    print ('----------------------------------------------------------------------------------')
    
    #Separador en la consola
    print ('\n')

    #Pidiendo datos necesarios por consola al usuario

    #frm: ciudad de origen
    frm = input('Por favor, ingrese el código del aeropuerto de la ciudad de origen: ')
    print ('\n')

    #to: ciudad de destino
    to = input('Por favor, ingrese el código del aeropuerto de la ciudad de destino: ')
    print ('\n')

    #visa: posee o no vida el usuario
    visa = int(input('¿Posee usted VISA? \n1. SI \n2. NO \nIngrese en número correspondiente: '))
    print ('\n')

    #Guardando si el usuario Tiene o No tiene visa
    if visa == 1:
        visa = True
    else:
        visa = False
    
    #Criterio a tomar en cuenta para correr los métodos
    route = input('¿Qué criterio desea considerar a la hora del viaje? \n1. Costo mínimo \n2. Número de vuelos mínimo \nIngrese en número correspondiente: ')
    print ('\n')

    #Si el usuario elige como criterio el costo mínimo 
    if route == '1':
        #Se ejecuta el método correspondiente
        dijkstra_min_cost(g, g.get_vertex(frm), g.get_vertex(to), visa) 
    #Sino, si el usuario elige como criterio el número de vuelos mínimo
    else:
        #Se ejecuta el método correspondiente
        dijkstra_min_steps(g, g.get_vertex(frm), g.get_vertex(to), visa) 

    #Reconstruir el camino obtenido por el método correspondiente 
    target = g.get_vertex(to)
    path = [target.get_id()]
    costo = []
    shortest(target, path, costo)
    path.reverse()

    #Mensaje de resultado para el usuario
    
    #Si el usuario elige como criterio el costo mínimo, el mensaje es 
    if target.get_distance() == 99999999999:
        print ('')
    elif route == '1':
        print ('El costo mínimo de ' + frm + ' a ' + to + ' es de: $' + str(target.get_distance()))
        print ('En este, el camino a tomar será: ')
        for x in range(len(path)):
            print(str(path[x]))
    
    #Si el usuario elige como criterio el número de vuelos mínimo
    else:
        print ('El número mínimo de vuelos de ' + frm + ' a ' + to + ' es de ' + str(target.get_distance())+ ' vuelo-s-')
        print ('Para este caso el costo de ' + frm + ' a ' + to + ' es de: $' + str(sum(costo)))
        print ('En este, el camino a tomar será: ')
        for x in range(len(path)):
            print(str(path[x]))

#OJOO !!!!!!!! OJOJOJOOOJ
#Verificar que el destino no sea igual al origen, que no metan num donde van letras
#y vice, que el codigo de la ciudad que metan existe
#No se que mas
#Revisar si se lanzan mensajes de errores correspondientes
#revisar que los emnsajes finales de la corrida del programa digan errores de no vida etc tec etc