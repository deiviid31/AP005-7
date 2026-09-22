# sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}  # (comentado) Crea un diccionario habitación:temperatura
# num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}  # (comentado) Crea un diccionario lugar:cantidad de cámaras

# print(sensors)  # (comentado) Imprimiría el diccionario sensors
# print(num_cameras)  # (comentado) Imprimiría el diccionario num_cameras
# translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }  # (comentado) Crea un diccionario de traducciones inglés-élfico
# print(translations)  # (comentado) Imprimiría el diccionario translations

##Verifiying an error:  # Encabezado: se va a mostrar un ejemplo que produce un error
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}  # (comentado) Inválido: usa listas como claves; las listas no son hashables -> daría TypeError
# # print(powers)  # (doblemente comentado) Imprimiría powers si existiera

# children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}  # (comentado) Crea diccionario apellido:lista de hijos
# print(children)  # (comentado) Imprimiría el diccionario children

# my_empty_dictionary = {}  # (comentado) Crea un diccionario vacío
# print(my_empty_dictionary)  # (comentado) Imprimiría el diccionario vacío

# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  # (comentado) Crea diccionario plato:precio
# print("Before: ", menu)  # (comentado) Imprimiría el menu antes de modificarlo
# menu["cheesecake"] = 8  # (comentado) Agregaría la clave "cheesecake" con valor 8
# print("After", menu)  # (comentado) Imprimiría el menu después de agregar cheesecake
# animals_in_zoo = {"dinosaurs": 0}  # (comentado) Crea diccionario con "dinosaurs":0
# animals_in_zoo = {"dinosaurs": 0}  # (comentado) Vuelve a crear el mismo diccionario (línea repetida)
# animals_in_zoo = {"horses": 2}  # (comentado) Sobrescribe animals_in_zoo por uno nuevo con "horses"
# print(animals_in_zoo)  # (comentado) Imprimiría el diccionario final animals_in_zoo


##Add multiple keys  # Encabezado: agregar varias claves a la vez
# sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}  # (comentado) Crea diccionario sensors con 3 habitaciones
# print("Before", sensors)  # (comentado) Imprimiría sensors antes de agregar más claves

# #If we wanted to add 3 new rooms, we could use:  # (comentado) Nota explicativa
# sensors.update({"pantry": 22, "guest room": 25, "patio": 34})  # (comentado) Agregaría 3 claves nuevas usando update()
# print("After", sensors)  # (comentado) Imprimiría sensors con las claves nuevas

###  # Separador decorativo
# user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}  # (comentado) Crea diccionario usuario:ID
# print(user_ids)  # (comentado) Imprimiría user_ids
# user_ids.update({"theLooper": 138475, "stringQueen": 85739})  # (comentado) Agregaría dos usuarios nuevos con update()
# print(user_ids)  # (comentado) Imprimiría user_ids actualizado

## Overwrite Values ##  # Encabezado: sobrescribir valores existentes
#We know that we can add a key by using the following syntax:  # Nota explicativa
#menu["banana"] = 3  # (comentado) Ejemplo de cómo agregar la clave "banana"
# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  # (comentado) Crea diccionario menu
# print("Before: ", menu)  # (comentado) Imprimiría menu antes de sobrescribir
# menu["oatmeal"] = 5  # (comentado) Sobrescribiría el valor de "oatmeal" a 5
# print("After", menu)  # (comentado) Imprimiría menu con el valor ya actualizado

## Notice the value of "oatmeal" has now changed to 5.  # Nota aclaratoria
# oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}  # (comentado) Crea diccionario categoría:ganador
# print("Before", oscar_winners)  # (comentado) Imprimiría oscar_winners antes de cambios
# print()  # (comentado) Imprimiría una línea en blanco
# oscar_winners.update({"Supporting Actress": "Viola Davis"})  # (comentado) Agregaría nueva categoría con update()
# print("After1", oscar_winners)  # (comentado) Imprimiría oscar_winners tras el update
# print()  # (comentado) Imprimiría otra línea en blanco
# oscar_winners["Best Picture"] = "Moonlight"  # (comentado) Sobrescribiría el valor de "Best Picture"
# print("After2", oscar_winners)  # (comentado) Imprimiría oscar_winners final


###Dict Comprehensions  # Encabezado: comprensión de diccionarios
#Let’s say we have two lists that we want to combine into a   # Nota explicativa
#dictionary, like a list of students and a list of their heights,   # Continúa la nota explicativa
#in inches:  # Continúa la nota explicativa

names = ['Jenny', 'Alexus', 'Sam', 'Grace']  # Crea una lista de nombres de estudiantes
heights = [61, 70, 67, 64]  # Crea una lista de estaturas (en pulgadas)

#Python allows you to create a dictionary using   # Nota explicativa
# a dict comprehension, with this syntax:  # Continúa la nota explicativa

# zipStudents = zip(names, heights)  # (comentado) Combinaría names y heights en un iterador de tuplas
# print("zipStudents: ", zipStudents)  # (comentado) Imprimiría el objeto zip (no su contenido directamente)

# students = {key:value for key, value in zip(names, heights)}  # (comentado) Crearía diccionario nombre:estatura con comprensión
# #students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}  # Nota que muestra el resultado esperado
# print(students)  # (comentado) Imprimiría el diccionario students

# #zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:  # Nota explicativa sobre zip()

# drinks = ["espresso", "chai", "decaf", "drip"]  # (comentado) Crearía lista de bebidas
# caffeine = [64, 40, 0, 120]  # (comentado) Crearía lista de niveles de cafeína

# zipped_drinks = zip(drinks, caffeine)  # (comentado) Combinaría ambas listas en un iterador de tuplas
# print(zipped_drinks)  # (comentado) Imprimiría el objeto zip

# drinks_to_caffeine = {key:value for key, value in zipped_drinks}  # (comentado) Crearía diccionario bebida:cafeína
# print(drinks_to_caffeine)  # (comentado) Imprimiría el diccionario resultante

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]  # Crea una lista de canciones
playcounts = [78, 29, 44, 21, 89, 5]  # Crea una lista con la cantidad de reproducciones de cada canción
plays = {key:value for key, value in zip(songs, playcounts)}  # Crea diccionario canción:reproducciones usando zip + comprensión
print(plays)  # Imprime el diccionario plays recién creado
plays.update({"Purple Haze": 1})  # Agrega la canción "Purple Haze" con 1 reproducción
plays.update({"Respect": 94})  # Actualiza el valor de "Respect" a 94 reproducciones
print("After: ", plays)  # Imprime el diccionario plays ya actualizado
library = {"The Best Songs": plays, "Sunday Feelings": {}}  # Crea un diccionario anidado: playlist "The Best Songs" = plays, y otra vacía
print(library)  # Imprime el diccionario library completo
