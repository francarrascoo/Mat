import numpy as np

print ("SUMA")
A = np.array([[1, 2, 3],
[4, 5, 6]])

B = np.array([[11, 12, 13],
[14, 15, 16]])

C = A + B
print(C)

print ("RESTA")
A = np.array([[1, 2, 3],
[4, 5, 6]])

B = np.array([[11, 12, 13],
[14, 15, 16]])

C = B-A
print(C)

#PONDERACIÓN
A = np.array([[1, 2, 3],
[4, 5, 6]])

B = np.array([[11, 12, 13],
[14, 15, 16]])

C = 2*A #Ponderamos por el Doble La matriz A
D = 1.2*A #Ponderamos por el 120% la Matriz A

print(f"PONDERACIÓN C \n{C}")
print(f"PONDERACIÓN D \n{D}")