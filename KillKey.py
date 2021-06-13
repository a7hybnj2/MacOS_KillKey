#!/usr/bin/python

import os
import getpass
import pwd
import time

#Set this during setup. Prevents logoff and provides some feedback
test = False

name = getpass.getuser()
id = pwd.getpwnam(name).pw_uid
the_command = "system_profiler SPUSBDataType"
device_uuid = "0E239BC6-F960-3107-89CF-1C97F78BB46B" #no private every reformat is new UUID
logout = "launchctl bootout user/" + str(id)


# Should this be 'user' or 'gui'?
# Having tested both ^ they appear to be identical

# The user will need admin privlidges. for bootout
# could try a 'killall -u name' but I think that might need privlidges too.

if test:
	if os.system(the_command + " 2>/dev/null | grep -w " + device_uuid + " 1>/dev/null") != 0:
	    print("DID NOT FIND KEY!")
	else:
	    print("FOUND KEY!")
	print()
	print("Below is the command that will be run to log out")
	print(logout)
else:
	while 1:
		# I need to put an event handler here for accepting ctrl+c
		if os.system(the_command + " 2>/dev/null | grep -w " + device_uuid + " 1>/dev/null") != 0:
			os.system(logout)
		time.sleep(1)