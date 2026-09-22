a = 1  # Variable de control del ciclo while, empieza en 1 para entrar al bucle
value = input('Ingrese un valor')  # Pide al usuario un valor a evaluar (llega como texto)
value = int(value)  # Convierte el valor ingresado de texto a número entero

while a == 1:  # Ciclo que se repite mientras el usuario quiera seguir evaluando números (a == 1)
    for i in range(1,value+1):  # Recorre todos los números desde 1 hasta value
        conta = 0  # Contador de divisores de i, se reinicia en cada valor de i
        for n in range(1, i+1):  # Recorre todos los números desde 1 hasta i buscando divisores
            residue = i%n  # Calcula el residuo de dividir i entre n
            if residue == 0:  # Si el residuo es 0, n es divisor de i
                conta = conta + 1  # Incrementa el contador de divisores
            
            # print("i = ", i)
            # print("n = ", n)
            # print("residue = ", residue)
            # print("conta = ", conta)
    if conta == 2:  # Al salir del for interno, revisa si el último i evaluado tiene exactamente 2 divisores (nota: solo se evalúa el último i del rango, no cada uno)
       print(f'{i} es un primo')  # Imprime que ese número es primo
       print("\n")  # Imprime una línea en blanco para separar resultados
    else:
       print(f'{i} NOOO es un primo')  # Si no tiene exactamente 2 divisores, indica que no es primo
       print("\n")  # Imprime una línea en blanco para separar resultados

    print('Do you want to continue?. Press 1 to do that')  # Pregunta al usuario si desea continuar
    a = input()  # Lee la respuesta del usuario (texto)
    a = int(a)  # Convierte la respuesta a número entero

    if a != 1:  # Si la respuesta no es 1, el usuario no quiere continuar
        break  # Sale del ciclo while

    value = input('Ingrese un valor')  # Si continúa, pide un nuevo valor a evaluar
    value = int(value)  # Convierte el nuevo valor a entero
