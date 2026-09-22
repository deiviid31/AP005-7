import time  # Importa el módulo time para poder usar time.sleep()

cadena = 'Python'  # Define la cadena de texto que se va a recorrer

for letra in cadena:  # Recorre cada letra de la cadena una por una
   if letra == 't':  # Si la letra actual es 't'
      continue  # Salta esta letra sin imprimirla ni esperar
   print(letra)  # Imprime la letra actual
   time.sleep(1)  # Espera 1 segundo antes de continuar con la siguiente letra
