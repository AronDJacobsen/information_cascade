
from tools import *

np.random.seed(4)


n_simulations = 100
n_agents = 50
n_independents = [5, 20, 45, 50]
prior = 1/2
signal_accuracy = 2/3
save = False

for n_independent in n_independents:
    results = independent_simulation(n_simulations, n_agents, n_independent, prior, signal_accuracy)
    ratio = results['ratio']
    print(f'for {n_independent} the ratio is {ratio}')
    name = 'ind_exp_' + str(n_independent)
    create_double_plot(results, n_simulations, n_agents, np.round(signal_accuracy, 3), save, name)