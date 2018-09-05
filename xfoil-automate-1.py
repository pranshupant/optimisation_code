import subprocess as sp
import shutil
import sys
import string

sp.Popen(['xfoil <controlfile.xfoil>outputfile.out'],
      stdin=sp.PIPE,
      stdout=None,
      stderr=None,
      shell=True
      )
