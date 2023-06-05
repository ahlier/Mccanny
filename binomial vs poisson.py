# This program compares how binomial and poisson distribution differ with the constant
# expected value, but different sample size n
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.stats import poisson, binom

miu = 20
n = 500
x = np.arange(0, n, 1)
fig, ax = plt.subplots()
p_poisson, = ax.plot(x, poisson.pmf(x, mu=miu), label='poisson')
p_binomial = ax.plot(x, binom.pmf(x, n, miu/n), label='binomial')
ax.set_xlim([0, 3*miu])  # we are only looking at changes around the center

ax.set_xlabel('x')
ax.set_ylabel('probability density')

# set slider position
fig.subplots_adjust(bottom=0.25)
n_ax = fig.add_axes([0.1, 0.1, 0.8, 0.03])

n_slider = Slider(ax=n_ax, label='n', valmin=miu, valmax=1000, valstep=1 ,valinit=n)

# This will change the binomial graph based on the slider output
def update(val):
    p_binomial[0].set_ydata(binom.pmf(x, val, miu/val))
    fig.canvas.draw_idle()

n_slider.on_changed(update)
ax.legend(loc='upper right')
ax.set_title('binomial vs poisson distribution with miu={}'.format(miu))
plt.show()