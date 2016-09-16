import nsfg
import thinkstats2
import thinkplot
from chap01ex import ReadFemResp

resp = ReadFemResp()

print "numkdhh" in resp

# Actual distribution of the number of children under 18 in households

pmf_num = thinkstats2.Pmf(resp.numkdhh, label = "actual")

def BiasPmf(pmf, label):
	new_pmf = pmf.Copy(label = label)

	for x, p in pmf.Items():
		new_pmf.Mult(x, x)

	new_pmf.Normalize()

	return new_pmf

new_pmf_num = BiasPmf(pmf_num, label = "biased")

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_num, new_pmf_num])
thinkplot.Show(xlabel = "# kids in household", ylabel = "PMF")

actual_mean = pmf_num.Mean()
biased_mean = new_pmf_num.Mean()

print "There is an actual mean of %0.2f children per household" % actual_mean
print ("If we surveyed children themselves that biased distribution has"
" a mean of %0.2f" % biased_mean)