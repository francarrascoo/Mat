import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 30):
    x = 1000 * np.exp(0.1 * i)
    print (f"el valor {i} es: {x}")
