import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import special
import time


def C(n, r):
    return special.factorial(n)/(special.factorial(n-r)*special.factorial(r))


def binomial(r, n, p):
    return C(n, r)*p**r*(1-p)**(n-r)


def normal(x, sigma, miu):
    return np.e**(-0.5*((x-miu)/sigma)**2)/(sigma*np.sqrt(2*np.pi))


def draw_binomial(n = 100, p = 1/6):
    p_lst = []
    for i in range(n):
        p_lst.append(binomial(i, n, p))
    popt, pcov = curve_fit(normal, np.arange(n), p_lst)
    plt.plot(np.arange(n*10)/10, normal(np.arange(n*10)/10, *popt))
    plt.hist(np.arange(n), weights=p_lst, bins=n, rwidth=0.9)
    plt.show()




