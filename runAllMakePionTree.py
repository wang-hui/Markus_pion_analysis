#! /usr/bin/env python3
import glob

event_files = glob.glob('/eos/user/m/mseidel/HCALDPG/RecoPaper/SinglePionExpo_miniRECO_CMSSW_10_6_UL/*RECO.root')
event_files += glob.glob('/eos/user/m/mseidel/HCALDPG/RecoPaper/SinglePionExpo_miniRECO_CMSSW_10_6_UL_NoPU/*RECO.root')
event_files += glob.glob('/eos/user/m/mseidel/HCALDPG/RecoPaper/SinglePionExpo_miniRECO_CMSSW_10_6_UL_OOTPU/*RECO.root')
command = './MakePionTree.py'
commands = [[command, f, '--overwrite'] for f in event_files]

threads = 10

print('jobs    = %i' % len(commands))
print('threads = %i' % threads)

from multiprocessing.pool import ThreadPool
from subprocess import STDOUT, call

def run(cmd):
    return cmd, call(cmd, stderr=STDOUT)

for cmd, rc in ThreadPool(threads).imap_unordered(run, commands):
    if rc != 0:
        print('{cmd} failed with exit status: {rc}'.format(**vars()))