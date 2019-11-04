import matplotlib.pyplot as plt
import numpy as np
import pickle, sys
from lmfit.model import load_model, Model

data = pickle.load(open(sys.argv[1],'r'))
res = sys.argv[2]
x, y = [], []
for i in data:
	print i[0]
	if i[0] == res:
		print i[1]
		x, y = i[1][:,0], i[1][:,1]

xm, ym = np.array((x[0], x[(len(x)/2)],x[(len(x)/2)+1], x[-1])), np.array((y[0], y[(len(x)/2)], y[(len(x)/2)+1], y[-1]))
#xmm, ymm = np.array([x[0], x[-1]]), np.array([y[0], y[-1]])
print x[0], x[-1]
print x
def logb(x, base = np.e):
	return np.log(x)/np.log(base)

def func(x, a, b, c):
    return a*np.log(x+b) + c

model = Model(func)
params = model.make_params(a=0, b=10, c=0)
params['b'].min = 1
# params['base'].min = 1

result = model.fit(y, params, x=x)
resultm = model.fit(ym, params, x=xm)
#resultmm = model.fit(ymm, params, x=xmm)
#print(result.fit_report())

plt.plot(x, y, 'bo')
plt.plot(x, result.best_fit, 'r.')
plt.plot(xm, resultm.best_fit, 'g+')
plt.axis((0, 10.5, 0, 100))
plt.legend(['Original', 'fitbrute', 'fit minimum'])
#plt.plot(x, 23.03*np.log(x+1)+34.48, 'g+')
plt.show()