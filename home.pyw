from tkinter import *
from PIL import Image, ImageTk

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

# Boton para que lleva a la interfaz de seleccion de vuelo
botonComenzar = Button(homeFrame, text="Comenzar", width=15, bg="#f5f5f5", font=("Roboto", 10, "bold")).place(x="600", y="600", anchor="center")


home.mainloop()
