import subprocess as sp
#import os
import shutil
import sys
import string

 
ps = sp.Popen(['xfoil'],
              stdin=sp.PIPE,
              stdout=None,
              stderr=None)

cmd = 'load bsairfoil.txt\n'
 
def issueCmd(cmd,echo=True):
    ps.stdin.write(cmd.encode('utf-8'))
    if echo:
       print(cmd)
 
issueCmd(cmd)

cmdn = ["oper\n",
        "v\n",
        "1.346e6\n", 
        "iter 5000\n", 
        "pacc\n",
        "bsa.out\n\n",
        "alfa 0\n",
        "pacc\n",
        "cpwr cp_a0.dat\n",
        "dump d.dat\n",
        "hard\n",
        "\n", 
        "quit\n"]


for i in range(len(cmdn)):
    issueCmd(cmdn[i])

