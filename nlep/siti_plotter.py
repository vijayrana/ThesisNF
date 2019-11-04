import matplotlib.pyplot as plt 
import pandas as pd 
import argparse
import os

parser = argparse.ArgumentParser(description='Extract SITI scores from csv file and plot it')
parser.add_argument('-f',type=str, help='path to SITI csv file')
parser.add_argument('-t', '--title', type=str, help='Title for plot')
args = parser.parse_args()
print args
# f = os.path.splitext(os.path.basename(args.f))[0]
# print type(f)
# cpu_count = str(8)
#os.system("./siti.py " + args.f + " --output_file " + f + ".csv --cpu_count " + cpu_count)
print  args.title
csvfile = args.f

df = pd.read_csv(csvfile) #, skiprows=[0])

si = df.si.tolist()
ti = df.ti.tolist()
frame = df.frame.tolist()

#plt.plot(frame, si, '')
plt.plot(si, ti, 'o')
#plt.legend(['Spatial Information', 'Temporal Information'])
plt.title(args.title, fontsize=15)
plt.xlabel('Spatial Information', fontsize=15)
plt.ylabel('Temporal Information', fontsize=15)
plt.xticks(fontsize=15)#,  rotation=0)
plt.yticks(fontsize=15)
plt.subplots_adjust(0.06, 0.06, 0.99, 0.97, 0.2,0.2)
plt.show()
