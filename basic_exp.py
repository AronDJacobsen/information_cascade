from functions import *




n_simutations = 1000

n_agents = 40

prior = 1/2

signal_accuracy = 2/3


results = run_simulation(n_simutations, n_agents, prior, signal_accuracy)


# number of plots
plots = len(results[0].keys())

plot_types ={'a_cumsum': {'t': 'Cumulative approves', 'y':'# of approves'},
             'ab_cumsum': {'t':'Cumulative approves minus rejects', 'y':'# approve - rejects'},
            'ab': {'t':'Approves or rejects', 'y': 'approve or reject'}}

create_plots(results, plot_types, n_simutations, np.round(signal_accuracy, 3))







