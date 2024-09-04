from scipy.optimize import fsolve

def despeje_funcion (x, cantidad_visitas):
    return 300*x + 500 - cantidad_visitas

def calcular_campañas(cantidad_visitas):
    x = 0
    solucion = fsolve(despeje_funcion, x, args=cantidad_visitas)
    return solucion

cantidad_visitas = 500
print (calcular_campañas(cantidad_visitas))

