
import numpy as np
import matplotlib.pyplot as plt

def posterior(p, q, a, b):
    numerator = p * (q**a) * ((1-q)**b)
    denominator = p * (q**a) * ((1-q)**b) + (1-p) * ((1-q)**a) * (q**b)
    posterior_prob = numerator / denominator
    return posterior_prob






def run_simulation(n_simutations, n_agents, prior, signal_accuracy):

    results = {}
    for sim in range(n_simutations):
        results[sim] = {}
        results[sim]['a'] = np.zeros(n_agents)
        results[sim]['ab'] = np.zeros(n_agents)
        a = 0
        b = 0
        for idx, agent in enumerate(range(n_agents)):

            marble = np.random.binomial(1, signal_accuracy, size=None) # 2/3
            if marble == 1:
                posterior_prob = posterior(prior, signal_accuracy, a+1, b)
            else:
                posterior_prob = posterior(prior, signal_accuracy, a, b+1)

            if (posterior_prob >= prior):
                a += 1
                results[sim]['a'][idx] = 1
                results[sim]['ab'][idx] = 1
            else:
                b += 1
                results[sim]['ab'][idx] = -1

        results[sim]['a_cumsum'] = np.cumsum(results[sim]['a'])
        results[sim]['ab_cumsum'] = np.cumsum(results[sim]['ab'])

        #print("Simulation", sim, "marble was")

    return results




