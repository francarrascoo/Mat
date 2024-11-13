import numpy as np

peso= np.array([1.6, 1.92, 2.16, 2.56])

deformacion=np.array([2, 2.4, 2.7, 3.2])

pendiente, intercepto = np.polyfit(peso, deformacion, 1)

print (f'La pendiente es {round(pendiente,2)}')

print (f'(El coeficiente de posicion es {round(intercepto,2)})')