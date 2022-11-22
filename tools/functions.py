
import numpy as np
# setting random seed
np.random.seed(42)

### SIMULATION FUNCTIONS ###


def calculate_posterior(p, q, a, b):
    # calculate the posterior given...
    # probability of accepting given a #high and #low signals + yours
    numerator = p * ( (q**a) * ((1-q)**b) )
    denominator = numerator + (1-p) * ( ((1-q)**a) * (q**b) )
    posterior_prob = numerator / denominator
    return posterior_prob


def calculate_choice(posterior_prob):
    # based on posterior and prior, calculate agents choice
    # initialize
    choose_a = 0
    choose_b = 0

    # if posterior is larger
    if (posterior_prob > 0.5):
        # majority blue is approved
        choose_a = 1

    # if they are the same
    elif posterior_prob == 0.5:
        # if a tie, trust your own observation more
        choose_a = 1
        # the choice is 50/50
        #choice = np.random.binomial(1, 1/2, size=None)
        # todo: or choice = marble?
        #if choice == 1:
        #    choose_a = 1
        #else:
        #    choose_b = 1

    # else if less 1/2
    else:
        # majority red is approved
        choose_b = 1

    return choose_a, choose_b


def basic_simulation(n_simulations, n_agents, prior, signal_accuracy):
    # the basic simulation

    results = {}
    for sim in range(n_simulations):
        results[sim] = {}
        results[sim]['a'] = np.zeros(n_agents)
        results[sim]['ab'] = np.zeros(n_agents)
        a = 0
        b = 0
        for agent in range(n_agents):

            # draw a marble
            marble = np.random.binomial(1, signal_accuracy, size=None) # 2/3

            if marble == 1: # if e.g. the blue marble
                posterior_prob = calculate_posterior(prior, signal_accuracy, a+1, b) # add to obs
            else: # if e.g. the red marble
                posterior_prob = calculate_posterior(prior, signal_accuracy, a, b+1) # add to obs
            
            # calculating agents choice based on posterior and prior
            choose_a, choose_b = calculate_choice(posterior_prob)
            a += choose_a # 1 if chosen, 0 otherwise
            b += choose_b # 1 if chosen, 0 otherwise
            results[sim]['a'][agent] = choose_a
            results[sim]['ab'][agent] = choose_a -choose_b # this fluctuates, thus b is -1 if chosen


        results[sim]['a_cumsum'] = np.cumsum(results[sim]['a'])
        results[sim]['ab_cumsum'] = np.cumsum(results[sim]['ab'])

    return results



def independent_simulation(n_simulations, n_agents, n_independent, prior, signal_accuracy):
    # the independent simulation

    results = {}
    for sim in range(n_simulations):
        results[sim] = {}
        results[sim]['a'] = np.zeros(n_agents)
        results[sim]['ab'] = np.zeros(n_agents)
        a = 0
        b = 0
        for agent in range(n_agents):

            # draw a marble
            marble = np.random.binomial(1, signal_accuracy, size=None) # 2/3

            if(agent < n_independent):
                if(marble == 1): #if blue
                    choose_a, choose_b = 1, 0
                    a += choose_a
                else: #if red
                    choose_a, choose_b = 0, 1
                    b += choose_b
                results[sim]['a'][agent] = choose_a
                results[sim]['ab'][agent] = choose_a -choose_b # this fluctuates, thus b is -1 if chosen    
            else:
                if marble == 1: # if e.g. the blue marble
                    posterior_prob = calculate_posterior(prior, signal_accuracy, a+1, b) # add to obs
                else: # if e.g. the red marble
                    posterior_prob = calculate_posterior(prior, signal_accuracy, a, b+1) # add to obs
                
                
                # calculating agents choice based on posterior and prior
                choose_a, choose_b = calculate_choice(posterior_prob)
                a += choose_a # 1 if chosen, 0 otherwise
                b += choose_b # 1 if chosen, 0 otherwise
                results[sim]['a'][agent] = choose_a
                results[sim]['ab'][agent] = choose_a -choose_b # this fluctuates, thus b is -1 if chosen


        results[sim]['a_cumsum'] = np.cumsum(results[sim]['a'])
        results[sim]['ab_cumsum'] = np.cumsum(results[sim]['ab'])

    return results
