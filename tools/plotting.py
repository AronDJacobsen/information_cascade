
import numpy as np
# setting random seed
np.random.seed(42)
import matplotlib.pyplot as plt


### PLOTTING FUNCTIONS ###


def create_triple_plots(results, n_simutations, n_agents, signal_accuracy):
    #plt.style.use('ggplot')
    plt.style.use('seaborn-colorblind') # colors

    # info about data stored
    plot_types = {'a_cumsum': {'t': 'Cumulative approves', 'y': '# of approves'},
                  'ab_cumsum': {'t': 'Cumulative approves minus rejects', 'y': '# approve - rejects'},
                  'ab': {'t': 'Approves or rejects', 'y': 'approve or reject'}}

    n_subplots = len(plot_types.keys())
    fig, ax = plt.subplots(nrows=1, ncols=n_subplots, figsize=(9, 3))
    #fig.subplots_adjust(hspace=1)#, wspace=.2)


    for idx, plot_type in enumerate(plot_types):
        # subplot is (nrows, ncols, nidx)
        # defining subplot
        #ax[idx].subplot(n_subplots, 1, idx+1, figsize=(8, 8))
        # TODO: set limit on y axis based on num agents
        offset = np.linspace(-0.15,0.15, n_simutations)
        for sim in range(n_simutations):
            ax[idx].plot(results[sim][plot_type]+ offset[sim], linewidth=.3)
        #ax[idx].set_title(f"{plot_types[plot_type]['t']}\nSignal accuracy = {signal_accuracy}")
        #ax[idx].set_title(f"Signal accuracy: {signal_accuracy}")
        if plot_type == 'a_cumsum':
            ax[idx].set_ylim([0, n_agents])
        elif plot_type == 'ab_cumsum':
            ax[idx].set_ylim([-n_agents, n_agents])

        ax[idx].set_ylabel(plot_types[plot_type]['y'])
        ax[idx].set_xlabel('# agent in sequence')
    fig.suptitle(f"Signal accuracy: {signal_accuracy}")
    fig.tight_layout()
    plt.show()

    # TODO: save fig





