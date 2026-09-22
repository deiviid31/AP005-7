# #### Get A Key  # (comentado) Encabezado: obtener un valor por su clave
# #you can access the values in it by providing the key:  # (comentado) Nota explicativa

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # (comentado) Crea diccionario edificio:altura
# print(building_heights["Burj Khalifa"]) # Prints 828  # (comentado) Imprimiría la altura del Burj Khalifa
# print(building_heights["Ping An"]) # Prints 599  # (comentado) Imprimiría la altura de Ping An

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}  # (comentado) Crea diccionario elemento:lista de signos
# print(zodiac_elements["earth"])  # (comentado) Imprimiría la lista de signos de tierra
# print(zodiac_elements["fire"])  # (comentado) Imprimiría la lista de signos de fuego

# ## Get an Invalid Key  # (comentado) Encabezado: acceder a una clave inválida

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # (comentado) Vuelve a crear el diccionario building_heights
# print(building_heights["Landmark 81"])  # (comentado) Daría KeyError porque esa clave no existe

# ##One way to avoid this error is to first check if the key exists in the dictionary:  # (comentado) Nota explicativa
# key_to_check = "Landmark 81"  # (comentado) Guarda en una variable la clave a verificar

# if key_to_check in building_heights:  # (comentado) Verificaría si la clave existe antes de acceder
#   print(building_heights["Landmark 81"])  # (comentado) Imprimiría el valor solo si la clave existiera

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}  # (comentado) Vuelve a crear el diccionario zodiac_elements

# zodiac_elements["energy"] = "Not a Zodiac element"  # (comentado) Agregaría una nueva clave "energy" con un texto como valor

# if "energy" in zodiac_elements:  # (comentado) Verificaría si "energy" está en el diccionario
#   print(zodiac_elements["energy"])  # (comentado) Imprimiría el valor de "energy"

# ##Safely Get a Key  # (comentado) Encabezado: obtener una clave de forma segura
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # (comentado) Vuelve a crear el diccionario building_heights

# #this line will return 632:  # (comentado) Nota explicativa
# building_heights.get("Shanghai Tower")  # (comentado) Devolvería 632 usando get(), sin riesgo de error

# #this line will return None:  # (comentado) Nota explicativa
# building_heights.get("My House")  # (comentado) Devolvería None porque esa clave no existe

# ###  # (comentado) Separador decorativo
# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}  # (comentado) Crea diccionario usuario:ID
# user_ids.get("teraCoder")  # (comentado) Devolvería el ID de "teraCoder" usando get()

# if user_ids.get("teraCoder") == None:  # (comentado) Verificaría si "teraCoder" no existe en el diccionario
#    tc_id = 1000  # (comentado) Asignaría un valor por defecto (1000) si no existiera
# else:   # (comentado) Caso contrario, si sí existe la clave
#    tc_id = user_ids.get("teraCoder")  # (comentado) Asignaría el ID real de "teraCoder"

# print(tc_id)  # (comentado) Imprimiría el valor final de tc_id

# if user_ids.get("superStackSmash") == None:  # (comentado) Verificaría si esa clave no existe
#      stack_id = 100000  # (comentado) Asignaría un valor por defecto si no existiera

# print(stack_id)  # (comentado) Imprimiría stack_id (fallaría si el if no se ejecutó, por no estar definida)

