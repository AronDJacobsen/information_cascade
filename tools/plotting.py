
import numpy as np
# setting random seed
np.random.seed(42)
import matplotlib.pyplot as plt


### PLOTTING FUNCTIONS ###


def create_triple_plots(results, n_simutations, n_agents, signal_accuracy):
    #plt.style.use('ggplot')
    plt.style.use('seaborn-colorblind') # colors

    # info about data stored
    plot_types = {'a_cumsum': {'t': 'Cumulative approves', 'y': '#approves'},
                  'ab_cumsum': {'t': 'Cumulative approves - rejects', 'y': '#approve - #rejects'},
                  'ab': {'t': 'Approve/reject fluctuations', 'y': 'approve or reject'}}

    n_subplots = len(plot_types.keys())
    fig, ax = plt.subplots(nrows=1, ncols=n_subplots, figsize=(9, 3))
    #fig.subplots_adjust(hspace=1)#, wspace=.2)


    for idx, plot_type in enumerate(plot_types):
        # subplot is (nrows, ncols, nidx)
        # defining subplot
        # creating offset for lines to make them more visible
        offset = np.linspace(-0.15,0.15, n_simutations)
        for sim in range(n_simutations):
            ax[idx].plot(results[sim][plot_type]+ offset[sim], linewidth=.4)
        # set title for each subplot?
        ax[idx].set_title(f"{plot_types[plot_type]['t']}")

        # plots specifications
        if plot_type == 'a_cumsum':
            # setting limits so more comparable and visible
            ax[idx].set_ylim([-0.25, n_agents+0.25])
        elif plot_type == 'ab_cumsum':
            ax[idx].set_ylim([-n_agents-0.25, n_agents+0.25])
        elif plot_type == 'ab':
            ax[idx].set_yticks([-1, 1])
            ax[idx].set_yticklabels(['reject', 'approve'])

        ax[idx].set_ylabel(plot_types[plot_type]['y'])
        ax[idx].set_xlabel('# agent in sequence')

    fig.suptitle(f"Signal accuracy: {signal_accuracy}  | #Simulations: {n_simutations}")
    fig.tight_layout()
    plt.show()
    # TODO: save fig


def fluctuation_plot(results):
    offset = -1*np.linspace(-0.05, 0.05, len(results.keys()))
    for idx, prior in enumerate(list(results.keys())):
        plt.plot(results[prior] + offset[idx], label=prior)
        #, linewidth=.4
    plt.yticks([-1, 1], ['reject', 'approve'])
    plt.title('Strong-prior agents choice fluctuations')
    plt.ylabel('current agent approves or rejects')
    plt.xlabel('# rejects from other agents')
    plt.legend()
    plt.tight_layout()
    plt.show()





