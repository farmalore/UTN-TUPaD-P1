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

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range (1,11):
        print (f"{numero} x {i} = {numero * i}")
              
numero =int(input("Ingrese el numero que quiere saber su tabla:"))
tabla_multiplicar(numero)   

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma= a+b
    resta= a-b
    multiplicacion= a * b
    division= a/b
    print(f"La suma de los numeros ingresados es {suma}, la resta {resta}, la multiplicacion es {multiplicacion} y la division es {division}")

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
operaciones_basicas(num1,num2)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def  calcular_imc(peso, altura):
    imc= peso/(altura**2)
    imc2=round(imc,2)
    print(f"Su IMC es {imc2}")

peso=float(input("Ingrese su peso (en kg): "))
altura=float(input("Ingreso su altura (en metros): "))
calcular_imc(peso, altura)

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit=(celsius * 1.8 + 32)
    print(f"La temperatura ingresada corresponde a {fahrenheit} °F")

celsius= float(input("Ingrese la temperatura en grados celsius "))
celsius_a_fahrenheit(celsius)

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a, b, c):
    promedio=((a + b + c)/3)
    print(f"El promedio de los tres numeros es {promedio}")

a=float(input("Ingrese el primer numero: "))
b=float(input("Ingrese el segundo numero: "))
c=float(input("Ingrese el tercer numero: "))
calcular_promedio(a, b, c)



              