
from tools import *



n_simutalions = 100
n_agents = 50
n_independents = [10, 20, 30]
prior = 1/2
signal_accuracy = 2/3
save = False

for n_independent in n_independents:
    results = independent_simulation(n_simutalions, n_agents, n_independent, prior, signal_accuracy)
    name = 'ind_exp_' + str(n_independent)
    create_double_plot(results, n_simutalions, n_agents, np.round(signal_accuracy, 3), save, name)