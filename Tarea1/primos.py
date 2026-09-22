import time  # Importa el módulo time para medir el tiempo de ejecución
inicio = time.time()  # Guarda el tiempo actual (marca de inicio) para medir cuánto tarda el programa

for i in range(0,31):  # Recorre todos los números desde 0 hasta 30 (i es el número a evaluar)
    conta = 0  # Contador de divisores de i, se reinicia en cada iteración
    for n in range(1, i+1):  # Recorre todos los números desde 1 hasta i para buscar divisores
        residue = i%n  # Calcula el residuo de dividir i entre n
        if residue == 0:  # Si el residuo es 0, significa que n es divisor de i
            conta = conta + 1  # Incrementa el contador de divisores
              
    if conta == 2:  # Si i tiene exactamente 2 divisores (1 y sí mismo), es primo
        print(f'{i} es un primo')  # Imprime el número que resultó ser primo
        
fin = time.time()  # Guarda el tiempo actual (marca de fin) al terminar el cálculo
print("t = ", (fin - inicio)*1000)  # Imprime el tiempo transcurrido en milisegundos
