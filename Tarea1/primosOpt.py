# 9) Imprimir los números primos existentes entre 0 y 30
tope_rango=30  # Define el límite superior del rango a evaluar (30)
n = 0  # Número que se va a evaluar, empieza en 0
primo = True  # Bandera que indica si n es primo, se asume primo al inicio
while (n < tope_rango):  # Repite mientras n sea menor que el tope del rango
    for div in range(2, n):  # Prueba divisores desde 2 hasta n-1
        if (n % div == 0):  # Si div divide exactamente a n
            primo = False  # n no es primo, se marca la bandera en False
    if (primo):  # Si al terminar el for la bandera sigue en True
        print(n)  # Imprime n porque es primo
    else:
        primo = True  # Reinicia la bandera a True para el siguiente número
    n += 1  # Incrementa n para evaluar el siguiente número


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
n = 0  # Reinicia n en 0 para esta segunda versión optimizada
primo = True  # Bandera que indica si n es primo
while (n < tope_rango):  # Repite mientras n sea menor que el tope del rango
    for div in range(2, n):  # Prueba divisores desde 2 hasta n-1
        if (n % div == 0):  # Si div divide exactamente a n
            primo = False  # n no es primo
            break  # Corta el ciclo for apenas se encuentra un divisor (optimización)
    if (primo):  # Si la bandera sigue en True, n es primo
        print(n)  # Imprime n
    else:
        primo = True  # Reinicia la bandera para el siguiente número
    n += 1  # Incrementa n

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
ciclos_sin_break = 0  # Contador de iteraciones del for sin usar break
n = 0  # Reinicia n en 0
primo = True  # Bandera de primalidad
while (n < tope_rango):  # Repite mientras n sea menor que el tope del rango
    for div in range(2, n):  # Prueba divisores desde 2 hasta n-1
        ciclos_sin_break += 1  # Cuenta cada iteración del for (sin break)
        if (n % div == 0):  # Si div divide exactamente a n
            primo = False  # n no es primo
    if (primo):  # Si la bandera sigue en True
        print(n)  # Imprime n porque es primo
    else:
        primo = True  # Reinicia la bandera
    n += 1  # Incrementa n
print('Cantidad de ciclos: ' + str(ciclos_sin_break))  # Muestra cuántas iteraciones tomó sin break


ciclos_con_break = 0  # Contador de iteraciones del for usando break
n = 0  # Reinicia n en 0
primo = True  # Bandera de primalidad
while (n < tope_rango):  # Repite mientras n sea menor que el tope del rango
    for div in range(2, n):  # Prueba divisores desde 2 hasta n-1
        ciclos_con_break += 1  # Cuenta cada iteración del for (con break)
        if (n % div == 0):  # Si div divide exactamente a n
            primo = False  # n no es primo
            break  # Corta el ciclo apenas encuentra un divisor
    if (primo):  # Si la bandera sigue en True
        print(n)  # Imprime n porque es primo
    else:
        primo = True  # Reinicia la bandera
    n += 1  # Incrementa n
print('Cantidad de ciclos: ' + str(ciclos_con_break))  # Muestra cuántas iteraciones tomó con break
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')  # Calcula y muestra la proporción de ciclos ahorrados

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
tope_rango=100  # Aumenta el límite del rango a 100 para comparar la optimización a mayor escala
ciclos_sin_break = 0  # Reinicia el contador de ciclos sin break
n = 0  # Reinicia n en 0
primo = True  # Bandera de primalidad
while (n < tope_rango):  # Repite mientras n sea menor que el nuevo tope (100)
    for div in range(2, n):  # Prueba divisores desde 2 hasta n-1
        ciclos_sin_break += 1  # Cuenta cada iteración del for (sin break)
        if (n % div == 0):  # Si div divide exactamente a n
            primo = False  # n no es primo
    if (primo):  # Si la bandera sigue en True
        print(n)  # Imprime n porque es primo
    else:
        primo = True  # Reinicia la bandera
    n += 1  # Incrementa n
print('Cantidad de ciclos: ' + str(ciclos_sin_break))  # Muestra cuántas iteraciones tomó sin break con tope=100

ciclos_con_break = 0  # Reinicia el contador de ciclos con break
n = 0  # Reinicia n en 0
primo = True  # Bandera de primalidad
while (n < tope_rango):  # Repite mientras n sea menor que el nuevo tope (100)
    for div in range(2, n):  # Prueba divisores desde 2 hasta n-1
        ciclos_con_break += 1  # Cuenta cada iteración del for (con break)
        if (n % div == 0):  # Si div divide exactamente a n
            primo = False  # n no es primo
            break  # Corta el ciclo apenas encuentra un divisor
    if (primo):  # Si la bandera sigue en True
        print(n)  # Imprime n porque es primo
    else:
        primo = True  # Reinicia la bandera
    n += 1  # Incrementa n
print('Cantidad de ciclos: ' + str(ciclos_con_break))  # Muestra cuántas iteraciones tomó con break con tope=100
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')  # Calcula y muestra la proporción de ciclos ahorrados con el rango más grande
