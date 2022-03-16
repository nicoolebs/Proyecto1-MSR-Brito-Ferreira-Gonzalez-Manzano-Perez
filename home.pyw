#Importaciones respectivas
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from dijkstra import *
from graph import *
from node import *
from data import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
import matplotlib as mpl


#Configuración de la interfaz gráfica

#Creación de la ventana
home = Tk()

#Título de la ventana
home.title("Metro Travel")

#Ícono de la ventana
home.iconbitmap("imagenes/Logo 2.ico")
home.iconphoto(False, tk.PhotoImage(file='imagenes/Logo 2.png'))

#Para que la ventana no sea redimensionable
home.resizable(0, 0)

#Configuración del frame que va a contener todos los widgets que se van a mostar en la interfaz gráfica
homeFrame = Frame()
homeFrame.pack()
homeFrame.config(bg="#f0ebe7")
homeFrame.config(width="1300", height="700")

#Configuración de la imagen/logo que sale en la ventana
logoImg = Image.open("imagenes/Logo 2.png")
ajusteLogo = logoImg.resize((130, 130))
logoAjustado = ImageTk.PhotoImage(ajusteLogo)


#Etiquetas que se muestran en pantalla con mensajes de Bienvenida
Label(homeFrame, text="¡Bienvenido a la Agencia de Viajes Metro Travel!", fg="#000000", font=("Poppins", 18, "bold"), bg="#f0ebe7").place(x="600", y="50", anchor="center")
Label(homeFrame, image=logoAjustado, bg="#f0ebe7").place(x="50", y="15")
Label(homeFrame, text="En Metro Travel nos especializamos en viajes desde "
                      "el Aeropuerto de Maiquetía hacia diversas Islas del Mar Caribe", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7")\
                    .place(x="600", y="115", anchor="center")


#Etiqueta e imagen que muestran los destinos de la agencia
Label(homeFrame, text="Destinos que ofrecemos:", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="150", y="170", anchor="center")
#Configuración de imagen de destinos
destinosImg = Image.open("imagenes/Destinos del Proyecto.png")
ajusteDesti = destinosImg.resize((550, 190))
destAjustado = ImageTk.PhotoImage(ajusteDesti)
Label(homeFrame, image=destAjustado, bg="#f0ebe7").place(x="290", y="280",anchor='center')


#Comboboxes para que el usuario seleccione la ciudad de origen y destino deseadas 

#Ciudades disponibles de la agencia con su nombre y código
ciudades = ['Caracas - CCS', 'Aruba - AUA', 'Bonaire - BON', 'Curazao - CUR', 'San Martín - SXM', 'Santo Domingo - SDQ', 'San Bartolomé - SBH','Puerto España - POS','Barbados - BGI','Fort de France - FDF','Point a Pitre - PTP']

#Etiqueta y Combobox para identificar y seleccionar la ciudad de origen
Label(homeFrame, text="Por favor, seleccione el código de la ciudad de origen:", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="385")
codigoOrigen = ciudades[0][-3:]

#Etiqueta y Combobox para identificar y seleccionar la ciudad de destino
Label(homeFrame, text="Por favor, seleccione el código de la ciudad de destino:", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="425")
codigoDestino = ciudades[1][-3:] 

#Método que guarda el código de la ciudad de origen
def asignaCodigoOrigen():
    codigo = str(seleccionadoOrigen.get())
    codigoOrigen = codigo[-3:]
    return codigoOrigen

#Método que guarda el código de la ciudad de destino
def asignaCodigoDestino():
    codigo = str(seleccionadoDestino.get())
    codigoDestino = codigo[-3:]
    return codigoDestino

seleccionadoOrigen = StringVar(homeFrame)
seleccionadoOrigen.set(ciudades[0])
ciudadOrigen_menu = OptionMenu(homeFrame, seleccionadoOrigen, *ciudades)
ciudadOrigen_menu.pack()

seleccionadoDestino = StringVar()
seleccionadoDestino.set(ciudades[1])
ciudadDestino_menu = OptionMenu(home, seleccionadoDestino, *ciudades)
ciudadDestino_menu.pack()

#Ubicando los comboboxes en la interfaz
ciudadOrigen_menu.place(x="490", y="385")
ciudadDestino_menu.place(x="490", y="425")


#Apartado para que el usuario seleccione si TIENE o NO el documento visa

#Etiqueta señalando que indique si tiene o no el documento
Label(homeFrame, text="¿Posee usted VISA?", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="460")

#Inicialización del btn en tiene visa
visaSelected = True

def toggleVisa():
    if seleccionadoVisa.get() == "Si":
        return True
    else:
        return False

#Opciones para el usuario -tiene o no tiene visa-
opcionesVisas = ["Si", "No"]

seleccionadoVisa = StringVar()
seleccionadoVisa.set(opcionesVisas[0])
seleccionadoVisa_menu = OptionMenu(home, seleccionadoVisa, *opcionesVisas)
seleccionadoVisa_menu.pack()

#Ubicación del Btn con la opción de seleccionar si tiene o no visa
seleccionadoVisa_menu.place(x="490", y="460")


#Apartado para que el usuario seleccione si quiere cumplir su viaje con el criterio de Costo Mínimo o el criterio de Vuelos Mínimos

#Etiqueta señalando que indique si tiene o no el documento
Label(homeFrame, text="¿Qué criterio desea considerar a la hora del viaje?", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="490")

#Inicialización del btn en criteri costo mínimo
criterio = 'Costo mínimo'

def toggleCriterio():
    criterio = seleccionadoCriterio.get()
    return criterio

#Opciones para el usuario -quiere viajar con costo mínimo o vuelos mínimos-  
opcionesCriterio = ['Costo mínimo', 'Vuelos mínimos']

seleccionadoCriterio = StringVar()
seleccionadoCriterio.set(opcionesCriterio[0])
seleccionadoCriterio_menu = OptionMenu(home, seleccionadoCriterio, *opcionesCriterio)
seleccionadoCriterio_menu.pack()

#Ubicación del Btn con la opción del criterio
seleccionadoCriterio_menu.place(x="490", y="490")


#Dibujando el Grafo Inicial completo sin los vuelos deseados por el usuario a realizar

#Creación del grafo a dibujar
grafoDibujo = nx.Graph()
grafoDatos = createGraph()

#Arcos del grafo a dibujar -no dirigido-
arcosGrafoDibujo = [
('CCS', 'AUA'),
('CCS', 'CUR'),
('CCS', 'BON'),
('AUA', 'CUR'),
('AUA', 'BON'),
('CUR', 'BON'),
('CCS', 'SDQ'),
('SDQ', 'SXM'),
('SXM', 'SBH'),
('CCS', 'POS'),
('CCS', 'BGI'),
('POS', 'BGI'),
('POS', 'SXM'),
('BGI', 'SXM'),
('POS', 'PTP'),
('POS', 'FDF'),
('PTP', 'SXM'),
('PTP', 'SBH'),
('CUR', 'SXM'),
('AUA', 'SXM')
]

#Configuración de la figura a generar
figure= plt.figure(figsize=(4, 4), dpi=100)
plt.axis('off')
subplot= figure.add_subplot(111)

#Agregando al grafo a dibujar las aristas
grafoDibujo.add_edges_from(arcosGrafoDibujo)

#Dibujando el grafo con sus respectivas configuraciones de tamaño, color, etc
pos = nx.spring_layout(grafoDibujo)
nx.draw_networkx_nodes(grafoDibujo, pos, node_size=100, node_color='#8EB2D5')
nx.draw_networkx_edges(grafoDibujo, pos, edgelist=grafoDibujo.edges(), width=0.5, edge_color='black', arrows="-")
labels_params = {"font_size": 10}
nx.draw_networkx_labels(grafoDibujo, pos, **labels_params)
canvas = FigureCanvasTkAgg(figure,master=home)
canvas.draw()

#Colocando el dibujo en la ventana de Tkinter
canvas.get_tk_widget().pack()
toolbar = NavigationToolbar2Tk(canvas, home)
toolbar.update()
canvas.get_tk_widget().place(x="790", y="150")


#Función que hace que se vuelva a pintar el grafo si se selecciona un vuelo a realizar
def pintarGrafo(path):
    #Colores para nodos
    colors=[]
    #Lista de Ciudades con las que se trabaja
    listaCiudades = ["CCS", "AUA", "CUR", "BON", "SDQ", "SXM", "SBH", "POS", "BGI", "PTP", "FDF"]

    #Bandera
    found = False

    #Fores que permiten establecer los colores de los nodos si fueron seleccionados como parte del viaje del usuario
    for ciudad in listaCiudades:
        for ciudad_path in path:
            #Si la ciudad se visita para realizar el viaje se pinta de color rojo el nodo
            if ciudad == ciudad_path:
                colors.append('#D33457')
                found = True
                continue
        if found:
            found = False
            continue
        #Si no es asi, se deja del color inicial
        else:
            colors.append('#8EB2D5')

    #Lista de los arcos entre ciudades que se maneja
    arcos = [('CCS', 'AUA'), ('CCS', 'CUR'), ('CCS', 'BON'), ('CCS', 'SDQ'), ('CCS', 'POS'), ('CCS', 'BGI'), ('AUA', 'CUR'), ('AUA', 'BON'), ('AUA', 'SXM'), ('CUR', 'BON'), ('CUR', 'SXM'), ('SDQ', 'SXM'), ('SXM', 'SBH'), ('SXM', 'POS'), ('SXM', 'BGI'), ('SXM', 'PTP'), ('SBH', 'PTP'), ('POS', 'BGI'), ('POS', 'PTP'), ('POS', 'FDF')]
    #Colores para nodos
    colors_e = []
    
    #Segunda Bandera
    found_e = False

    #Fores que permiten establecer los colores de los arcos si son parte del viaje del usuario
    for x in range(len(arcos)):
        for y in range(len(path) - 1):
            #Si ese arco se utiliza para llegar el destino deseado se pinta de rojo
            if arcos[x] == (path[y], path[y + 1]) or arcos[x] == (path[y + 1], path[y]):
                colors_e.append('#D33457')
                found_e = True
                continue
        if found_e:
            found_e = False
            continue
        #Si no es asi, se deja del color inicial
        else:
            colors_e.append('black')
            
    #Dibujando el grafo con sus respectivas configuraciones de tamaño, color, etc
    nx.draw_networkx_nodes(grafoDibujo, pos, node_color=colors, node_size=100)
    nx.draw_networkx_edges(grafoDibujo, pos, edgelist=grafoDibujo.edges(), width=0.9, edge_color=colors_e, arrows="-")
    labels_params = {"font_size": 10}
    nx.draw_networkx_labels(grafoDibujo, pos, **labels_params)

    canvas = FigureCanvasTkAgg(figure, master=home)
    canvas.draw()

    #Colocando el dibujo en la ventana de Tkinter
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, home)
    toolbar.update()
    canvas.get_tk_widget().place(x="790", y="150")

