
from  tools import *



n_simutations = 100

n_agents = 10

prior = 1/2

signal_accuracy = 2/3


results = attention_simulation(n_simutations, n_agents, prior, signal_accuracy)


create_triple_plots(results, n_simutations, n_agents, np.round(signal_accuracy, 3))







