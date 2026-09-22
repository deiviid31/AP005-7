# for i in range (1,21):
#     residual = i%2
#     if residual == 0:
#         print(f'{i} is even')
#     else:
#         #print(f'{i} is odd')
#         print(str(i) + ' is odd')

# for i in range (0,6):
#     result = i**3
#     print(result)

times = input("Enter a number of times: ")  # Pide al usuario cuántas veces quiere repetir algo (llega como texto)
times = float(times)  # Convierte el valor ingresado a número decimal
times = int(times)  # Convierte el decimal a entero (trunca la parte decimal)
print(type(times))  # Imprime el tipo de dato de times (int)
print(times)  # Imprime el valor final de times

if times == 0:  # Si el usuario ingresó 0
    print("Don't do anything")  # No hace nada más, solo lo indica
else:
    for i in range(1,times+1):  # Recorre desde 1 hasta times
        print("i = ", i)  # Imprime el valor actual de i en cada iteración
