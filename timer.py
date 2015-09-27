#!/usr/bin/python
import time
import sys
from Tkinter import *

def timer(minutes):
	print "Started at " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	print "Running for %f minutes" %(minutes)
	mins = 0
	#60 seconds of sleep
	sec = 60
	#can also call less than a minute
	if minutes < 1:
		sec = int(60*minutes)
    #Loop until minutes is reached
	while mins < minutes:
		time.sleep(sec)
		#One more minute!
		mins += 1
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
		timer(10)