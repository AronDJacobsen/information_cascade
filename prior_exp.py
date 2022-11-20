
from  tools import *


iterations = 15
# taken from:
# https://web.stanford.edu/~clark/1990s/Mosteller,%20F.%20_%20Youtz,%20C.%20_Quantifying%20probabilistic%20expressions_%201990.pdf

priors = {'Always: 99%': 99/100,
          'Certain: 97%': 97/100,
          'Likely/Probable/Often: 69%': 69/100,
          'Frequent: 61%': 61/100,
          'Even chance: 50%': 50/100
          }

results = {}

for idx, prior in enumerate(list(priors.keys())):
    results[prior] = []
    # the question is, when will this agent also reject and go with the flow
    p = priors[prior]
    a = 1 # agent has observed a high signal
    # like the marble experiment
    q = 2/3 # probability of a high signal for e.g. majority blue
    # amount of low signals grows
    for b in range(iterations):
        # calculating probability of accepting given:
        #    - you private high signal, but #b low signals
        posterior_prob = calculate_posterior(p, q, a, b)
        choose_a, choose_b = calculate_choice(posterior_prob)
        # agent still approves that majority is blue
        if choose_a:
            results[prior].append(1)
        else:
            results[prior].append(-1)

# fluctuation plot:


fluctuation_plot(results)





