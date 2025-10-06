import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de x
x = np.linspace(-10, 10, 100)

# Definir dos funciones lineales
# f1(x) = 2x + 3
# f2(x) = -x + 5
y1 = 2 * x + 3
y2 = -1 * x + 5

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='f₁(x) = 2x + 3', color='blue', linewidth=2)
plt.plot(x, y2, label='f₂(x) = -x + 5', color='red', linewidth=2)

# Agregar detalles
plt.title('Gráfico de dos funciones lineales')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Mostrar la gráfica
plt.show()
