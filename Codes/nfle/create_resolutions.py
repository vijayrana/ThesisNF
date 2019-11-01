import os 
import sys

resolutionList = [360, 480, 720, 1080, 1440]
file1 = sys.argv[1]
file1Name = os.path.splitext(os.path.basename(file1))[0]
file1Ext = os.path.splitext(os.path.basename(file1))[1]

if not os.path.isdir(file1Name + '_resolutions'):
        os.mkdir(file1Name + '_resolutions')

#home = os.path.expanduser("~")
#ffmpeg = home + "/ffmpeg-4.1.3-amd64-static/ffmpeg"


for r in resolutionList:
    os.system('ffmpeg -y -i ' + file1 +  ' -vf scale=-2:' + str(r) + ' -c:v libx264 -crf 22 -an ' + file1Name + '_resolutions/'+ file1Name + '_' + str(r) + file1Ext)
    

