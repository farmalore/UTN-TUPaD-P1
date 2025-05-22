#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario

def factorial(n):
 if n == 0:
   return 1
 else:
  return n * factorial(n - 1)
 
num=int(input("Ingrese un numero natural: "))
for i in range(1,num+1):
 print("El factorial de", i, "es",factorial(i))

 #2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique.

def fibonacci(n):
 if n == 0:
  return 0
 elif n == 1:
  return 1
 else:
  return fibonacci(n - 1) + fibonacci(n - 2)
 
posicion=int(input("Ingrese la posicion para calcular fibonacci: "))
for i in range(1,posicion+1):
  print("fibonacci",i,fibonacci(i))

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1)
#Prueba esta función en un algoritmo general.
n=2
m=3
pot=n*n*(m-1)
print(pot)

def potencia(n,b):
 if n==0:
  return 1
 elif b==1:
  return 1
 else:
  return n*n*(b-1)

print(potencia(2,3))

#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)
num=int(input("Ingrese un numero entero positivo para convertir a binario: "))
print(f"el numero decimal convertido a binario es {decimal_a_binario(num)}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es.
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
palabra=input("Ingrese la palabra a comprobar: ")
print(es_palindromo(palabra))

#6)Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos.
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
numero=int(input("Ingrese el numero que quiera sumar sus digitos: "))
print(f"La suma de los digitos del numero ingresado es {suma_digitos(numero)}")
#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide.
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
bloques=int(input("Ingrese la cantidad de bloques del nivel mas bajo: "))
print(f"Los bloques necesarios para construir la piramide son {contar_bloques(bloques)}")

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        coincidencia = 1 if numero % 10 == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)
num1=int(input("Ingrese un numero: "))
digito=int(input("Ingrese el digito que desea verificar la repetecion: "))
print(f"El {digito} se repite en {num1} {contar_digito(num1,digito)} veces.")











