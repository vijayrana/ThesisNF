import matplotlib.pyplot as plt
import numpy as np
import pickle
from lmfit.model import load_model, Model

data = pickle.load(open('american_football_harmonic_scene_4_score.bin','r'))
x, y = data[-1][1][:,0], data[-1][1][:,1]
print len(x)
def func(x, a, b, c):
    return a*np.log(x+b) + c


model = Model(func)
params = model.make_params(a=3, b=10, c=0)
params['b'].min = 1

result = model.fit(y, params, x=x)
print(result.fit_report())

plt.plot(x, y, 'bo')
plt.plot(x, result.best_fit, 'r-')
plt.axis((0, 10, 0, 100))
plt.plot(x, 23.03*np.log(x+1)+34.48, 'g+')
plt.show()