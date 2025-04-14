#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad= int(input("Por favor ingrese su edad : "))
if edad > 18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota= int(input("Por favor ingrese su nota: "))
if nota >=6:
        print("Aprobado")
else:
        print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar

numero= int(input("Ingrsa un numero par"))
if numero % 2==0:
       print ("Ha ingresado un numero par")
else:
       print("Por favor, ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

años= int(input("ingrese su edad:"))
if 0 <= años < 12 :
       print ("Eres un niño/a")
elif 12 <= años < 18:
       print ("Eres un adolescente") 
elif 18 <= años < 30:
       print("Eres un adulto/a joven")
elif años > 30:
       print("Eres un adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.
contraseña= (input("Ingrese una contraseña entre 8 y 14 caracteres"))
if 8 <= len(contraseña)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres")

#6)escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mode, median, mean  
numeros_aleatorios= [random.randint(1,100)for i in range(50)]     
moda= mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
if media>mediana > moda:
       print("Segos positivo")
if media< mediana < moda:
       print("Sesgo negativo")
if media==mediana==moda:
       print("sin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
frase= input("Por favor, ingrese una frase o una palabra:")
if frase[-1] in ("aeiouAEIOU"):
       print(frase,"!")
else:
       print(frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas
print("A continuacion, ingrese su nombre y la opcion como desea que se muestre por pantalla:" \
"1: se mostrara su nombre todo en mayuscula" \
"2: se mostrara su nombre todo en minuscula" \
"3: se mostrara la primera letra de su nombre en mayuscula y el resto en minuscula")
nombre= input("Por favor, ingrese su nombre")
opcion= int(input("Ingrese la opcion deseada:"))
if opcion==1:
       print(nombre.upper())
elif opcion==2:
       print(nombre.lower())
elif opcion==3:
       print(nombre.title())

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
escala=float(input( "Ingrese la magnitud del terremoto: "))
if 0<escala<3:
       print("Muy leve")
elif 3<=escala<4:
       print("Leve")
elif 4<=escala<5:
       print("Moderado") 
elif 5<=escala<6:
       print("Fuerte")
elif 6<=escala<7:
       print("Muy Fuerte")
else:
       print("Extremo")      
#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio=input("Por favor, di en que hemisferio te encuentras(N/S): ")
mes=input("En que mes estas?(1 al 12): ")
dia=input("Que dia es?: ")
if hemisferio=="S":
       if (mes==12 and dia>=21) or (mes==1) or (mes==2) or (mes==3 and dia<21):
              print("Verano")
       elif (mes==3 and dia>=21) or (mes==4) or (mes==5) or (mes==6 and dia<21):
              print("Otoño")
       elif (mes==6 and dia>=21) or (mes==7) or (mes==8) or (mes==9 and dia <21):
              print("Invierno")
       elif (mes==9 and dia >= 21) or (mes==10) or (mes==11) or (mes==12 and dia <21):
              print("Primavera")
if hemisferio=="N":
       if (mes==12 and dia>=21) or (mes==1) or (mes==2) or (mes==3 and dia<21):
              print("Invierno")
       elif (mes==3 and dia>=21) or (mes==4) or (mes==5) or (mes==6 and dia<21):
              print("Primavera")
       elif (mes==6 and dia>=21) or (mes==7) or (mes==8) or (mes==9 and dia <21):
              print("Verano") 
       elif (mes==9 and dia >= 21) or (mes==10) or (mes==11) or (mes==12 and dia <21):
              print("Otoño")      
              



