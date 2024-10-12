

"""
import sys 
import os
import threading
from tkinter import Tk, Label, Button
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from capa_logica_negocio.codigo import calculadora

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


import sys
import os
from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu
#from src.capa_logica_negocio.codigo import calculadora

# Agregar la ruta del módulo
#sys.path.append(r"f:/ANALISIS Y DESARROLLO/PROGRAMA-BD/src")
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def realizar_operacion():
    x = int(entry_x.get())
    y = int(entry_y.get())
    operacion = seleccion_operacion.get()
    resultado = calculadora(operacion, x, y)
    label_resultado.config(text=f"Resultado: {resultado}")

ventana = Tk()
ventana.title("Calculadora GUI")  
ventana.geometry("400x300")  
ventana.configure(bg="azure2")

# Etiqueta para operación
label_operacion = Label(ventana, text="Seleccione operación:")
label_operacion.pack()

# Menú desplegable para seleccionar operación
operaciones = ["suma", "resta", "multi", "divi"]
seleccion_operacion = StringVar(ventana)
seleccion_operacion.set(operaciones[0])
menu_operacion = OptionMenu(ventana, seleccion_operacion, *operaciones)
menu_operacion.pack()

# Entradas para los números
label_x = Label(ventana, text="Ingrese el primer número:")
label_x.pack()
entry_x = Entry(ventana)
entry_x.pack()

label_y = Label(ventana, text="Ingrese el segundo número:")
label_y.pack()
entry_y = Entry(ventana)
entry_y.pack()

# Botón para realizar la operación
btn_calcular = Button(ventana, text="Calcular", command=realizar_operacion)
btn_calcular.pack()

# Etiqueta para mostrar el resultado
label_resultado = Label(ventana, text="Resultado: ")
label_resultado.pack()

ventana.mainloop()

