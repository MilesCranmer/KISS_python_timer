#!/usr/bin/python
import time
import sys
from Tkinter import *

def timer(minutes):
	print "Started at " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	print "Running for %f minutes" %(minutes)
	time.sleep(int(60.0*minutes))
        #when time is over, create dialog box:
	root = Tk() 
	root.title("%d minutes are up!" % (minutes))
	root.lift()
	root.call('wm', 'attributes', '.', '-topmost', '1')
	mainloop()

#starts program with entered time in minutes, or 10 minutes
if __name__ == "__main__":
    if len(sys.argv) > 1:
        timer(float(sys.argv[1]))
    else:
        print("Please enter a time")
        exit()
