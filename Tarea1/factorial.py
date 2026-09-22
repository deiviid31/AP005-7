while True:  # Ciclo infinito que se repite indefinidamente (aquí nunca se rompe con break)

    value = int(input("Enter a positive integer value: "))  # Pide un número al usuario y lo convierte a entero
    print("Value: ", value)  # Imprime el valor ingresado
    a = isinstance(value, int)  # Verifica si value es de tipo entero (siempre True porque ya se convirtió con int())
    if a == True and value > 0:  # Si value es entero y además es positivo
        fact = 1  # Inicializa el factorial en 1
        for i in range (1, value + 1):  # Recorre los números desde 1 hasta value
            fact = fact*i            # Multiplica el factorial acumulado por i en cada paso
        print(f'The factorial of {value} is: ', fact)  # Imprime el resultado del factorial
    else:
        print("Please, enter a positive integer number")  # Si no es positivo, pide un valor válido
