from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-1.5, 1.5, 0.001)
def f(x):
    return x**3
y = f(x)

step = 100


for i in range(step):
    plt.clf()
    plt.plot(x+i*(y-x)/step, y+i*(x-y)/step)
    plt.plot(2*x, 2*x)
    plt.xlim((min(x[0], min(y)), max(x[-1], max(y))))
    plt.ylim((min(min(y), min(x)), max(max(y), max(x))))

    plt.pause(0.01)

plt.show()
