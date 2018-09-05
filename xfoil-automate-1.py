import subprocess as sp
import shutil
import sys
import string
import time
import os
import signal

ps = sp.Popen(['xfoil <controlfile.xfoil>outputfile.out'],
              stdin=sp.PIPE,
              stdout=None,
              stderr=None,
              shell=True
              #preexec_fn=os.setsid
                )
