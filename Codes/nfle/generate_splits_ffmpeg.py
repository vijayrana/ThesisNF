import os
import sys
import pandas as pd

file1 = sys.argv[1]
file1Name = os.path.basename(file1).split('.')[0]
file1Ext = "."+os.path.basename(file1).split('.')[1]
print file1Ext
print  file1Name
os.system('scenedetect -i ' + file1 + ' -o . detect-content list-scenes')
csvfile = file1Name + '-Scenes.csv'

df = pd.read_csv(csvfile, skiprows=[0])

ss = df.columns[2]
t = df.columns[-1]

for i, row in df.iterrows():
        os.system('ffmpeg -i ' +  file1 + ' -ss ' + str(row[ss]) + ' -t ' + str(row[t]) + ' -c:v copy -c:a copy ' + file1Name + '_scene_' + str(i+1) + file1Ext)

