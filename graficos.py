import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 45,0.01) #Rango de X
y = 200*x+700 #Función

plt.plot(x, y) #Gráfico de lineas x e y / Ejes

plt.axis([0, 45, 700, 9700]) # Domino y recorrido

plt.xlabel('Energía utilizada (kWh)')# Con un título eje x

plt.ylabel('Costo para usuario ($)')# Y un título de eje y

plt.title('Costo para el usuario según uso de energía')# Y un titulo del grafico

plt.grid()# Pedimos mostrar una grilla para facilitar la lectura

plt.show()# y que nos muestre el gráfico