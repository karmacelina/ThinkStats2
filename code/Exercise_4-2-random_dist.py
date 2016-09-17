import thinkstats2
import thinkplot
import numpy as np 
import matplotlib.pyplot as plt 

random_1000 = []

for i in range(1000):
	random_1000.append(np.random.random())

index_random_1000 = []
for index, number in enumerate(random_1000):
	index_random_1000.append(index)

plt.scatter(index_random_1000, random_1000)
plt.show()

pmf = thinkstats2.Pmf(random_1000, label = 'random number')
cdf = thinkstats2.Cdf(random_1000, label = 'random number')

thinkplot.PrePlot()
thinkplot.Pmf(pmf)
thinkplot.Show(xlabel = 'random number', 
			   ylabel = 'probability', 
			   loc = 'best',
			   axis = [0, 1, 0, 0.002],
			   title = 'Probabilty Mass Function: Randomly picked numbers from 0 to 1 ')

thinkplot.PrePlot()
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel = 'random number',
	           ylabel = 'cumulative distribution function',
	           loc = 'best',
	           axis = [0, 1, 0, 1],
	           title = 'Cumulative Distribution Function: Randomly picked numbers from 0 to 1')
