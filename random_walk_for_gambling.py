import numpy as np
import matplotlib.pyplot as plt
import random
'''
This program shows why gambler will always tend to lose all their money, it uses
random walk model to show how a person's money change over rounds of games
'''

def random_walk(starting_fund=1000, bet_per_round=20, p=0.5, winning_multipler=2):
    '''

    :param starting_fund: how much money the gambler starts with
    :param bet_per_round: how much is he betting per round
    :param p: probability of winning
    :param winning_multipler: what is the ratio between how much he can win per
    round and the capital he puts in
    :return: it will return a list and each element in the list means how much
    he has left after each round
    '''
    winning = winning_multipler * bet_per_round
    betting = True
    fund = [starting_fund]

    while betting:
        result = random.choices([0, 1], weights=[1-p, p], k=1)
        fund.append(fund[-1] - bet_per_round + result[0] * winning)
        if fund[-1] <= 0:
            betting = False

    return fund


def draw_random_walk(fund=random_walk()):
    plt.plot(np.arange(len(fund)), fund)
    plt.show()


def expected_round():
    num_round = []
    for _ in range(100):
        num_round.append(len(random_walk()))
    return np.mean(num_round), np.std(num_round)

draw_random_walk()
