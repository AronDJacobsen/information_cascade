
from tools import *

np.random.seed(4)


n_simulations = 100
n_agents = 50
prior = 1/2
signal_accuracies = [1/2, 1/2+1/1000000, 2/3, 9/10]
save = True


for signal_accuracy in signal_accuracies:
    results = basic_simulation(n_simulations, n_agents, prior, signal_accuracy)
    ratio = results['ratio']
    print(f'for {str(np.round(signal_accuracy, 3))} the ratio is {ratio}')
    name = 'SA_exp_' + str(np.round(signal_accuracy, 8))
    create_double_plot(results, n_simulations, n_agents, np.round(signal_accuracy, 3), save, name)






