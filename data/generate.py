import numpy as np
from math import exp


def normal(num=100, d=3, a=1.0, b=0.5, c=0.0):
        # generate the means of the distribution
        mu = np.array([c for _ in range(d)])

        # generate the desired covariance matrix
        r = np.array([[a if c == r else b for c in range(d)] for r in range(d)])

        # Generate the random samples.
        return np.random.multivariate_normal(mu, r, size=num)


def sigmoid(start=-5.0, end=5.0, num=50):
        for i in np.linspace(start, end, num):
            yield 1 / (1 + exp(-i))
