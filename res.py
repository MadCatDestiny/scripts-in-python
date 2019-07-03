import  os
import sys
#TODO: add cross-platform
pl = sys.platform
cdir = os.getcwd()
try:
    f = open('ht.in','r')
    f.close()
    os.startfile(cdir + '\\tr.exe')
except FileNotFoundError:
    os.startfile(cdir + '\\in.exe')
