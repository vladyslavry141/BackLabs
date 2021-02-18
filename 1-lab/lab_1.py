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


def print_table (x, y):
    print('{:<30} {:<30}'.format('x', 'f(x)'))
    for i in range(len(x)):
        if(x[i] is None):
            continue	
        print('{:<30} {:<30}'.format(x[i], y[i]))	


def spec_point_for_X (start, end):
    points = []
    pi2_point = math.ceil(start / (np.pi/2)) * (np.pi/2)
    if pi2_point % np.pi == 0:
        pi2_point += np.pi/2
    while pi2_point < end:
        points.append(pi2_point)
        pi2_point += np.pi	
    return points


def print_spec_points_for_X (spec_for_X):
    if len(spec_for_X) > 0:
        print("Special points for X:")
        print('{:<30} {:<30}'.format('x', 'f(x)'))
        for i in range(len(spec_for_X)):
            print('{:<30} {:<30}'.format(spec_for_X[i], 0))	
    else:
        print("No special point for X")


def print_spec_points_for_Y(start, end):
    if start <= 0 and end > 0:
        print("Special points for Y:")	
        print('{:<30} {:<30}'.format('x', 'f(x)'))
        print('{:<30} {:<30}'.format(0, 1))
    else:
        print("No special point for Y")		
				
		
start = float(input("Enter the beginning of the interval    "))
end = float(input("Enter the end of the interval    "))
step = float(input("Enter a tab step    "))
x = special_range(start, end, step)
y = list(map(my_func, x))
high = abs(start - end)
print_table(x, y)
spec_for_X = spec_point_for_X(start, end)
print_spec_points_for_X(spec_for_X)
print_spec_points_for_Y(start, end)
plt.axis([start, end, - high/2 - 3, high/2 + 3])
plt.grid(True)
plt.plot(x, y)
plt.show()