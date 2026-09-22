for i in range(100, 301):  # Recorre todos los números desde 100 hasta 300
    if (i%12) != 0:  # Si i no es divisible exactamente entre 12
        continue  # Salta a la siguiente iteración sin imprimir
    print(i)  # Si i es divisible entre 12, lo imprime
