
from tools import *

np.random.seed(2)


n_simutalions = 100
n_agents = 50
prior = 1/2
signal_accuracies = [1/2, 2/3, 9/10]
save = True


for signal_accuracy in signal_accuracies:
    results = basic_simulation(n_simutalions, n_agents, prior, signal_accuracy)
    name = 'SA_exp_' + str(np.round(signal_accuracy, 3))
    create_double_plot(results, n_simutalions, n_agents, np.round(signal_accuracy, 3), save, name)







