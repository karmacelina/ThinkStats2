import nsfg
import math

preg = nsfg.ReadFemPreg()

# Choose live births only. 
live = preg[preg.outcome == 1] 

# first born babies and others
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenEffectSize(group1, group2):
	diff = group1.mean() - group2.mean()

	var1 = group1.var()
	var2 = group2.var()
	n1, n2 = len(group1), len(group2)

	weighed_var = (n1*var1 + n2*var2)/(n1+n2)

	d = diff/math.sqrt(weighed_var)

	return d

d_prglngth = CohenEffectSize(firsts.prglngth, others.prglngth)

print("The difference in the means of pregnancy lengths for first borns" 
" and those who are not first borns is %0.3f standard deviations" % d_prglngth)


"""
Using the variable totalwgt_lb, investigate whether first babies are lighter
or heavier than others.

Compute Cohen's d to quantify the difference between the groups. 

How does it compare to the difference in pregnancy length?
"""

# First, create variables corresponding to first and other babies' weights series

wg_firsts = firsts.totalwgt_lb
wg_others = others.totalwgt_lb

# Compute Cohen's d:
d_totalwgt_lb = CohenEffectSize(wg_firsts, wg_others)

print("\nThe difference in the means of weight in lbs for first borns"
	" and those who are not first borns is %0.3f standard deviations" % d_totalwgt_lb)

ratio = d_totalwgt_lb/d_prglngth

print ("\n The ratio between the size of the effect order of birth has on these"
" quantities is %0.3f" % ratio)