#Declaración de labels que cambiarán dependiendo del resultado generado por el usuario
#Label que indica el camino/vuelos/escalas
label_camino = tk.Label(homeFrame, fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7")
label_camino.place(x="15", y="600")
#Label que indica el costo, número min de vuelos, etc
label_respuesta = tk.Label(homeFrame, fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7")
label_respuesta.place(x="15", y="620")

#Método que permite ejecutar Dijkstra y mostrar los resultados en la interfaz
def ejecutarDijkstra():

    #Guardando el origen, destino, el criterio y si se posee o no la visa
    frm = asignaCodigoOrigen()
    to = asignaCodigoDestino()
    route = toggleCriterio()
    visa = toggleVisa()
    #Variables que permiten modificar los labels de respuesta
    respuesta = ''
    camino = ''
    global label_camino
    global label_respuesta
    #Se crea el grafo
    g = createGraph()

    #Si el destino es igual al origen se genera el mensaje
    if frm == to:
        #Se muestra en interfaz el mensaje
        respuesta = 'La ciudad de origen no puede ser igual a la ciudad de destino. Por favor, ingrese nuevamente su viaje.'

    #Si el usuario no tiene visa y su ciudad de destino requiere visa
    elif g.get_vertex(to).visa == True and visa == False:
		#Se muestra en interfaz el mensaje que no pueder hacer el viaje
        respuesta = 'Lo sentimos, usted no tiene Visa para ingresar a la ciudad de destino deseada.'
	
    #Otros casos
    else:
        #Si el criterio seleccionado fue el del costo mínimo
        if route == 'Costo mínimo':
            # Se ejecuta el método correspondiente
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

        #Grafo
        grafoFinal = nx.Graph()

        #Si no hay camino entre las dos ciudades
        if target.get_distance() == 99999999999:
            respuesta = 'No hay camino entre ' + str(frm) + ' y ' + str(to) + ' intente cambiando las condiciones de vuelo.'
        #Si el usuario elige como criterio el costo mínimo, el mensaje es
        elif route == 'Costo mínimo':
            respuesta = 'El costo mínimo de ' + str(frm) + ' a ' + str(to) + ' es de $ ' + str(target.get_distance()) + '.'
        #Si el usuario elige como criterio el número de vuelos mínimo
        else:
            respuesta = 'El costo de ' + str(frm) + ' a ' + str(to) + ' es de $ ' + str(sum(costo)) + ' y el número mínimo de vuelos es de ' + str(target.get_distance()) + ' vuelos.'

        #Se pinta el grafo con los resultados
        pintarGrafo(path)

        #Mensaje que indica el camino que debe tomar el usuario
        camino = "La ruta que debe tomar para llegar a su destino es: " + str(path)+"."

        #Colocando el dibujo del grafo con los resultados en la ventana de Tkinter
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, home)
        toolbar.update()
        canvas.get_tk_widget().place(x="775", y="150")

    #Mostrando los labels con sus respectivos mensajes
    label_camino.config(text = camino)
    label_respuesta.config(text = respuesta)


#Boton que lleva a la selección de vuelo
botonComenzar = Button(homeFrame, text="Buscar Viaje", width=25,height=1, bg="#B6CBDE", font=("Roboto", 10, "bold"), command=ejecutarDijkstra).place(x="600", y="580", anchor="center")

home.mainloop()
