
import numpy as np
# setting random seed
np.random.seed(42)

### SIMULATION FUNCTIONS ###


def posterior(p, q, a, b):
    # calculate the posterior given...
    numerator = p * ( (q**a) * ((1-q)**b) )
    denominator = numerator + (1-p) * ( ((1-q)**a) * (q**b) )
    posterior_prob = numerator / denominator
    return posterior_prob


def update_variables(results, sim, agent, posterior_prob, prior, a, b):
    # based on posteror, calculate agents choice

    # if posterior is larger than the prior
    if (posterior_prob > prior):
        # majority blue is approved
        a += 1
        results[sim]['a'][agent] = 1
        results[sim]['ab'][agent] = 1

    # if they are the same
    elif posterior_prob == prior:
        # the choice is 50/50
        choice = np.random.binomial(1, 1/2, size=None)

        # todo: or choice = marble?

        if choice == 1:
            a += 1
            results[sim]['a'][agent] = 1
            results[sim]['ab'][agent] = 1
        else:
            b += 1
            results[sim]['ab'][agent] = -1

    # if less than prior
    else:
        # majority red is approved
        b += 1
        results[sim]['ab'][agent] = -1


    return results, a, b


def basic_simulation(n_simutations, n_agents, prior, signal_accuracy):
    # the basic simulation

    results = {}
    for sim in range(n_simutations):
        results[sim] = {}
        results[sim]['a'] = np.zeros(n_agents)
        results[sim]['ab'] = np.zeros(n_agents)
        a = 0
        b = 0
        for agent in range(n_agents):

            # draw a marble
            marble = np.random.binomial(1, signal_accuracy, size=None) # 2/3

            if marble == 1: # if e.g. the blue marble
                posterior_prob = posterior(prior, signal_accuracy, a+1, b) # add to obs
            else: # if e.g. the red marble
                posterior_prob = posterior(prior, signal_accuracy, a, b+1) # add to obs


            results, a, b = update_variables(results, sim, agent, posterior_prob, prior, a, b)


        results[sim]['a_cumsum'] = np.cumsum(results[sim]['a'])
        results[sim]['ab_cumsum'] = np.cumsum(results[sim]['ab'])

    return results




