import tkinter as tk
ventana = tk.Tk()
ventana.title("Programa de registro") # titulo en la ventana
ventana.geometry("800x500+0+0") # tamaño de ancho y alto y tambien ubicación en la pantalla inicialmente
ventana.minsize(400, 200) # tamaño minimo permitido de ancho y alto 
ventana.maxsize(1200, 800) # tamaño maximo permitido de ancho y alto
ventana.resizable(True, True) # prohición para agrandar el ancho y alto; lo que se ponga en false no da permiso y True si da permiso
ventana.configure(bg="azure2") # color de fondo
ventana.attributes("-alpha", 0.9) # nivel de transparencia desde 0.0 hasta 1
ventana.mainloop() # arrancar o bucle de arranque
