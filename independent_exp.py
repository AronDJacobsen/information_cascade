
from  tools import *



n_simutalions = 100

n_agents = 50

n_independent = 10

prior = 1/2

signal_accuracy = 2/3


results = independent_simulation(n_simutalions, n_agents, n_independent, prior, signal_accuracy)


create_triple_plots(results, n_simutalions, n_agents, np.round(signal_accuracy, 3))