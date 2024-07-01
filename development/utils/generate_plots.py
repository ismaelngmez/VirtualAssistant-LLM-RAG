import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.figure(figsize=(10, 6))

# Generar datos de una distribución normal
mu = 0
sigma = 1
x = np.linspace(-4, 4, 100)
pdf = norm.pdf(x, mu, sigma)

# Representar la distribución normal teórica
plt.plot(x, pdf, color='gray', linewidth=5)

# Línea vertical en la media y predicción
plt.axvline(0, color='gray', linestyle='--', linewidth=1)
plt.axvline(0.5, color='orange', linestyle='-', linewidth=3)

# Añadir etiquetas
# plt.legend(['Distribución normal', 'Media'], loc='best')
plt.text(0.6, 0.1, 'x', color='orange')
plt.text(1.3, 0.2, 'f', color='gray')
plt.xticks([])  # Quitar etiquetas del eje x
plt.yticks([])  # Quitar etiquetas del eje y
plt.xlabel('Distribución de las observaciones')
plt.ylabel('Densidad de probabilidad')

# Mostrar la gráfica
plt.savefig('distribucion_normal.png')
plt.show()
