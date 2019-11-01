import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons, TextBox
import pickle 
import sys
import os
import collections

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
    print "length.....", len(bitRate)
    return bitRate, qp

##############################################################################################

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
#plt.plot(np.arange(0, 10.1, 0.01)+0.99, 1 * np.log10(np.arange(0, 10.1, 0.01)) + 74.63, lw=2)
#plt.axis((0, 10, 0, 100))
# plt.ylabel('Quality (VMAF Score)', fontsize=15)
# plt.xlabel('Bit Rate (Mbps)', fontsize=15)
# plt.xticks(np.arange(0, 10.1, 0.5), fontsize=15)#,  rotation=0)
# plt.yticks(np.arange(0,100.1,5), fontsize=15)
# title = 'VMAF Quality Score at 720p resolution over different Bitrates'
#plt.title(title, fontsize=20)
# plt.legend(reslist,fontsize=15)
# plt.subplots_adjust(0.04, 0.06, 0.99, 0.97, 0.2,0.2)

##############################################################################################
flag = 0
if flag == 1:
    ipvalues = raw_input("Enter values for a,xoff and yoff (space-separated)\n").split()
    a,xoff,yoff = [float(z) for z in ipvalues]
    base = np.e
else:
    #a,base,xoff,yoff = 10,np.e,0,0
    a,base,xoff,yoff = 1, np.e, 0, 0

plt.subplots_adjust(bottom=0.25)

t = np.arange(0, 10.1, 0.01)
s = a * np.log(t) + yoff
l, = plt.plot(t+xoff, s, lw=2)
plt.axis((0, 10, -10, 100))
plt.legend(reslist+['Ln Curve'])
###############################################################################################
# brq_list = pickle.load(open(sys.argv[1],'r'))
# sp = [0,0,1,0,1,2]
# ep = [3,3,2,1,1,0]
# resl = [s[0] for s in brq_list]

# for i,j,k in zip(brq_list,sp,ep):
# 	plt.xticks(np.arange(0, 10.1, 1), fontsize=15)
# 	end = len(i[1][1:,1])-k
# 	plt.plot(i[1][1:,0][j:end], i[1][1:,1][j:end], '.-')
# 	plt.legend(['Ln Curve']+resl)
#############################################################################################
#				left up/down  right width
axa = plt.axes([0.05, 0.15, 0.65, 0.015])
axb = plt.axes([0.05, 0.12, 0.65, 0.015])
axc = plt.axes([0.05, 0.09, 0.65, 0.015])
axcf = plt.axes([0.05, 0.06, 0.65, 0.015])
axd = plt.axes([0.05, 0.03, 0.65, 0.015])
axdf = plt.axes([0.05, 0.00, 0.65, 0.015])
resetax = plt.axes([0.8, 0.09, 0.9, 0.05])


sa = Slider(axa, 'a', 0.01, 40.0, valinit=a, valstep=0.001)
sb = Slider(axb, 'base', 1.001, 100, valinit=base, valstep=0.01)
sc = Slider(axc, 'xoff', -3.0, 3.0, valinit=xoff, valstep=0.01)
scf = Slider(axcf, 'xoff Fine', -1.0, 1.0, valinit=0, valstep=0.001)
sd = Slider(axd, 'yoff', -150.0, 150.0, valinit=yoff, valstep=0.01)
sdf = Slider(axdf, 'yoff Fine', -150.0, 150.0, valinit=yoff, valstep=0.01)

def nplog(n, base=np.e):
	return np.log(n)/np.log(base)

def update(val):
    au = sa.val
    baseu = sb.val
    xoffu = sc.val
    xoffuf = scf.val
    yoffu = sd.val
    yoffuf = sdf.val
    l.set_ydata(au*nplog(t, baseu) + yoffu+yoffuf)
    l.set_xdata(t+xoffu+xoffuf)
    fig.canvas.draw_idle()

sa.on_changed(update)
sb.on_changed(update)
sc.on_changed(update)
sd.on_changed(update)
scf.on_changed(update)
sdf.on_changed(update)

button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    sa.reset()
    sb.reset()
    sc.reset()
    sd.reset()
button.on_clicked(reset)

plt.show()

print ' a = ',sa.val, '\n', ' base = ', sb.val, '\n', ' xoff = ', sc.val+scf.val ,'\n', ' yoff = ', sd.val+sdf.val

