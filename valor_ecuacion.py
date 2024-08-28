# Se llama a la biblioteca numpy, para trabajar con arreglos de datos

import numpy as np

# Modulo de la biblioteca scipy que nos permitirá poder resolver ecuaciones no necesariamente lineales
# a través de la función fsolve

from scipy.optimize import fsolve

# Se define la función C(e) y se retorna la expresión resultante del igualar a cero

def C(e):
    return 120*e+2000-68000

# Lo que retorna proviene del siguiente despeje:
# 120*e+\num{2000} = \num{68000}
# 120*e+\num{2000}\num{-68000} = 0

# Se le asigna a un arreglo t valores desde 0 hasta 1000 con un espacio de distancia. 
# Por lo tanto, este vector contiene solo el elemento 0

t = np.linspace(0, 10000, 1)

# Se le asigna a un arreglo sol, la(s) solución(es) entre la expresión retornada en def y el arreglo t.
# Como este ́ultimo arreglo contiene solo el elemento 0, entonces fsolve busca la solución entre
# la expresi ́on 120*e+2000-68000 y 0

sol = fsolve(C, t)

# Imprime en la consola el resultado obtenido del despeje de la ecuación

print(sol[0])