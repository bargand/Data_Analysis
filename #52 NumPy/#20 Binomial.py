from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''
@ n = 10 → Number of trials per experiment
@ This means that each single experiment involves 10 independent trials.
@ Think of each trial like flipping a coin.
@ In each trial, an outcome can be either a success (e.g., getting heads) or a failure (e.g., getting tails).
@ So, with n=10, each experiment simulates 10 coin flips.
@ The result of each experiment is how many times success occurred out of those 10.
@ 🧠 Analogy: Suppose you toss a coin 10 times — how many times will it land heads? That's what this parameter sets.


@ p = 0.5 → Probability of success on each trial
@ This defines the likelihood of success in a single trial.
@ p=0.5 means there's a 50% chance of success per trial.
@ In the coin flip analogy, this means a fair coin — heads and tails are equally likely.
@ If p were 0.7, it would mean the coin is biased — you'd expect heads 70% of the time.
@ 📌 So: In each of the 10 trials per experiment, there's a 50% chance of success.


@ size = 1000 → Number of experiments (samples)
@ This tells the function how many full experiments to run.
@ You're not just simulating one person flipping a coin 10 times.
@ You're simulating this process 1000 times.
@ So you'll end up with 1000 numbers, each between 0 and 10, indicating the number of successes in that run.
'''
'''
sns.displot(random.binomial(n=10, p=0.5, size=1000), kind='kde')

plt.show()
'''

data = {
    "normal": (random.normal(loc=2, scale=2, size=1000)),
    "binomial": (random.binomial(n=2, p=0.5, size=1000))
}

sns.displot(data, kind='kde')

plt.show()