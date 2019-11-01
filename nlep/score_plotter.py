
#skateboarding
#sp=[0,0,-8,5,5,-7]#Skateboarding
#ep = [-5,-5,-4,-3,-2,-1]
#a4 247 x 170

import pickle
import sys
import numpy as np
import matplotlib.pyplot as plt

brq_list = pickle.load(open(sys.argv[1],'r'))
#title = sys.argv[2]
print brq_list
sp = [0,0,1,0,1,2]
ep = [3,3,2,1,1, 0]

resl = [s[0] for s in brq_list]

def plotdesc():
	#plt.subplots_adjust(0.06, 0.06, 0.99, 0.97, 0.2,0.2)
	plt.axis((0, 10.5, 0, 100))
	plt.yticks(np.arange(0,101,10), fontsize=15)
	#plt.title(title, fontsize = 15)
	plt.xlabel('Bit Rate (Mbps)',  fontsize = 15)
	plt.ylabel('Quality (VMAF Score)',  fontsize = 15)
plt.subplots_adjust(0.06, 0.06, 0.99, 0.97, 0.2,0.2)

for i in brq_list:
	# plt.subplot(2,1,1)
	print i[1][:,0]
	plotdesc()
	plt.xticks(np.arange(0, 10.1, 1), fontsize=15)
	#print "BR...", i[1][:,0],  "  ......quality..... ", i[1][:,1]
	plt.plot(i[1][:,0], i[1][:,1], 'o-')
plt.legend(resl, fontsize = 15)

# for i, j, k in zip(brq_list, sp, ep):
# 	#plt.subplot(2,1,2)
# 	plotdesc()
# 	plt.xticks(np.arange(0, 10.1, 1), fontsize=15)
# 	end = len(i[1][1:,1])-k
# 	plt.plot(i[1][1:,0][j:end], i[1][1:,1][j:end], 'o-')
# 	plt.legend(resl, fontsize = 15)
# #plt.figure(figsize=(8.27, 11.69))
plt.show()