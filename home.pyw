#Importaciones respectivas
from operator import le
from tkinter import *
from turtle import color, width
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

#Configuración inicial de la interfaz gráfica

#Creación de la ventana
home = Tk()
#Título de la ventana
home.title("Metro Travel")
#Ícono
home.iconbitmap("imagenes/Logo 2.ico")
home.iconphoto(False, tk.PhotoImage(file='imagenes/Logo 2.png'))
#Para que la ventana no sea redimensionable
home.resizable(0, 0)




#Configuración del frame que va a contener todos los widgets que se van a mostar en la interfaz gráfica
homeFrame = Frame()
homeFrame.pack()
homeFrame.config(bg="#f0ebe7")
homeFrame.config(width="1200", height="795")

#Conficuración de la imagen/logo de la ventana
logoImg = Image.open("imagenes/Logo 2.png")
ajusteLogo = logoImg.resize((130, 130))
logoAjustado = ImageTk.PhotoImage(ajusteLogo)

#creando un canvas para poder hacer el scroll
my_canvas = Canvas(home)
my_canvas.pack(side = LEFT, fill=BOTH, expand = 1)


# Scrollbar de la ventana
scrollbar = Scrollbar(home)
scrollbar.pack(side=RIGHT, fill=Y)

#ahora configuramos el canvas
my_canvas.configure(yscrollcommand=scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))


#ahora hacemos un nuevo frame dentro del canvas, es imperativo para que el scroll pueda funcionar
segundoFrame = Frame(my_canvas)

my_canvas.create_window((0, 0), window = segundoFrame, anchor='nw')


