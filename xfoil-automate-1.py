import subprocess as sp
import shutil
import sys
import string
import time as t

t1 = t.time()
sp.Popen(['xfoil <controlfile.xfoil>outputfile.out'],
      stdin=sp.PIPE,
      stdout=None,
      stderr=None,
      shell=True
      )
t2= t.time()
print(t2-t1)