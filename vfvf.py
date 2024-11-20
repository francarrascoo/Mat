import numpy as np 

"""sum = 0
for i in range (1, 10):
    s = 2000000 * 1.012**(i)
    sum = sum + s
    print(f"mes {i} = {s}")
print(f"Suma = {sum}")"""

"""A = np.array([[2, 3], [1, 2]])
A_inv = np.linalg.inv(A)
print(A_inv)"""

"""A = np.array([[2, 1], 
            [3, -2]])

B = np.array([[10],[ 8]])

A_inv = np.linalg.inv(A)

print(A_inv)

K = A_inv @ B
print(K)"""

#Pregunta 5 - 6
# Una empresa de tecnología está optimizando sus servidores. Para ello, mide cada mes las transacciones por segundo (TPS) de sus servidores.
# Se ha obtenido que el segundo mes, el rendimiento del servidor es 1.066 TPS y el quinto mes, el rendimiento es de 8.528 TPS.

m2 = 1066
m5 = 8528
razon = (m5/m2)**(1/3)
print(razon)

#mn = m1 * r^(n-1)
a1 = m2/razon
print(a1)

for i in range(1, 13):
    s = a1 * razon**(i-1)
    print(f"mes {i} = {s}")
    if s == 136192:
        print(f"El mes en el que el rendimiento fue de 136.192 TPS fue el mes {i}")
        break

#Pregunta 7
# Un local comercial se arrendó por 2 años y durante ese periodo, 
# el valor del arriendo se incrementó todos los meses en una cantidad constante. 
# En el cuarto mes, el valor del arriendo fue $1.108.000 y en el décimo segundo mes el valor del arriendo fue $1.396.000.

m4 = 1108000
m12 = 1396000
constante = (m12-m4)/(12-4)

#an = a1 + (n-1)d
a1 = m4 -3*constante
print(a1)

for i in range(1, 25):
    s = a1 + (i-1)*constante
    print(f"mes {i} = {s}")
    if s == 1828000:
        print(f"El mes en el que el arriendo fue de $1.828.000 fue el mes {i}")
        break