#Etiquetas que se muestran en pantalla con mensajes de Bienvenida
Label(homeFrame, text="¡Bienvenido a la Agencia de Viajes Metro Travel!", fg="#000000", font=("Poppins", 18, "bold"), bg="#f0ebe7").place(x="600", y="50", anchor="center")
Label(homeFrame, image=logoAjustado, bg="#f0ebe7").place(x="50", y="15")
Label(homeFrame, text="En Metro Travel nos especializamos en viajes desde "
                      "el Aeropuerto de Maiquetía hacia diversas Islas del Mar Caribe", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7")\
                    .place(x="600", y="115", anchor="center")


#Etiqueta e imagen que muestran los destinos de la agencia
Label(homeFrame, text="Destinos que ofrecemos:", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="150", y="170", anchor="center")
destinosImg = Image.open("imagenes/Destinos del Proyecto.png")
ajusteDesti = destinosImg.resize((550, 190))
destAjustado = ImageTk.PhotoImage(ajusteDesti)
Label(homeFrame, image=destAjustado, bg="#f0ebe7").place(x="290", y="280",anchor='center')


#COMBOBOXES PARA ELEGIR LA CIUDAD DE ORIGEN Y DESTINO

#Ciudades disponibles
ciudades = ['Caracas - CCS', 'Aruba - AUA', 'Bonaire - BON', 'Curazao - CUR', 'San Martín - SXM', 'Santo Domingo - SDQ', 'San Bartolomé - SBH','Puerto España - POS','Barbados - BGI','Fort de France - FDF','Point a Pitre - PTP']
#Etiqueta y Combobox señalando selección de origen
Label(homeFrame, text="Por favor, seleccione el código del aeropuerto de la ciudad de origen:", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="385")
codigoOrigen = ciudades[0][-3:]
#Etiqueta y Combobox señalando selección de origen
Label(homeFrame, text="Por favor, seleccione el código del aeropuerto de la ciudad de destino:", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="425")
codigoDestino = ciudades[1][-3:]

#Métodos que guardan los códigos de las cuidades de origen y destino
def asignaCodigoOrigen():
    codigo = str(seleccionadoOrigen.get())
    codigoOrigen = codigo[-3:]
    return codigoOrigen

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

#Ubicando los dropdowns de la interfaz
ciudadOrigen_menu.place(x="470", y="385")
ciudadDestino_menu.place(x="470", y="425")


#SELECCIONANDO SI EL CLIENTE TIENE VISA O NO
#Etiqueta señalando que indique si tiene o no el documento
Label(homeFrame, text="¿Posee usted VISA?", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="460")

visaSelected = True

def toggleVisa():
    if seleccionadoVisa.get() == "Si":
        return True
    else:
        return False


opcionesVisas = ["Si", "No"]

seleccionadoVisa = StringVar()
seleccionadoVisa.set(opcionesVisas[0])
seleccionadoVisa_menu = OptionMenu(home, seleccionadoVisa, *opcionesVisas)
seleccionadoVisa_menu.pack()
seleccionadoVisa_menu.place(x="160", y="460")


#SELECCIONANDO SI EL CLIENTE QUIERE EL COSTO O NUMERO DE VUELOS MINIMOS
#Etiqueta señalando que indique si tiene o no el documento
Label(homeFrame, text="¿Qué criterio desea considerar a la hora del viaje? Seleccione 1.- Costo mínimo ó 2.- Número de vuelos mínimo", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="490")

criterio = '1'

def toggleCriterio():
    criterio = seleccionadoCriterio.get()
    return criterio
opcionesCriterio = ['1', '2']

seleccionadoCriterio = StringVar()
seleccionadoCriterio.set(opcionesCriterio[0])
seleccionadoCriterio_menu = OptionMenu(home, seleccionadoCriterio, *opcionesCriterio)
seleccionadoCriterio_menu.pack()
seleccionadoCriterio_menu.place(x="685", y="490")


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

figure= plt.figure(figsize=(3.5, 3.5), dpi=100)
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
canvas.get_tk_widget().place(x="775", y="160")


#METODO PARA EJECUTAR DIJKSTRA Y ENSEÑAR RESULTADO EN PANTALLA
def ejecutarDijkstra():

    frm = asignaCodigoOrigen()
    to = asignaCodigoDestino()
    route = toggleCriterio()
    visa = toggleVisa()
    #creamos el grafo:
    g = createGraph()
    print("Datos del viaje", frm, ",", to, ",", route, ",", visa)
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

    print(path)
    grafoFinal = nx.Graph()
    # Si el usuario elige como criterio el costo mínimo, el mensaje es
    if target.get_distance() == 99999999999:
        print('')
    elif route == '1':
        Label(homeFrame, text="El costo minimo de", fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="590")
        Label(homeFrame, text=frm, fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="165", y="590")
        Label(homeFrame, text="a", fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="210", y="590")
        Label(homeFrame, text=to, fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="235", y="590")
        Label(homeFrame, text="es de:", fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="280", y="590")
        Label(homeFrame, text=target.get_distance(), fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="340", y="590")

        print('El costo mínimo de ' + frm + ' a ' + to + ' es de: $' + str(target.get_distance()))
        print('En este, el camino a tomar será: ')
        
        colors = []

        for x in range(len(arcosGrafoDibujo)):

            grafoFinal.add_edge(arcosGrafoDibujo[x][0], arcosGrafoDibujo[x][1])

            for y in range(len(path) - 1):

                if arcosGrafoDibujo[x] == (path[y], path[y + 1]) or arcosGrafoDibujo[x] == (path[y + 1], path[y]):
                    colors.append('red')
                else:
                    colors.append('blue')

    # Si el usuario elige como criterio el número de vuelos mínimo
    else:

        Label(homeFrame, text="El numero minimo de vuelos de", fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="590")
        Label(homeFrame, text=frm, fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="165", y="590")
        Label(homeFrame, text="a", fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="210", y="590")
        Label(homeFrame, text=to, fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="235", y="590")
        Label(homeFrame, text="es de:", fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="280", y="590")
        Label(homeFrame, text=target.get_distance(), fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="340", y="590")
        Label(homeFrame, text="el costo sera", fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="340", y="590")
        Label(homeFrame, text=sum(costo), fg="#000000",
              font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="340", y="590")

        print(
            'El número mínimo de vuelos de ' + frm + ' a ' + to + ' es de ' + str(target.get_distance()) + ' vuelo-s-')
        print('Para este caso el costo de ' + frm + ' a ' + to + ' es de: $' + str(sum(costo)))
        print('En este, el camino a tomar será: ')

        colors = []

        for x in range(len(arcosGrafoDibujo)):

            grafoFinal.add_edge(arcosGrafoDibujo[x])

            for y in range(len(path) - 1):

                if arcosGrafoDibujo[x] == (path[y], path[y+1]) or arcosGrafoDibujo[x] == (path[y+1], path[y]):
                    colors.append('red')
                else:
                    colors.append('blue')

    Label(homeFrame, text="La ruta que debe tomar para llegar a su destino es:", fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="10", y="560")
    Label(homeFrame, text=path, fg="#000000", font=("Roboto", 12, "bold"), bg="#f0ebe7").place(x="400", y="560")

    # GRAFO FINAL
    figure = plt.figure(figsize=(3.5, 3.5), dpi=100)
    plt.axis('off')
    subplot = figure.add_subplot(111)

    pos = nx.spring_layout(grafoFinal)
    nx.draw_networkx_nodes(grafoFinal, pos, node_size=10)
    nx.draw_networkx_edges(grafoFinal, pos, edgelist=grafoFinal.edges(), width=0.2, edge_color=colors, arrows="-")
    labels_params = {"font_size": 5}
    nx.draw_networkx_labels(grafoFinal, pos, **labels_params)

    canvas = FigureCanvasTkAgg(figure,
                               master=home)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, home)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().place(x="100", y="160")


# Boton que lleva a la interfaz de seleccion de vuelo
botonComenzar = Button(homeFrame, text="Buscar Viaje", width=25,height=1, bg="#B6CBDE", font=("Roboto", 10, "bold"), command=ejecutarDijkstra).place(x="600", y="540", anchor="center")


home.mainloop()
