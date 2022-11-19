from functions import *




n_simutations = 1000

n_agents = 100

prior = 1/2

signal_accuracy = 2/3


results = run_simulation(n_simutations, n_agents, prior, signal_accuracy)

for sim in range(n_simutations):
    plt.plot(results[sim]['a_cumsum'])

plots = 0


plt.title(f"Signal accuracy = {signal_accuracy}")
plt.ylabel('# of approves')
plt.xlabel('# agent in sequence')
plt.show()






