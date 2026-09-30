# Importamos la librería "time" para poder usar time.sleep() y hacer pausas
import time

# Datos de entrada: los valores que le vamos a dar a la neurona
inputs = [1, 2, 3, 4]
# Respuestas correctas para cada entrada (cada target es el doble de su input).
# Es lo que queremos que la neurona aprenda.
targets = [2, 4, 6, 8]

# w es el peso de la neurona. Empieza con un valor cualquiera (0.1) y se irá
# ajustando durante el entrenamiento hasta acercarse al valor correcto (2)
w = 0.1
# learning_rate (tasa de aprendizaje): qué tan grande es cada ajuste del peso.
# Si es muy grande se pasa de largo, si es muy pequeña aprende muy lento
learning_rate = 0.1

# Función que calcula la predicción de la neurona para una entrada "i"
def predict(i):
  # La neurona multiplica la entrada por su peso. Usa el valor actual de w,
  # por eso cada vez que w cambia, las predicciones también cambian
  return w*i

#Train the network
# Repetimos el entrenamiento 30 veces (30 épocas). Una época es una pasada
# completa por todos los datos. Usamos "_" porque no necesitamos el contador
for _ in range(30):
  # Imprime una línea de guiones para separar visualmente cada época
  print("---------------------")
  # Imprime el título de la época
  print("Nueva Epoca")
  # Otra línea de guiones
  print("---------------------")
  # "for i in inputs" recorre la lista inputs: en cada vuelta i toma el valor
  # 1, luego 2, luego 3 y luego 4. Para cada i llamamos predict(i) y guardamos
  # todos los resultados en la lista pred (esto se llama list comprehension)
  pred = [predict(i) for i in inputs]
  # zip(pred, targets) junta las dos listas de a pares: (p1, t1), (p2, t2)...
  # Por cada par calculamos el error = valor correcto - predicción
  errors = [t - p for p, t in zip(pred, targets)]
  # Costo: promedio de los errores. Se suman todos y se divide entre la
  # cantidad de datos (len(targets) = 4). Nos dice qué tan lejos está la neurona
  cost = sum(errors)/len(targets)
  # Muestra los valores correctos. Como se pasan dos argumentos a print,
  # los imprime separados por un espacio (el f antes de las comillas no hace nada aquí)
  print(f"Targets: ", targets)
  # Muestra las predicciones actuales de la neurona
  print(f"Predictions: ", pred)
  # Muestra el error de cada predicción
  print(f"Errors: ", errors)
  # Muestra el peso actual con 10 decimales (.10f) y el costo con 6 decimales (.6f).
  # Las llaves {} insertan el valor de la variable dentro del texto
  print(f"Weight: {w: .10f}, Cost: {cost:.6f}")
  # Actualiza el peso: se le suma el costo multiplicado por la tasa de aprendizaje.
  # Si el costo es positivo (la neurona predice de menos), w sube; si es negativo, w baja
  w += learning_rate*cost
  # Muestra el peso ya actualizado, que se usará en la siguiente época
  print(f"Nuevo Peso: {w}")
  # Pausa de 1 segundo para poder ver con calma cada época en la consola
  time.sleep(1)

#Test the network:
# Entradas nuevas que la neurona nunca vio durante el entrenamiento
test_inputs = [5, 6]
# Respuestas correctas de esas entradas nuevas, para comparar
test_targets = [10, 12]
# Predicciones de la neurona para las entradas nuevas, usando el peso ya entrenado
pred = [predict(i) for i in test_inputs]
# zip junta de a tres: entrada, respuesta correcta y predicción.
# En cada vuelta i, t y p toman los valores de la misma posición de las tres listas
for i, t, p in zip(test_inputs, test_targets, pred):
  # Imprime la entrada, el valor correcto y la predicción con 4 decimales (.4f)
  print(f"input:{i}, target:{t}, pred:{p:.4f}")
