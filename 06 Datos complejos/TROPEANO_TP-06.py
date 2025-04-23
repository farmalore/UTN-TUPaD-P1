#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.
numero=list(range(1,101,4))
print(numero)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

dias_habiles=["lunes","martes","miercoles","jueves","viernes"]
print(dias_habiles[3])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo:
#lista_vacia = []

calles=[]
calles.append("Rivadavia")
calles.append("Calchaqui")
calles.append("M_Rodriguez")

print(calles)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!

animales = ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[3]="oso"
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
#en una lista dad utilizando la funcion remove + max = elimina el valor mas grande de la lista.






