for i in range(1,6):  # Recorre i desde 1 hasta 5 (aunque el ciclo se rompe en la primera iteración)
    while i <= 4:  # Mientras i sea menor o igual a 4
        i += 1  # Incrementa i en 1
        print(i)  # Imprime el nuevo valor de i
    break    # Rompe el ciclo for después de la primera iteración (por eso el for nunca llega a i=2,3,4,5)
