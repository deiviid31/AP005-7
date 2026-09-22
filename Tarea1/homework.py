a = input("Enter a number: ")  # Pide un número al usuario (se recibe como texto)
a = int(a)  # Convierte el valor de a a entero
b = input("Enter b number: ")  # Pide otro número al usuario (como texto)
b = float(b)  # Convierte el valor de b a número decimal (float)
c = a + b  # Suma a y b (Python convierte automáticamente el entero a float para la suma)

if a == b:  # Compara si a y b tienen el mismo valor numérico
    print("equal")  # Si son iguales, lo indica
else:
    print("Different")  # Si son diferentes, lo indica

print("Type of a is: ", type(a))  # Imprime el tipo de dato de a (int)
print("Type of b is: ", type(b))  # Imprime el tipo de dato de b (float)
print("c = ", c)  # Imprime el resultado de la suma

if type(a) == type(b):  # Compara si a y b son del mismo tipo de dato
    print("a and b are of the same type")  # Si tienen el mismo tipo, lo indica
else:
    print("a and b are of different type")  # Como a es int y b es float, siempre serán de tipos diferentes
