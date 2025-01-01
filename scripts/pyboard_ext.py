import sys
import os

# Need this to properly handle import paths for pyboard - 
# tools dir in micropython repo has not __init__.py file

script_dir = os.path.dirname(os.path.abspath(__file__))
tools_path = os.path.abspath(os.path.join(script_dir, '../micropython/tools'))
sys.path.append(tools_path)

import pyboard

pyb = pyboard.Pyboard('/dev/tty.usbmodem11101', 115200)
pyb.enter_raw_repl()
ret = pyb.exec('print(1+4)')
print(ret)
pyb.exit_raw_repl()