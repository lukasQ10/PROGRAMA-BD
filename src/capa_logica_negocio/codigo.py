
def suma(x, y):
  return x + y
def resta(x, y):
  return x - y
def multi(x, y):
  return x * y
def divi(x, y):
  return  "No se puede dividir por cero" if y == 0 else x / y


def calculadora():
  while True:
    print('''Operaciones disponibles:
          1. Suma
          2. Resta
          3. Multiplicación
          4. División
          5. Salir
          ''')
    try:
      eleccion = int(input('Ingrese el numero de la operacion que desea realizar: '))
      if eleccion in {1, 2, 3, 4, 5}:
        if eleccion == 5:
          print("Fue un gusto servirte")
          break
          
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
      else:
        print("\nNúmero no valido; ingrese un numero del 1 al 5 según la operación")
      
      
    except ValueError:
      print("no puedes ingresar un caracter diferente a un númeroIngrese solamente un número según la operación ")  
if __name__ == '__main__':
  calculadora()    




