#Importaciones respectivas
import heapq


#Método sort para los nodos
def sort_nodes(node):
  return node[0]


#Método para buscar el camino hasta un vertice
def shortest(v, path, costo):

	#Si existe un predecesor para el vertice
    if v.previous:
		#Se agrega al camino que se está formando este vértice
        path.append(v.previous.get_id())
		#Se agrega el costo del mismo
        costo.append(v.get_weight(v.previous))
		#Se busca en el anterior su predecesor de forma recursiva hasta llegar al inicio del camino indicado
        shortest(v.previous, path, costo)
	#Retorna el camino deseado
    return


#Método de Dijkstra para buscar el camino más barato entre los vértices/ciudades indicadas
def dijkstra_min_cost(aGraph, start, target, visa):

	#Si la ciudad destino requiere visa y la persona no tiene visa, no se puede buscar el camino más barato. Por ello se imprime el mensaje
	if target.visa == True and visa == False:
		#Mensaje para los que no tienen visa y la ciudad la pide para ingresar
		print('Lo sentimos, usted no tiene VISA para ingresar a la ciudad de destino deseada.\n Por ello no podemos ofrecerle la ruta indicada.')
	
	#En otro caso
	else:
		#Se hace que la distancia al nodo de inicio, o sea a la ciudad de donde se parte, sea 0
		start.set_distance(0)

		#Si la ciudad no requiere VISA y la persona no tiene VISA, se sabe que no se puede hacer escala en las ciudades que necesiten el documento -VISA-
		if target.visa == False and visa == False:
			#Se crea una cola con todos los nodos no visitados, excluyendo los que necesitan visa para ser visitados
			unvisited_queue = [(v.get_distance(),v) for v in aGraph if (not v.visa) or (v.id == start.id)]
		#Si la persona tiene VISA
		else:
			#Si la persona tiene VISA, se crea una cola con todos los nodos no visitados, ya que puede entrar a todas las ciudades del grafo
			unvisited_queue = [(v.get_distance(),v) for v in aGraph]
		
		unvisited_queue.sort(key=sort_nodes)
		unvisited_queue_list = list(unvisited_queue)

		#Se recorre la cola de no visitados
		while len(unvisited_queue_list):

			#Se Visita el nodo no visitado que tenga la menor distancia conocia al nodo de inicio y lo marca como visitado
			uv = unvisited_queue_list.pop(0)
			current = uv[1]
			current.set_visited()

			#Se examina los nodos adyacentes
			for next in current.adjacent:

				#Si el nodo esta visitado, no se examina y se regresa al bucle
				if next.visited:
					continue

				#Si el nodo no está visitado, se calcula la distancia de sus vecinos
				new_dist = current.get_distance() + current.get_weight(next)
				
				#Si la distancia calculada para un vecino es menor que la que tenía asignada, se actualiza la distancia mínima y el predecesor correspondiente
				if new_dist < next.get_distance():
					#Distancia
					next.set_distance(new_dist)
					#Predecesor
					next.set_previous(current)

			#Luego se va a reconstruir la cola con los vertices no visitados, para ello

			#Se vacía la cola que se tiene
			unvisited_queue = []

			#Se llena la cola con los no visitados

			#Si la ciudad no requiere VISA y la persona no tiene VISA, se sabe que no se puede hacer escala en las ciudades que necesiten el documento -VISA-
			if target.visa == False and visa == False:
				#Se crea una cola con todos los nodos no visitados, excluyendo los que necesitan visa
				unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited and not v.visa]
			#Si la persona tiene VISA
			else:
				#Si la persona si tiene VISA, se crea una cola con todos los nodos no visitados, porque puede entrar a todas las ciudades
				unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
			
			unvisited_queue.sort(key=sort_nodes)
			unvisited_queue_list = list(unvisited_queue)
		

#Método de Dijkstra para buscar el camino con menor cantidad de vuelos entre la ciudad de partida y de llegada
def dijkstra_min_steps(aGraph, start, target, visa):

	#Si la ciudad de destino requiere visa y la persona no tiene visa, no se puede buscar el camino con la menor cantidad de vuelos. Por ello se imprime mensaje
	if target.visa == True and visa == False:
		#Mensaje al no tener visa y querer ir a una ciudad -destino- que requiere el documento
		print('Lo sentimos, usted no tiene VISA para ingresar a la ciudad de destino deseada.\n Por ello no podemos ofrecerle la ruta indicada.')
	
	#En otro caso
	else:
		#Se hace que la distancia al nodo de inicio, o sea a la ciudad de donde se parte, sea 0
		start.set_distance(0)

		#Si la ciudad no requiere VISA y la persona no tiene VISA, no se puede hacer escala en las ciudades que necesiten el documento -VISA-
		if target.visa == False and visa == False:
			# Se crea una cola con todos los nodos no visitados, excluyendo los que necesitan visa
			unvisited_queue = [(v.get_distance(),v) for v in aGraph if (not v.visa) or (v.id == start.id)]
		#Si la persona tiene VISA
		else:
			#Si la persona si tiene VISA, se crea una cola con todos los nodos no visitados, porque puede entrar a todas las ciudades
			unvisited_queue = [(v.get_distance(),v) for v in aGraph]
		
		unvisited_queue.sort(key=sort_nodes)
		unvisited_queue_list = list(unvisited_queue)

		#Se recorre la cola de no visitados
		while len(unvisited_queue_list):

			#Se Visita el nodo no visitado que tenga la menor distancia conocia dal nodo de inicio y lo marca como visitado
			uv = unvisited_queue_list.pop(0)
			current = uv[1]
			current.set_visited()

			#Se examina los nodos adyacentes
			for next in current.adjacent:

				#Si el nodo esta visitado, no se examina y se regresa al bucle
				if next.visited:
					continue

				#Si el nodo no está visitado, se calcula la distancia de sus vecinos. En este caso sería un viaje de un nodo a otro
				new_dist = current.get_distance() + 1
				
				#Si la distancia calculada para un vecino es menor que la que se tenía asignada, se actualiza la distancia mínima y el predecesor
				if new_dist < next.get_distance():
					#Distancia
					next.set_distance(new_dist)
					#Predecesor
					next.set_previous(current)

			#Luego se va a reconstruir la cola con los vertices no visitados. Para ello
			
			#Se vacía la cola
			unvisited_queue = []
			
			#Se llena la cola con los no visitados

			#Si la ciudad no requiere VISA y la persona no tiene VISA, se sabe que no se puede hacer escala en las ciudades que necesiten el documento -VISA-
			if target.visa == False and visa == False:
				#Se crea una cola con todos los nodos no visitados, excluyendo los que necesitan visa
				unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited and not v.visa]
			
			#Si la persona tiene VISA
			else:
				#Si la persona si tiene VISA, se crea una cola con todos los nodos no visitados, porque puede entrar a todas las ciudades
				unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
			
			unvisited_queue.sort(key=sort_nodes)
			unvisited_queue_list = list(unvisited_queue)