def suma(x, y):
  return x + y
def resta(x, y):
  return x - y
def multi(x, y):
  return x * y
def divi(x, y):
  if y == 0:
    return  "No se puede dividir por cero" if y == 0 else x / y


def calculadora():
  while True:
    print("""Operaciones disponibles:
          1. Suma
          2. Resta
          3. Multiplicación
          4. División
          5. Salir
          """)
    try:
      eleccion = int(input('Ingrese el numero que de la operacion que desea consultar: '))
      if eleccion in {1, 2, 3, 4, 5}:
        x = int(input('Ingrese el primer numero: '))
        y = int(input('Ingrese el segundo numero: '))
        
        if eleccion == 1:
          print (f'El resultado es: {suma(x, y)}')
        elif eleccion == 2:
          print (f'El resultado es: {resta(x, y)}')
        elif eleccion == 3:
          print (f'El resultado es: {multi(x, y)}')    
        elif eleccion == 4:
          print (f'El resultado es: {divi(x, y)}')
        elif eleccion == 5:
          print("Fue un gusto servirte") 
        break
      else:
        print("\nNúmero no valido; ingrese un numero del 1 al 5 según la operación")
      
      
    except ValueError:
      print("Ingrese solamente un numero acorde ")  
if __name__ == '__main__':
  calculadora()    