
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range (101):
    print(i)
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.
num=int(input("Ingrese un numero entero:" ))
digito=0
absoluto= abs(num)
while absoluto > 0:
    absoluto= absoluto//10
    digito += 1
print ("el numero ingresado tiene", digito, "digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.

num1=int(input("Ingrese el menor numero: "))
num2=int(input("Ingrese el siguiente numero "))
suma=0
for i in range (num1+1,num2):
    suma+=i
print(f"la suma de los numeros enteros entre {num1} y {num2} es {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.
numero=1
sumatoria=0
while numero != 0:
    numero=int(input("Ingrese un numero entero: (presione 0 para salir)"))
    sumatoria += numero
print (f"El total acumulado es {sumatoria}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_aleatorio= random.randint(0,9)
num_usuario= -1
intentos=0
while num_aleatorio != num_usuario:
    num_usuario=int(input( "Adivine el numero (entre 0 y 9):"))
    intentos +=1
print(f"Adivinaste! para lograrlo necesitaste {intentos} intentos")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

for i in range (100,1,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

num_natural=int(input("Ingrese un numero natural: "))
sum_num=0

for i in range (num_natural + 1):
    sum_num += i

print(f"La suma entre 0 y el {num_natural} es {sum_num}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).






