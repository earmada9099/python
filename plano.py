# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:41:44 2023

@author: Ezequiel
"""

import numpy as np
import matplotlib.pyplot as plt

def aceleracion_componente(angulo):
    # Gravedad
    g = 9.8  # m/s^2

    # Calcular la componente de la aceleración en el eje del desplazamiento
    aceleracion = g * np.sin(np.radians(angulo))

    return aceleracion

# Crear un rango de ángulos
angulos = np.arange(0, 91, 5)

# Calcular la aceleración para cada ángulo
aceleraciones = [aceleracion_componente(angulo) for angulo in angulos]

# Crear el gráfico
plt.figure(figsize=(8, 6))
plt.plot(angulos, aceleraciones, label='Componente de Aceleración')
plt.title('Variación de la Aceleración en un Plano Inclinado')
plt.xlabel('Ángulo del Plano Inclinado (grados)')
plt.ylabel('Aceleración (m/s^2)')
plt.legend()
plt.grid(True)
plt.show()