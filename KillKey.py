#!/usr/bin/env python
import os
from time import sleep
from config import *
while 1:
    if os.system(the_command + " | grep " + device_uuid) == 0:
        print("FOUND")
    else:
        print("NOT FOUND")
        #os.system(logout) #this logs you out but doesn't reinit fileVault
    sleep(5)