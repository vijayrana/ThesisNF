import numpy as np

#Skateboarding
ranges = {
360 : np.hstack((np.arange(0.025, 0.15, 0.025))), 
480 : np.hstack((np.arange(0.025, 0.15, 0.025))),#np.arange(0.175, 0.396, 0.05),0.395)), 
720 : np.hstack((0.05, 0.075, 0.21, np.arange(0.1, 0.25, 0.025))), 
1080: np.hstack((0.21, 0.32, np.arange(0.2, 0.375, 0.025))), 
1440: np.hstack((0.32, np.arange(0.3, 1.5, 0.1))), 
2160: np.hstack((1.2, 1.0, np.arange(1.3, 10, 0.25)))
}