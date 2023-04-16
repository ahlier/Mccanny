import numpy as np
import matplotlib.pyplot as plt
import random

p = 0.4
step = 100
step_size = 1
initial_value = 100
trial = 100
return_multiplier = 2
record = []

for _ in range(trial):
    current_value = initial_value
    record.append([])
    for _ in range(step):
        if current_value <= 0:
            record[-1].append(0)
            continue

        outcome = np.random.choice([0, 1], 1, p=[1-p, p])

        current_value = current_value-step_size+return_multiplier*step_size*outcome
        record[-1].append(current_value)

for i in range(trial):
    plt.plot(np.arange(1, step+1), record[i])
plt.xlabel('number of round')
plt.ylabel('balance')
plt.title('Monte Carlo simulation on a game with p={}, \n'
          'return multiplier of {} over {} simulations'.
          format(p, return_multiplier, trial))
plt.show()


def draw_expected_return(record):
    matrix = np.array(record)
    ave = np.mean(matrix, axis=0)
    plt.plot(np.arange(1, step+1), ave)
    plt.xlabel('number of round')
    plt.ylabel('average balance')
    plt.title('average balance of {} simulations'.format(trial))
    plt.show()

draw_expected_return(record)
