import matplotlib.pyplot as plt

import numpy as np

x = np.arange(0, 45,0.01) #Rango de X

y = 200*x+700 #Función

plt.plot(x, y) #Gráfico de lineas x e y / Ejes

plt.axis([0, 45, 700, 9700]) # domino y recorrido

plt.xlabel('Energía utilizada (kWh)')# con un título eje x

plt.ylabel('Costo para usuario ($)')# y un título de eje y

plt.title('Costo para el usuario según uso de energía')# y un titulo del grafico

plt.grid()# pedimos mostrar una grilla para facilitar la lectura

plt.show()# y que nos muestre el gráfico