import heapq

#Metodo para buscar el camino hasta un vertice
def shortest(v, path):

	#Si existe un predecesor para el vertice, se agrega al camino y se busca en el anterior su predecesor de forma recursiva hasta llegar al inicio del camino
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

#Metodo de Dijkstra para buscar el camino más barato
def dijkstra_min_cost(aGraph, start, target, visa):

	#Si el país destino requiere visa y la persona no tiene visa, no se puede buscar el camino más barato
	if target.visa == True and visa == False:

		print('Usted no tiene VISA para ingresar al país destino, por lo que no podemos ofrecerle la ruta deseada.')

	else:

		# La distancia al nodo de inicio es 0
		start.set_distance(0)

		#Si el país no requiere VISA y la persona no tiene VISA, no se puede hacer escala en los paises que neceseitan VISA
		if target.visa == False and visa == False:
			# Se crea una cola con todos los nodos no visitados, excluyendo los que necesitan visa
			unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visa]
		else:
			# Si la persona si tiene VISA, se crea una cola con todos los nodos no visitados, porque puede entrar a todos los paises
			unvisited_queue = [(v.get_distance(),v) for v in aGraph]
		
		heapq.heapify(unvisited_queue)

		#Se recorre la cola de no visitados
		while len(unvisited_queue):

			# Visite el nodo no visitado que tenga la menor distancia conocia dal nodo de inicio y lo marca como visitado
			uv = heapq.heappop(unvisited_queue)
			current = uv[1]
			current.set_visited()

			#Examina los nodos adyacentes
			for next in current.adjacent:

				# Si el nodo esta visitado, no se examina y regresa al bucle
				if next.visited:
					continue

				#Si el nodo no está visitado, se calcula la distancia de sus vecinos
				new_dist = current.get_distance() + current.get_weight(next)
				
				#Si la distancia calculada para un vecino es menor que la que tenia asignada, se actualiza la distancia minima y el predecesor
				if new_dist < next.get_distance():
					next.set_distance(new_dist)
					next.set_previous(current)

			# Reconstruir la cola con los vertices no visitados

			# 1. Se vacia la cola
			while len(unvisited_queue):
				heapq.heappop(unvisited_queue)
			# 2. Llenar la cola con los no visitados
			if target.visa == False and visa == False:
				# Se crea una cola con todos los nodos no visitados, excluyendo los que necesitan visa
				unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited and not v.visa]
			else:
				# Si la persona si tiene VISA, se crea una cola con todos los nodos no visitados, porque puede entrar a todos los paises
				unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
			
			heapq.heapify(unvisited_queue)
		
#Metodo de Dijkstra para buscar el camino con menor cantidad de vuelos
def dijkstra_min_steps(aGraph, start, target, visa):

	#Si el país destino requiere visa y la persona no tiene visa, no se puede buscar el camino más barato
	if target.visa == True and visa == False:

		print('Usted no tiene VISA para ingresar al país destino, por lo que no podemos ofrecerle la ruta deseada.')

	else:

		# La distancia al nodo de inicio es 0
		start.set_distance(0)

		#Si el país no requiere VISA y la persona no tiene VISA, no se puede hacer escala en los paises que neceseitan VISA
		if target.visa == False and visa == False:
			# Se crea una cola con todos los nodos no visitados, excluyendo los que necesitan visa
			unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visa]
		else:
			# Si la persona si tiene VISA, se crea una cola con todos los nodos no visitados, porque puede entrar a todos los paises
			unvisited_queue = [(v.get_distance(),v) for v in aGraph]
		
		heapq.heapify(unvisited_queue)

		#Se recorre la cola de no visitados
		while len(unvisited_queue):

			# Visite el nodo no visitado que tenga la menor distancia conocia dal nodo de inicio y lo marca como visitado
			uv = heapq.heappop(unvisited_queue)
			current = uv[1]
			current.set_visited()

			#Examina los nodos adyacentes
			for next in current.adjacent:

				# Si el nodo esta visitado, no se examina y regresa al bucle
				if next.visited:
					continue

				#Si el nodo no está visitado, se calcula la distancia de sus vecinos
				new_dist = current.get_distance() + 1
				
				#Si la distancia calculada para un vecino es menor que la que tenia asignada, se actualiza la distancia minima y el predecesor
				if new_dist < next.get_distance():
					next.set_distance(new_dist)
					next.set_previous(current)

			# Reconstruir la cola con los vertices no visitados
			
			# 1. Se vacia la cola
			while len(unvisited_queue):
				heapq.heappop(unvisited_queue)
			# 2. Llenar la cola con los no visitados
			if target.visa == False and visa == False:
				# Se crea una cola con todos los nodos no visitados, excluyendo los que necesitan visa
				unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited and not v.visa]
			else:
				# Si la persona si tiene VISA, se crea una cola con todos los nodos no visitados, porque puede entrar a todos los paises
				unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
			
			heapq.heapify(unvisited_queue)