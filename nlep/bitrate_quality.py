import os
import sys
#from numpy import arange, around, hstack 
from cv2 import VideoCapture, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH

if len(sys.argv) < 2:
        sys.exit('Print Usage:\npython bitrate_quality.py distVidPath refVidPath')
#read the distorted file and extract its name and extension
f = sys.argv[1]
fName = os.path.splitext(f)[0]
fExt = os.path.splitext(f)[1] #file1[-4:]
fLog = fName + '.log' 

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
#Initialize lower bound and upper bound amd calcaulate midpoint
l = 0.1
h = 10.0
m = (l+h)/2.0
qd = 1.1

#command templates for transcoding and vmafscore estimation with placeholders for varaible which is updated inside the loop
brcmd = 'ffmpeg -y -i {f} -c:v libx265 -x265-params pass=1:stats={fn}/{fn}_{br}M.log -b:v {br}M -preset {ps} -an -f null /dev/null && ffmpeg -y -i {f} -c:v libx265 -x265-params pass=2:stats={fn}/{fn}_{br}M.log -b:v {br}M -preset {ps} -an {fn}/{fn}_{br}M{fe}'
qcmd = 'ffmpeg2vmaf {w} {h} {ref} {fn}/{fn}_{br}M{fe}'

print "\n\n\n\n", refVideoPath, "\n\n\n\n"
while(qd > 1.0):
        #lower bound transcoding and vmafscore estimation 
        os.system(brcmd.format(f=f, fn=fName, br=str(l), ps = preset, fe = fExt))
        ql = os.popen(qcmd.format(w=3840, h=2160, ref=refVideoPath, fn=fName, br=str(l),fe=fExt)).read().split()[-1].split(':')[1]
        print ql
        #write the score obtained to a file
        fl = open(os.path.join(fScore, fName+'_'+str(l)+'M.abc'), 'w')
        fl.write(ql)

        #higher bound transcoding and vmafscore estimation
        os.system(brcmd.format(f=f, fn=fName, br=str(h), ps = preset, fe = fExt))
        qh = os.popen(qcmd.format(w=width, h=height, ref=refVideoPath, fn=fName, br=str(h),fe=fExt)).read().split()[-1].split(':')[1]
        print qh
        fh = open(os.path.join(fScore, fName+'_'+str(h)+'M.abc'), 'w')
        fh.write(qh)

        #mid-point transcoding and vmafscore estimation 
        os.system(brcmd.format(f=f, fn=fName, br=str(m), ps = preset, fe = fExt))
        qm = os.popen(qcmd.format(w=width, h=height, ref=refVideoPath, fn=fName, br=str(m),fe=fExt)).read().split()[-1].split(':')[1]
        print qm
        fm = open(os.path.join(fScore, fName+'_'+str(m)+'M.abc'), 'w')
        fm.write(qm)
        print "\n\n\n\n", ql, qm, qh
        ql = float(ql)
        qm = float(qm)
        qh = float(qh)
        print ql, qm, qh, "\n\n\n\n"

        #update l and h based on bisection 
        if (qm-ql) > (qh-qm):
                h = m
                qd = qm-ql
                if m - l < 0.1:
                	break
        else:
                l = m
                qd = qh - qm
                if h - m < 0.1:
                	break
        m = round((l+h)/2.0, 3)
        fl.close()
        fh.close()
        fm.close()

