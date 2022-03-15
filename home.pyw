from tkinter import *
from PIL import Image, ImageTk
from dijkstra import *
from graph import *
from node import *
from data import *
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

# Configuracion inicial de la interfaz grafica
home = Tk()

home.title("Metro Travel")

home.iconbitmap("imagenes/Logo 2.ico")

home.resizable(0, 0)

# Configuracion del frame que va a contener todos los widgets que se van a mostar en la interfaz grafica
homeFrame = Frame()

homeFrame.pack()

homeFrame.config(bg="#f0ebe7")

homeFrame.config(width="1200", height="650")

# Conficuracion de la imagen
logoImg = Image.open("imagenes/Logo 2.png")

ajusteLogo = logoImg.resize((150, 150))

logoAjustado = ImageTk.PhotoImage(ajusteLogo)

# Las etiquetas que de muestran en pantalla
Label(homeFrame, text="¡Bienvenido a la Agencia de Viajes Metro Travel!", fg="#000000", font=("Poppins", 18, "bold"), bg="#f0ebe7").place(x="600", y="50", anchor="center")

Label(homeFrame, image=logoAjustado, bg="#f0ebe7").place(x="50", y="0")

Label(homeFrame, text="En Metro Travel nos especializamos en viajes desde "
                      "el Aeropuerto de Maiquetía hacia diversas Islas del Mar Caribe", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7")\
                    .place(x="600", y="160", anchor="center")


#COMBOBOXES PARA ELEGIR LA CIUDAD DE ORIGEN Y DESTINO
ciudades = ['Caracas - CCS', 'Aruba - AUA', 'Bonaire - BON', 'Curazao - CUR', 'San Martín - SXM', 'Santo Domingo - SDQ', 'San Bartolomé - SBH','Puerto España - POS','Barbados - BGI','Fort de France - FDF','Point a Pitre - PTP']

codigoOrigen = ciudades[0][-3:]
codigoDestino = ciudades[1][-3:]
#metodos que guardan los codigos de la cuidad de origen y destino
def asignaCodigoOrigen(event):
    codigo = str(seleccionadoOrigen.get())
    codigoOrigen = codigo[-3:]
    print("seleccionado Origen", codigoOrigen)

def asignaCodigoDestino(event):
    codigo = str(seleccionadoDestino.get())
    codigoDestino = codigo[-3:]
    print("seleccionado Destino", codigoDestino)


seleccionadoOrigen = StringVar()
seleccionadoOrigen.set(ciudades[0])
ciudadOrigen_menu = OptionMenu(home, seleccionadoOrigen, *ciudades, command=asignaCodigoOrigen)
ciudadOrigen_menu.pack()

seleccionadoDestino = StringVar()
seleccionadoDestino.set(ciudades[1])
ciudadDestino_menu = OptionMenu(home, seleccionadoDestino, *ciudades, command=asignaCodigoDestino)
ciudadDestino_menu.pack()

#Haciendo placing de los dropdowns
ciudadOrigen_menu.place(x="400", y="250")
ciudadDestino_menu.place(x="650", y="250")


#SELECCIONANDO SI EL CLIENTE TIENE VISA O NO
visaSelected = True

def toggleVisa(event):
    if seleccionadoVisa.get() == "Si":
        visaSelected = True
    else:
        visaSelected = False

    print("Visa", visaSelected)

opcionesVisas = ["Si", "No"]

seleccionadoVisa = StringVar()
seleccionadoVisa.set(opcionesVisas[0])
seleccionadoVisa_menu = OptionMenu(home, seleccionadoVisa, *opcionesVisas, command=toggleVisa)
seleccionadoVisa_menu.pack()
seleccionadoVisa_menu.place(x="450", y="325")


#SELECCIONANDO SI EL CLIENTE QUIERE EL COSTO O NUMERO DE VUELOS MINIMOS
criterio = '1'

def toggleCriterio(event):
    criterio =  seleccionadoCriterio.get()
    print("criterio", criterio)

opcionesCriterio = ['1', '2']

seleccionadoCriterio = StringVar()
seleccionadoCriterio.set(opcionesCriterio[0])
seleccionadoCriterio_menu = OptionMenu(home, seleccionadoCriterio, *opcionesCriterio, command=toggleCriterio)
seleccionadoCriterio_menu.pack()
seleccionadoCriterio_menu.place(x="675", y="325")


#DIBUJANDO EL GRAFO COMPLETO


grafoDibujo = nx.Graph()
grafoDatos = createGraph()

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

figure= plt.figure(figsize=(1.5, 1.5), dpi=100)
plt.axis('off')
subplot= figure.add_subplot(111)

grafoDibujo.add_edges_from(arcosGrafoDibujo)

pos = nx.spring_layout(grafoDibujo)
nx.draw_networkx_nodes(grafoDibujo, pos, node_size=10)
nx.draw_networkx_edges(grafoDibujo, pos, edgelist=grafoDibujo.edges(), width=0.2, edge_color='black', arrows="-")
labels_params = {"font_size":5 }
nx.draw_networkx_labels(grafoDibujo, pos, **labels_params)


canvas = FigureCanvasTkAgg(figure,
                           master=home)
canvas.draw()

# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, home)
toolbar.update()

# placing the toolbar on the Tkinter window
# canvas.get_tk_widget().pack()
canvas.get_tk_widget().place(x="975", y="100")
# dibujo = FigureCanvasTkAgg(figure, home)
#dibujo.get_tk_widget().grid(row=5, column=0)





#METODO PARA EJECUTAR DIJKSTRA
def ejecutarDijkstra():

    frm = codigoOrigen
    to = codigoDestino
    route = criterio
    visa = visaSelected
    #creamos el grafo:
    g = createGraph()
    if route == '1':
        # Se ejecuta el método correspondiente
        dijkstra_min_cost(g, g.get_vertex(frm), g.get_vertex(to), visa)
        # Sino, si el usuario elige como criterio el número de vuelos mínimo
    else:
        # Se ejecuta el método correspondiente
        dijkstra_min_steps(g, g.get_vertex(frm), g.get_vertex(to), visa)

        # Reconstruir el camino obtenido por el método correspondiente
    target = g.get_vertex(to)
    path = [target.get_id()]
    costo = []
    shortest(target, path, costo)
    path.reverse()

    # Mensaje de resultado para el usuario

    # Si el usuario elige como criterio el costo mínimo, el mensaje es
    if target.get_distance() == 99999999999:
        print('')
    elif route == '1':
        print('El costo mínimo de ' + frm + ' a ' + to + ' es de: $' + str(target.get_distance()))
        print('En este, el camino a tomar será: ')
        for x in range(len(path)):
            print(str(path[x]))

    # Si el usuario elige como criterio el número de vuelos mínimo
    else:
        print(
            'El número mínimo de vuelos de ' + frm + ' a ' + to + ' es de ' + str(target.get_distance()) + ' vuelo-s-')
        print('Para este caso el costo de ' + frm + ' a ' + to + ' es de: $' + str(sum(costo)))
        print('En este, el camino a tomar será: ')
        for x in range(len(path)):
            print(str(path[x]))


# Boton para que lleva a la interfaz de seleccion de vuelo
botonComenzar = Button(homeFrame, text="Comenzar", width=15, bg="#f5f5f5", font=("Roboto", 10, "bold"), command=ejecutarDijkstra).place(x="600", y="600", anchor="center")


home.mainloop()
