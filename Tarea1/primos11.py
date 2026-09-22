import time  # Importa el módulo time para medir el tiempo de ejecución
inicio = time.time()  # Guarda el tiempo actual (marca de inicio)

for i in range(1,31):  # Recorre los números del 1 al 30 (i es el número a evaluar)
    conta = 0  # Contador de divisores de i, se reinicia en cada iteración
    for n in range(1, i+1):  # Recorre los números del 1 hasta i buscando divisores
        residue = i%n  # Calcula el residuo de dividir i entre n
        if residue == 0:  # Si el residuo es 0, n es divisor de i
            conta = conta + 1  # Incrementa el contador de divisores              
    if conta == 2:  # Si i tiene exactamente 2 divisores, es primo
        print(f'{i} es un primo')  # Imprime el número primo encontrado
        print("\n")  # Imprime una línea en blanco para separar resultados

fin = time.time()  # Guarda el tiempo actual (marca de fin)
print("t = ", (fin - inicio)*1000)  # Imprime el tiempo transcurrido en milisegundos