# ###Delete a Key  # (comentado) Encabezado: eliminar una clave
#.pop() works to delete items from a dictionary, when you know the key value.  # (comentado) Nota explicativa sobre pop()
#raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}  # (comentado) Crea diccionario número:premio
#print(raffle.pop(320291, "No Prize"))  # (comentado) Eliminaría y devolvería el valor de la clave 320291 ("Gift Basket")
## Prints "Gift Basket"  # (comentado) Nota: resultado esperado del print anterior
#print(raffle)  # (comentado) Imprimiría el diccionario sin la clave 320291
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}  # (comentado) Nota: resultado esperado
# print(raffle.pop(100000, "No Prize"))  # (comentado) Como 100000 no existe, devolvería el valor por defecto "No Prize"
# # Prints "No Prize"  # (comentado) Nota: resultado esperado
# print(raffle)  # (comentado) Imprimiría el diccionario sin cambios (no se eliminó nada)
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}  # (comentado) Nota: resultado esperado
# print(raffle.pop(872921, "No Prize"))  # (comentado) Eliminaría y devolvería el valor de la clave 872921 ("Concert Tickets")
# # Prints "Concert Tickets"  # (comentado) Nota: resultado esperado
# print(raffle)  # (comentado) Imprimiría el diccionario sin la clave 872921
# # Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}  # (comentado) Nota: resultado esperado final

# available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}  # (comentado) Crea diccionario ítem:puntos de vida
# health_points = 20  # (comentado) Inicializa la variable de puntos de vida en 20

# health_points += available_items.pop("stamina grains", 0)  # (comentado) Sumaría y eliminaría "stamina grains" del diccionario
# health_points += available_items.pop("power stew", 0)  # (comentado) Sumaría y eliminaría "power stew" del diccionario
# health_points += available_items.pop("mystic bread", 0)  # (comentado) Como no existe, sumaría 0 (valor por defecto)

# print(available_items)  # (comentado) Imprimiría el diccionario restante de ítems
# print(health_points)  # (comentado) Imprimiría el total final de puntos de vida

# ##Get All Keys  # (comentado) Encabezado: obtener todas las claves
# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}  # (comentado) Crea diccionario estudiante:lista de notas
# print(list(test_scores))  # (comentado) Imprimiría una lista con todas las claves del diccionario
# # Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]  # (comentado) Nota: resultado esperado

# for student in test_scores.keys():  # (comentado) Recorrería todas las claves del diccionario
#  print(student)  # (comentado) Imprimiría cada nombre de estudiante

# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}  # (comentado) Crea diccionario usuario:ID
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}  # (comentado) Crea diccionario tema:cantidad de ejercicios

# users = user_ids.keys()  # (comentado) Guardaría todas las claves (usuarios) en "users"
# lessons = num_exercises.keys()  # (comentado) Guardaría todas las claves (temas) en "lessons"

# print(users)  # (comentado) Imprimiría la vista de claves "users"
# print(lessons)  # (comentado) Imprimiría la vista de claves "lessons"

##Get All Values  # Encabezado: obtener todos los valores
# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}  # (comentado) Crea diccionario estudiante:lista de notas

# for score_list in test_scores.values():  # (comentado) Recorrería todos los valores (listas de notas)
#  print(score_list)  # (comentado) Imprimiría cada lista de notas
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}  # (comentado) Crea diccionario tema:cantidad de ejercicios

# total_exercises = 0  # (comentado) Inicializa un contador total en 0

# for exercises in num_exercises.values():  # (comentado) Recorrería todos los valores (cantidades) del diccionario
#   total_exercises += exercises  # (comentado) Sumaría cada cantidad al total
# print(total_exercises)  # (comentado) Imprimiría la suma total de ejercicios

##Get All Items  # Encabezado: obtener todos los pares clave-valor
# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}  # (comentado) Crea diccionario marca:valor en miles de millones

# for company, value in biggest_brands.items():  # (comentado) Recorrería cada par clave-valor del diccionario
#  print(company + " has a value of " + str(value) + " billion dollars. ")  # (comentado) Imprimiría una frase con la marca y su valor

# pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}  # (comentado) Crea diccionario ocupación:porcentaje de mujeres

# for occupation, percentage in pct_women_in_occupation.items():  # (comentado) Recorrería cada par ocupación-porcentaje
#   print("Women make up " + str(percentage) + " percent of " + occupation + "s.")   # (comentado) Imprimiría una frase con el porcentaje y la ocupación
