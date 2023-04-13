import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import special
'''
This program can draw binomial, poisson and normal distribution
'''


def C(n, r):
    return special.factorial(n)/(special.factorial(n-r)*special.factorial(r))


def binomial(r, n, p):
    return C(n, r)*p**r*(1-p)**(n-r)


def normal(x, sigma, miu):
    return np.e**(-0.5*((x-miu)/sigma)**2)/(sigma*np.sqrt(2*np.pi))


def poisson(x, EV):
    return (EV**x)*(np.e**-EV)/(special.factorial(x))


def draw_binomial(n = 100, p = 1/6):
    p_lst = []
    for i in range(n):
        p_lst.append(binomial(i, n, p))
    popt, pcov = curve_fit(normal, np.arange(n), p_lst)
    plt.plot(np.arange(n*10)/10, normal(np.arange(n*10)/10, *popt))
    plt.hist(np.arange(n), weights=p_lst, bins=n, rwidth=0.9)
    plt.title('binomial distribution')
    plt.show()


def draw_poisson(x, EV):
    plt.plot(x, poisson(x, EV))
    plt.title('poisson distribution')
    plt.show()


def draw_normal(sigma, miu, start=0, end=100):
    plt.plot(np.arange(start, end, 0.1), normal(np.arange(start, end, 0.1), sigma, miu))
    plt.title('normal distribution')
    plt.show()

