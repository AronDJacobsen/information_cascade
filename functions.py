
import numpy as np
import matplotlib.pyplot as plt

def posterior(p, q, a, b):
    numerator = p * ( (q**a) * ((1-q)**b) )
    denominator = numerator + (1-p) * ( ((1-q)**a) * (q**b) )
    posterior_prob = numerator / denominator
    return posterior_prob



def run_simulation(n_simutations, n_agents, prior, signal_accuracy):

    results = {}
    for sim in range(n_simutations):
        results[sim] = {}
        results[sim]['a'] = np.zeros(n_agents)
        results[sim]['ab'] = np.zeros(n_agents)
        a = 0
        b = 0
        for agent in range(n_agents):

            # draw a
            marble = np.random.binomial(1, signal_accuracy, size=None) # 2/3

            if marble == 1: # if e.g. the blue marble
                posterior_prob = posterior(prior, signal_accuracy, a+1, b)
            else: # if e.g. the red marble
                posterior_prob = posterior(prior, signal_accuracy, a, b+1)

            # if posterior is larger than the prior
            if (posterior_prob > prior):
                a += 1
                results[sim]['a'][agent] = 1
                results[sim]['ab'][agent] = 1

            # if they are the same
            elif posterior_prob == prior:
                # the choice is 50/50
                #  choice = np.random.binomial(1, 1/2, size=None)
                choice = marble
                if choice == 1:
                    a += 1
                    results[sim]['a'][agent] = 1
                    results[sim]['ab'][agent] = 1
                else:
                    b += 1
                    results[sim]['ab'][agent] = -1

            # if less than prior
            else:
                b += 1
                results[sim]['ab'][agent] = -1

        results[sim]['a_cumsum'] = np.cumsum(results[sim]['a'])
        results[sim]['ab_cumsum'] = np.cumsum(results[sim]['ab'])

    return results



def create_plots(results, plot_types, n_simutations, signal_accuracy):
    n_subplots = len(plot_types.keys())
    plt.style.use('seaborn-colorblind')
    fig, ax = plt.subplots(nrows=1, ncols=n_subplots, figsize=(9, 3))
    #fig.subplots_adjust(hspace=1)#, wspace=.2)


    for idx, plot_type in enumerate(plot_types):
        # subplot is (nrows, ncols, nidx)
        # defining subplot
        #ax[idx].subplot(n_subplots, 1, idx+1, figsize=(8, 8))
        # TODO: set limit on y axis
        for sim in range(n_simutations):
            ax[idx].plot(results[sim][plot_type])
        #ax[idx].set_title(f"{plot_types[plot_type]['t']}\nSignal accuracy = {signal_accuracy}")
        #ax[idx].set_title(f"Signal accuracy: {signal_accuracy}")
        ax[idx].set_ylabel(plot_types[plot_type]['y'])
        ax[idx].set_xlabel('# agent in sequence')
    fig.suptitle(f"Signal accuracy: {signal_accuracy}")
    fig.tight_layout()
    plt.show()





