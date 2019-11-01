import os
import sys
#from numpy import arange, around, hstack 
from cv2 import VideoCapture, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH
import numpy as np
if len(sys.argv) < 2:
        sys.exit('Print Usage:\npython bitrate_quality.py distVidPath refVidPath')
#read the distorted file and extract its name and extension
global fi
fi = sys.argv[1]
fName = os.path.splitext(fi)[0]
fres = float(os.path.splitext(fi)[0].split('_')[-1])
fExt = os.path.splitext(fi)[1] #file1[-4:]
fLog = fName + '.log' 
print 'fres.................', fres
#preset for 2 pass encoding
preset = "slow"
#fi = fName''.join([i for i in fName if not i.isdigit()])

#read the reference file from command line as second argument
refVideoPath = sys.argv[2]

#create folder to store the files wth vmafscores
fScore = fName + '_score'

#extract width and height of reference video
cap = VideoCapture(refVideoPath)
width, height = int(cap.get(CAP_PROP_FRAME_WIDTH)), int(cap.get(CAP_PROP_FRAME_HEIGHT))
print "\n\n\n\n"
print fName, refVideoPath
print "\n\n\n\n"
#sys.exit()

#create folders for transcoded videos and vmafscore files
if not os.path.isdir(fName):
        os.mkdir(fName)
        os.mkdir(fScore)
#command templates for transcoding and vmafscore estimation with placeholders for varaible which is updated inside the loop
brcmd = 'ffmpeg -y -i {f} -c:v libx265 -x265-params pass=1:stats={fn}/{fn}_{br}M.log -b:v {br}M -preset {ps} -an -f null /dev/null && ffmpeg -y -i {f} -c:v libx265 -x265-params pass=2:stats={fn}/{fn}_{br}M.log -b:v {br}M -preset {ps} -an {fn}/{fn}_{br}M{fe}'
qcmd = 'ffmpeg2vmaf {w} {h} {ref} {fn}/{fn}_{br}M{fe}'

def br_q(bitrate):
        os.system(brcmd.format(f=fi, fn=fName, br=str(bitrate), ps = preset, fe = fExt))
        qb = os.popen(qcmd.format(w=3840, h=2160, ref=refVideoPath, fn=fName, br=str(bitrate),fe=fExt)).read().split()[-1].split(':')[1]
        #write the score obtained to a file
        with open(os.path.join(fScore, fName+'_'+str(bitrate)+'M.abc'), 'w') as f:
                f.write(qb)
# america range 360 (0.075, 0.4, 0.1), 480(0.36, 0.4, 0.1), 720(0.38, 0.9, 0.1), 1080(0.8, 2.3, 0.2), 1440(2.2, 4.4, 0.3), 2160(4.3, 10, 1)
# ranges = {360:np.hstack((np.arange(0.1, 1, .1), np.arange(1, 3, 0.25)))
#         480: np.hstack(np.arange())}
#americanfootball
# ranges = {
# 360 : np.arange(0.1, 0.176, 0.025), 
# 480 : np.hstack((np.arange(0.175, 0.396, 0.05),0.395)), 
# 720 : np.hstack((0.395, np.arange(0.4, 0.9, 0.1), 0.856)), 
# 1080: np.hstack((0.856, np.arange(0.9, 2.3, 0.2), 2.2, 2.298)), 
# 1440: np.hstack((2.298, np.arange(2.4, 4.2, 0.4), 4.32)), 
# 2160: np.hstack((4.32, np.arange(4.5, 10, 0.5)))}

#bigbuckbunny
# ranges = {
# 360 : np.hstack((np.arange(0.025, 0.16, 0.025), 0.16)), 
# 480 : np.hstack((0.1, 0.17, 0.2)), #np.arange(0.175, 0.396, 0.05),0.395)), 
# 720 : np.hstack((0.15, 0.12, np.arange(0.2, 0.3, 0.025), 0.317, 0.32)), 
# 1080: np.hstack((0.315, 0.317, np.arange(0.35, 2.3, 0.2), 0.483, 0.493)), 
# 1440: np.hstack((0.473, 0.483, np.arange(0.5, 1.0, 0.1), 1.452, 1.55)), 
# 2160: np.hstack((1.352, np.arange(1.5, 10, 0.5)))}

#costarica
# ranges = {
# 360 : np.hstack((np.arange(0.025, 0.125, 0.025))), 
# 480 : np.hstack((np.arange(0.05, 0.125, 0.025), 0.117, 0.12)),#np.arange(0.175, 0.396, 0.05),0.395)), 
# 720 : np.hstack((0.1, 0.117, np.arange(0.125, 0.3, 0.025))), 
# 1080: np.hstack((0.23, 0.254, np.arange(0.25, 0.7, 0.05))), 
# 1440: np.hstack((np.arange(0.33, 0.73, 0.05))), 
# 2160: np.hstack((0.5, 0.524, np.arange(0.6, 10, 0.25)))
# }

#monkeys
# ranges = {
# 360 : np.hstack((0.145, 0.160, np.arange(0.025, 0.175, 0.025))), 
# 480 : np.hstack((np.arange(0.125, 0.4, 0.025), 0.318, 0.33)),#np.arange(0.175, 0.396, 0.05),0.395)), 
# 720 : np.hstack((0.3, 0.317, 0.87, np.arange(0.125, 0.9, 0.05))), 
# 1080: np.hstack((0.85, 0.87, np.arange(0.9, 2.6, 0.1))), 
# 1440: np.hstack((2.6, np.arange(2.0, 5.5, 0.25))), 
# 2160: np.hstack((5.4, np.arange(5, 10, 0.25)))
# }

#Myanmar
ranges = {
360 : np.hstack((np.arange(0.025, 0.15, 0.025))), 
480 : np.hstack((np.arange(0.025, 0.15, 0.025))),#np.arange(0.175, 0.396, 0.05),0.395)), 
720 : np.hstack((0.075, 0.45, np.arange(0.1, 0.5, 0.05))), 
1080: np.hstack((0.45, 0.785, np.arange(0.4, 0.85, 0.05))), 
1440: np.hstack((0.785,0.75,1.72, np.arange(0.8, 1.8, 0.1))), 
2160: np.hstack((1.72, 1.7, np.arange(1.8, 10, 0.2)))
}

#loops with different ranges for different resolutions
for i in ranges[fres]:
        br_q(i)


