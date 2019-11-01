import os, sys, argparse
import numpy as np

parser = argparse.ArgumentParser(description='Extract scores from score files from given dir path in arguments and plot it')

parser.add_argument('-f', type=str, help='Path to score directories')
#parser.add_argument('-t', type=str, help='Title for plot')

args = parser.parse_args()
print 'args.f', args.f, '\n'
if args.f[-1] == '/':
        args.f = args.f[:-1]
rds = os.path.basename(args.f).replace('resolutions', '')
print 'rds', rds
#os.chdir(args.f)
resdir = [f for f in os.listdir(args.f) if f.endswith('_score')]
resdir.sort(key=lambda x: float(x.replace(rds, '').replace('_score', '')))
print resdir

brq_list = []
os.chdir(args.f)
for rd in resdir:
        rpath1 = os.path.join(os.getcwd(), rd)
        scorefiles = [s for s in os.listdir(rpath1) if s.endswith('.abc')]
        res = (rd.split('_')[-2])

        scorefiles.sort(key=lambda x:float(x.replace(rds+res+'_', '').replace('M.abc', '')))

        brq = np.zeros((len(scorefiles),2))
        for i, sf in enumerate(scorefiles):
                res = rd.split('_')[-2]
                rpath2 = os.path.join(rpath1, sf)
                print 
                with open(rpath2, 'r') as freader:
                        brq[i] = [(sf.replace(rds+res+'_', '').replace('M.abc', '')), freader.read()]
                        print "brq " +str(i)+ str(sf) + ' ......... ' + str(brq[i]) + '\n'

        brq_list.append((rd.split('_')[-2], brq))

import pickle
#if not os.path.exists(rds+'score.bin'):
with open(rds+'score.bin', 'w') as pdump:
        pickle.dump(brq_list, pdump)


