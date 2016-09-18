from __future__ import print_function, division

import thinkstats2
import thinkplot

""" In the BRFSS, the distribution of heights is roughly normal 
with parameters \mu = 178 cm and \sigma = 7.7 cm for men, and
\mu = 163 cm and \sigma = 7.3 cm for women. 

In order to join the Blue Man Group, you have to be a male between
5'10" and 6'1". 

What percentage of the U.S. male population is in this range? """

import scipy.stats

# Normal distribution of heights of men in the U.S. population
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc = mu, scale = sigma)

""" What percentage of U.S. men are between 5'10" and 6'1" ? """

# How many men are 5'11" or below?

h1_cm = (5 + 10 / 12) *  30

dist.cdf(h1_cm)

# How many men are 6'1" or below?
h2_cm = (6  + 1 / 12) * 30

dist.cdf(h2_cm)

percentage = (dist.cdf(h2_cm) - dist.cdf(h1_cm)) * 100

print("The percentage of the U.S. male population with heights",
"between 5'11\" and 6'1\" is %0.1f%%." % percentage)
