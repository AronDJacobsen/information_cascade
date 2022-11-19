from functions import *




n_simutations = 1000

n_agents = 100

prior = 1/2

signal_accuracy = 0.505


results = run_simulation(n_simutations, n_agents, prior, signal_accuracy)

for sim in range(n_simutations):
    plt.plot(results[sim]['a_cumsum'])
    plt.title(f"Signal accuracy = {signal_accuracy}")

plt.show()






