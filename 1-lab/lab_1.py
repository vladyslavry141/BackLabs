import math
import matplotlib.pyplot as plt
import numpy as np


def my_func(x):
    if x is None:
        return None
    tanx = math.tan(x)
    if tanx == 0:
        return math.cos(x)
    else:
        return x / math.tan(x)

def special_range(start, end, step):
    if start >= end:
        raise Exception("End should be bigger then start")
    if step <= 0:
        raise Exception("Step should be non negative")
    result = []
    i = start
    pi_point = math.ceil(start / np.pi) * np.pi
    if pi_point == 0.0:
        pi_point = np.pi
    while i < end:
        result.append(i)
        if (pi_point - i) < step:
            result.append(None)
            pi_point += np.pi
            if pi_point == 0.0:
                pi_point = np.pi
        i += step
    return result

start = float(input("Enter the beginning of the interval    "))
end = float(input("Enter the end of the interval    "))
step = float(input("Enter a tab step    "))
x = special_range(start, end, step)
y = list(map(my_func, x))
high = abs(start - end)
plt.axis([start, end, - high/2 - 3, high/2 + 3])
plt.grid(True)
plt.plot(x, y)
plt.show()