
import numpy as np
# setting random seed
import matplotlib.pyplot as plt


### PLOTTING FUNCTIONS ###


def create_triple_plot(results, n_simutations, n_agents, signal_accuracy):
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

    fig.suptitle(f"q: {signal_accuracy}  | #Simulations: {n_simutations}")
    fig.tight_layout()
    plt.show()
    # TODO: save fig




def create_double_plot(results, n_simutations, n_agents, signal_accuracy, save, name):
    #plt.style.use('ggplot')
    plt.style.use('seaborn-colorblind') # colors

    # info about data stored
    plot_types = {'ab_cumsum': {'t': 'Cumulative of approve vs. reject', 'y': '#approves - #rejects'},
                  'ab': {'t': 'Approve vs. reject fluctuations', 'y': 'approve or reject'}}

    n_subplots = len(plot_types.keys())
    fig, ax = plt.subplots(nrows=1, ncols=n_subplots, figsize=(9, 3))
    #fig.subplots_adjust(hspace=1)#, wspace=.2)


    for idx, plot_type in enumerate(plot_types):
        # subplot is (nrows, ncols, nidx)
        # defining subplot
        # creating offset for lines to make them more visible
        offset = np.linspace(-0.15,0.15, n_simutations)
        for sim in range(n_simutations):
            ax[idx].plot(results[sim][plot_type] + offset[sim], linewidth=.3)
        # set title for each subplot?
        ax[idx].set_title(f"{plot_types[plot_type]['t']}")

        # plots specifications
        if plot_type == 'ab_cumsum':
            ax[idx].set_ylim([-n_agents-1, n_agents+1])
            # creating offset for lines to make them more visible
            offset = np.linspace(-3/4, 3/4, n_simutations)
            for sim in range(n_simutations):
                ax[idx].plot(results[sim][plot_type] + offset[sim], linewidth=.3)
            # if independent experiment
            ax[idx].axhline(y=0, color='grey', linestyle='--')#, linewidth=.3)
        elif plot_type == 'ab':
            # creating offset for lines to make them more visible
            offset = np.linspace(-0.15, 0.15, n_simutations)
            for sim in range(n_simutations):
                ax[idx].plot(results[sim][plot_type] + offset[sim], linewidth=.3)
            ax[idx].set_yticks([-1, 1])
            ax[idx].set_yticklabels(['reject', 'approve'])
        ax[idx].set_ylabel(plot_types[plot_type]['y'])
        ax[idx].set_xlabel('# agent in sequence')

    #fig.suptitle(f"q: {signal_accuracy}  | #Simulations: {n_simutations}")
    fig.tight_layout()
    if save:
        plt.savefig(f'results/{name}.png', dpi=200)
    else:
        plt.show()



def fluctuation_plot(results, save, name):
    plt.style.use('seaborn-colorblind') # colors

    offset = -1*np.linspace(-0.05, 0.05, len(results.keys()))
    for idx, prior in enumerate(list(results.keys())):
        plt.plot(results[prior] + offset[idx], label=prior)
        #, linewidth=.4
    # plotting lines
    # just taking the last prior
    xcoords = list(range(len(results[prior])))
    for xc in xcoords:
        plt.axvline(x=xc, color='grey', lw=0.2)
    plt.yticks([-1, 1], ['reject', 'approve'])
    plt.title('Conformity of agent based on prior belief  |  q=2/3')
    plt.ylabel('Choice of agent')
    plt.xlabel('# rejects from other agents')
    plt.legend()
    plt.tight_layout()
    if save:
        plt.savefig(f'results/{name}.png')
    else:
        plt.show()







