import os
import collections
import sys
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.pyplot as plt
import pickle
import numpy as np

def extractscores(_file):
	# fName = _file#sys.argv[1]
	res = _file[10:-4]
	f = open(_file, 'r')
	_ = pickle.load(f)
	f.close()
	vmafScore = _.copy()
	for i in vmafScore.keys():
	    vmafScore[float(i.split('_')[6][:-1])] = float(vmafScore.pop(i))
	oVmafScore = collections.OrderedDict(sorted(vmafScore.items()))
	bitRate, qp = oVmafScore.keys(), oVmafScore.values()
	#print "length.....", len(bitRate)
	return bitRate, qp

if len(sys.argv) < 2:
	sys.exit("Few arguments provided\nUsage: python readScore.py <path/to/scorefiles/.xyz/directory>")

scorefiles = [f for f in os.listdir(sys.argv[1]) if f.endswith('xyz')]
scorefiles.sort(key= lambda x: float(x.strip('vmafscores').strip('.xyz')))
reslist = []
startPoints = {
360:1, 
480:2, 
720:4, 
1080:10, 
1440:21, 
2160:28
}#default is [0,0,0,0,0,0]
#scorefiles = [scorefiles[0]]
#endpoints = {360:-1, 480:-1, 720:-1, 1080:-1, 1440:-1, 2160:-1}
endpoints = {
360:6, 
480:8, 
720:16, 
1080:24, 
1440:32, 
2160:-1,
}

fig = plt.figure()
for f in scorefiles:#sys.argv[1:]
	print f
	res = int(f[10 : -4])
	print res
	reslist.append(f[10 : -4]) 
	bitRate, qp = extractscores(f)	
	plt.plot(bitRate[startPoints[res]:endpoints[res]], qp[startPoints[res]:endpoints[res]], 'o-')

#plt.axis((0, 10, 0, 100))
plt.ylabel('Quality (VMAF Score)', fontsize=15)
plt.xlabel('Bit Rate (Mbps)', fontsize=15)
plt.xticks(np.arange(0, 10.1, 0.5), fontsize=15)#,  rotation=0)
plt.yticks(np.arange(0,100.1,5), fontsize=15)
title = 'VMAF Quality Score at 720p resolution over different Bitrates'
#plt.title(title, fontsize=20)
plt.legend(reslist,fontsize=15)
plt.subplots_adjust(0.04, 0.06, 0.99, 0.97, 0.2,0.2)
#pickle.dump(fig,file('hongkong_data.bin','w'))
plt.show()
#plt.savefig('VMAF.jpg')

