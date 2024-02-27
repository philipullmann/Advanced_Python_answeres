#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:49:49 2024

@author: philip
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm, ttest_ind

mu = 10
poisson_rv = poisson(mu)

# Plot PMF
x = np.arange(0, 20)  # Define the range of values for plotting
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, poisson_rv.pmf(x), 'bo', ms=5)  # PMF
plt.vlines(x, 0, poisson_rv.pmf(x), colors='b', lw=2, alpha=0.5)
plt.title('Probability Mass Function (PMF)')


# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, poisson_rv.cdf(x), 'ro', ms=5)  # CDF
plt.title('Cumulative Distribution Function (CDF)')

plt.tight_layout()

# Plot histogram of 1000 random realizations
plt.figure()
plt.hist(poisson_rv.rvs(size=1000), bins=range(21), density=True, alpha=0.7)
plt.title('Histogram of 1000 Random Realizations')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()



# Create a normal random variable with mean mu and standard deviation sigma
mu = 0  # Mean
sigma = 1  # Standard deviation
normal_rv = norm(loc=mu, scale=sigma)

# Plot PDF
x = np.linspace(-5, 5, 1000)  # Define the range of values for plotting
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, normal_rv.pdf(x), 'b-', lw=2)  # PDF
plt.title('Probability Density Function (PDF)')

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, normal_rv.cdf(x), 'r-', lw=2)  # CDF
plt.title('Cumulative Distribution Function (CDF)')

plt.tight_layout()


# Plot histogram of 1000 random realizations
plt.figure()
plt.hist(normal_rv.rvs(size=1000), bins=30, density=True, alpha=0.7)
plt.title('Histogram of 1000 Random Realizations')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()


# Generate samples
sample_size = 1000
samples_poisson = poisson_rv.rvs(size=sample_size)
samples_normal = normal_rv.rvs(size=sample_size)

# Perform t-test
t_statistic, p_value = ttest_ind(samples_poisson, samples_normal)
print("T-statistic:", t_statistic)
print("P-value:", p_value)


