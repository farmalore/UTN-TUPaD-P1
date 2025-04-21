#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo ():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre=input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
    
def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido},tengo {edad} y vivo en {residencia}")

nom= input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido:")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido,edad, residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
#  calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el 
# radio al usuario y llamar ambas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    pi=3.14
    area= pi * (radio **2)
    print(f"El area del ciculo es {area}")

def  calcular_perimetro_circulo(radio):
    pi=3.14
    perimetro=2*pi*radio
    print(f"El perimetro del circulo es {perimetro}")

radio=float(input("Ingrese el radio del circulo que se desea saber su area y perimetro: "))
calcular_area_circulo(radio) 
calcular_perimetro_circulo(radio)

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas=segundos/3600
    print (f"los {segundos} equivalen a {horas} horas.")

segundos=float(input("ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)
