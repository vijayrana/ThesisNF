import matplotlib.pyplot as plt
import numpy as np
import pickle, sys
from scipy.optimize import curve_fit
import os

def func(x, a, b, c):
    return a*np.log(x+b) + c

data = pickle.load(open(sys.argv[1],'r'))
res = [a[0] for a in data]#sys.argv[2]
#print res
x, y = [], []
poptmlist  = []
mse = {}
for i in data:
	x, y = i[1][:,0], i[1][:,1]
	xm, ym = np.array((x[0], x[(len(x)/2)],x[(len(x)/2)+1], x[-1])), np.array((y[0], y[(len(x)/2)], y[(len(x)/2)+1], y[-1]))
	#popt, pcov = curve_fit(func, x, y, bounds=([10, 0, -0],[1000, 100, 1000]))
	poptm, _ = curve_fit(func, xm, ym, bounds=([10, 0, -0],[1000, 100, 1000]))
	#plt.plot(x, func(x, *popt))#, 'ro')
	logres = poptm[0]*np.log(x+poptm[1])+poptm[2]
	mse[i[0]] = np.square(np.subtract(y,logres)).mean()
	plt.plot(xm, func(xm, *poptm), 'o', lw=3)
	poptmlist.append(poptm)
	#plt.plot(x, y)

for i in data:
	x, y = i[1][:,0], i[1][:,1]
	plt.plot(x, y, 'black', lw=2)
plt.legend([(r, '{0:.2f}*(br+{0:.2f})+{0:.2f}'.format(*a)) for r, a in zip(res,poptmlist)]+['original'])
plt.xlabel('Bit Rate (Mbps)')#,  fontsize = 15)
plt.ylabel('Quality (VMAF Score)')
#plt.axis((-1,10, 0, 100))
fname = os.path.splitext(sys.argv[1])[0] + '_log.pdf'

plt.savefig(fname, papertype='a4', format='pdf', dpi=1200, bbox_inches='tight')
plt.show()

pickle.dump(mse, open(sys.argv[1].replace('score.bin','msescores.bin'), 'w'))

# MSE = np.square(np.subtract(Y_true,Y_pred)).mean() 