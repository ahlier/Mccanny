from distribution import C, normal, poisson
import numpy as np
import matplotlib.pyplot as plt
import random
'''
This program will show you visually how the central limit theorem work, it will 
first generate data points for the population with given population size and 
type of population distribution. Then the program will graph out the population
and then do an animation of how the sampling distribution is created 
'''

# mean and standard derivation of the population
miu = 10
sigma = 2

population_size = 1000
sample_size = 30
sampling_distribution = []

generate = True
population = []
distribution_type = int(input('population distribution: 1-random, 2-binomial, '
                              '3-normal, 4-uniform, 5-poisson'))

'''
The following while loop will keep generating random number for population 
based on the type of distribution you put in, and will exist the loop when the 
size of population is large enough
'''
while generate:
    x = np.random.uniform(max(0, miu - 3 * sigma), miu + 3 * sigma)
    y = np.random.random()

    if distribution_type == 1 or distribution_type == 4:
        population.append(x)
        if distribution_type == 1:
            title = 'random'
        else:
            title = 'uniform'

    elif distribution_type == 2:
        p = 0.2
        population = list(np.random.binomial(population_size+1, p, population_size))
        title = 'binomial'

    elif distribution_type == 3:
        if normal(x, sigma, miu) > y:
            population.append(x)
        title = 'normal'

    elif distribution_type == 5:
        p = poisson(np.arange(population_size+1), miu)
        population = random.choices(np.arange(population_size+1), weights=p, k=population_size)
        title = 'poisson'

    if len(population) == population_size:
        generate = False

plt.hist(population, rwidth=0.9, density=True, bins=int(np.sqrt(len(population))))
plt.title('{} population distribution'.format(title))
plt.show()

sigma_sample_mean = np.std(population)/np.sqrt(sample_size)
miu = np.mean(population)


'''
following will create a sampling distribution over 2000 trials
'''

for i in range(2000):
    sampling_distribution.append(np.mean(random.sample(population, sample_size)))

    plt.hist(sampling_distribution, rwidth=0.9, density=True,
             bins=int(np.sqrt(len(sampling_distribution))))
    plt.xlim(xmin=max(miu-4*sigma_sample_mean, 0),
             xmax=miu+4*sigma_sample_mean)
    plt.draw()
    plt.title('sampling distribution')
    plt.legend(['trial={}'.format(i)], loc='upper left')
    plt.pause(0.0001)
    plt.clf()

