import random  # Importa el módulo random para generar números aleatorios
from matplotlib import pyplot as plt  # Importa pyplot de matplotlib para graficar, renombrado como plt

# Add your code below:
numbers_a = range(1, 13)  # Crea un rango de números del 1 al 12 (eje x, por ejemplo los 12 meses)
numbers_b = [random.randint(1, 1000) for i in range(12)]  # Genera una lista de 12 números aleatorios entre 1 y 1000 (eje y)
plt.plot(numbers_a, numbers_b)  # Grafica numbers_a contra numbers_b como una línea
plt.show()  # Muestra la ventana con la gráfica
