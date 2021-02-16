import math
import matplotlib.pyplot as plt
import numpy as np

def my_func(x):
    return x / math.tan(x)

x = np.arange(-10, 10, 0.01)
# y = x / np.tan(x)
y = []
for i in x:
    y.append(my_func(i))
plt.plot(x, y)
plt.show()
