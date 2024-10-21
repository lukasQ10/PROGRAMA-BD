import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'capa_logica_negocio')))

from capa_logica_negocio.codigo import calculadora

print("Ejecutanfo presentacion.py")








"""
import sys 
import os
import threading
from tkinter import Tk, Label, Button
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.capa_logica_negocio.codigo import calculadora

def iniciar_calculadora():
  calculadora()

ventana = Tk()
ventana.title("Programa de registro") # titulo en la ventana
ventana.geometry("800x500+0+0") # tamaño de "ancho" y "alto" y tambien ubicación en la pantalla inicialmente
ventana.minsize(400, 200) # tamaño minimo permitido de "ancho" y "alto" 
ventana.maxsize(1200, 800) # tamaño maximo permitido de "ancho" y "alto"
ventana.resizable(True, True) # prohición para agrandar el "ancho" y "alto"; lo que se ponga en false no da permiso y True si da permiso
ventana.configure(bg="azure2") # color de fondo
ventana.attributes("-alpha", 1) # nivel de transparencia desde 0.0 hasta 1

lbl = Label(ventana, text= 'Calculadora')
lbl.pack()
btn = Button(ventana, text= 'Ingresar', command=lambda: threading.Thread(target=iniciar_calculadora))
btn.pack()

ventana.mainloop() # arrancar o bucle principal de arranque

"""