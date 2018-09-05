import subprocess as sp
import shutil
import sys
import string
import time
import os
import signal

ps = sp.Popen(["xfoil"],
              stdin=sp.PIPE,
              stdout=None,
              stderr=None,preexec_fn=os.setsid)

def issueCmd(cmd,echo=True):
    ps.stdin.write(cmd.encode('utf-8'))
    if echo:
       print(cmd)
       #time.sleep(0.5)

cmd = [ "load bsairfoil.txt\n",
        "oper\n",
        "v\n",
        "1.346e6\n", 
        "iter 5000\n", 
        "pacc\n",
        "bsa.txt\n\n",
        "alfa 0\n",
        "pacc\n",
        "cpwr cp_a0.dat\n",
        "dump d.dat\n",
        "hard\n",
        "\n",
        "quit\n"]


for i in range(len(cmd)):
    issueCmd(cmd[i])


#os.killpg(os.getpgid(ps.pid), signal.SIGTERM)