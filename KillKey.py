#!/usr/bin/env python
import subprocess #I read that this is *safer*
import os
from config import *
if os.system(the_command + " | grep " + device_uuid) == 0:
    print("FOUND")
else:
    print("NOT FOUND")