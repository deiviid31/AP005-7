#################LISTAS####################  # Encabezado decorativo: inicio de la sección de listas
###########################################  # Línea decorativa separadora
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']  # Crea una lista de colores
#input()  # (comentado) Pausaría el programa esperando que el usuario escriba algo
print(my_lista)  # Imprime la lista completa
print(type(my_lista))  # Imprime el tipo de dato de my_lista (list)
print(my_lista[2])  # Imprime el elemento en el índice 2 ('Amarillo')

print("my_lista size: ", len(my_lista))  # Imprime la cantidad de elementos de la lista
print(my_lista[0:2])  # Imprime una sublista (slice) desde el índice 0 hasta el 1
print(my_lista[:2])  # Imprime lo mismo que arriba; sin inicio equivale a empezar en 0

my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista)  # Imprime la lista con 'Blanco' ya agregado al final

my_lista.insert(3, 'Negro')  # Inserta 'Negro' en la posición de índice 3
print(my_lista)  # Imprime la lista con 'Negro' ya insertado


my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)  # Imprime la lista ya extendida con 'Marron' y 'Gris'

print(my_lista.index('Azul'))  # Imprime el índice donde se encuentra 'Azul'

#my_lista.remove('Magenta')  # (comentado) Intentaría eliminar 'Magenta'; no existe, daría ValueError
my_lista.remove('Marron')  # Elimina la primera aparición de 'Marron' en la lista
print(my_lista)  # Imprime la lista sin 'Marron'

my_lista.insert(8, 'Marron')  # Vuelve a insertar 'Marron', ahora en la posición 8
print(my_lista)  # Imprime la lista con 'Marron' reinsertado

print(my_lista.pop())  # Elimina y muestra el último elemento de la lista
size = len(my_lista)  # Guarda en "size" la cantidad actual de elementos de la lista
print("size = ", size)  # Imprime el tamaño actual de la lista
#print(my_lista.pop(size))  # (comentado) Intentaría sacar el elemento en el índice "size"; está fuera de rango, daría IndexError

my_lista_3 = my_lista*3  # Crea una nueva lista repitiendo my_lista 3 veces seguidas
print("my_lista_3: ", my_lista_3)  # Imprime la lista triplicada

print("Sort:")  # Imprime el texto "Sort:"
print()  # Imprime una línea vacía
my_listaSort = my_lista.sort()  # Ordena my_lista in-place (alfabéticamente) y guarda el valor de retorno (None) en my_listaSort
print(my_listaSort)  # Imprime None, porque sort() no devuelve ningún valor

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]  # Crea una lista de números en orden descendente
print("Ordering my_NumList: ")  # Imprime el texto indicando que se va a ordenar la lista
my_NumList.sort()  # Ordena la lista de números de menor a mayor (in-place)
print(my_NumList)  # Imprime la lista ya ordenada ascendentemente
#OrderedLList = my_NumList.sort()  # (comentado) Guardaría el retorno de sort(), que sería None
#print(my_listaSort)  # (comentado) Imprimiría my_listaSort

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)  # Ordena la lista de mayor a menor (in-place)
print("De menor a mayor: ", my_NumList)  # Imprime la lista ordenada descendentemente (el texto del print dice "de menor a mayor" pero el resultado es descendente)



#################TUPLAS####################  # Encabezado decorativo: inicio de la sección de tuplas
###########################################  # Línea decorativa separadora
# Corresponde a una estructura similar a las listas, la diferencia está  # Nota explicativa sobre las tuplas
# en que no se pueden modificar una vez creadas, es decir que son inmutables:  # Continúa la nota: las tuplas son inmutables

#Convertir una lista a tupla:prin  # Nota indicando el siguiente ejemplo
print("###########################")  # Imprime una línea decorativa
print("###########################")  # Imprime una línea decorativa
print("###########################")  # Imprime una línea decorativa
print("############TUPLAS#########")  # Imprime un encabezado con el texto "TUPLAS"
my_tupla = tuple(my_lista)  # Convierte my_lista en una tupla (inmutable)
print()  # Imprime una línea vacía
print()  # Imprime una línea vacía
print("my_tuple: ", my_tupla)  # Imprime la tupla recién creada

print(my_tupla[0])  # Imprime el primer elemento de la tupla
print(my_tupla[2])  # Imprime el elemento en el índice 2 de la tupla


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)  # Imprime True o False según si 'Rojo' está en la tupla
print(my_tupla.count('Rojo'))  # Imprime cuántas veces aparece 'Rojo' en la tupla

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')  # Ojo: esto NO crea una tupla, crea un string (falta la coma para que sea tupla)
print(my_tupla_unitaria)  # Imprime 'Blanco' (es un string, no una tupla)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999  # Crea una tupla por "empaquetado", sin usar paréntesis
print(my_tupla)  # Imprime la tupla empaquetada

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla  # Desempaqueta la tupla asignando cada valor a una variable
print(nombre)  # Imprime el valor de "nombre"
print(dia)  # Imprime el valor de "dia"
print(mes)  # Imprime el valor de "mes"
print(año)  # Imprime el valor de "año"

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)  # Imprime todos los valores desempaquetados en un solo print

#Convertir una tupla en una lista
my_lista2=list(my_tupla)  # Convierte la tupla en una lista nueva
print(my_lista2)  # Imprime la lista resultante de la conversión
