# KillKey

This project allows you to have a physical 'key' connected to your computer. When that key is removed the computer will quickly logout keeping your data safe.

## Contributing

I would be very happy if someone was interested in taking a look at this and suggesting improvements.

## Setup
1. The only file of importance is the KillKey.py
2. Create the hardware 'key'
   1. Plug a thumb drive into your computer.
   2. Run in terminal `diskutil list`
   3. Note the path for your usb thumb drive
   4. Run in terminal `diskutil eraseDisk free KillKey /YOUR_PATH_FROM_PREVIOUS_STEP_HERE`
      - This will remove the filesystem from the disk and prevent it from showing up as a storage device. It will also prevent it from being mounted which means you will not get the "improperly ejected" warnings.
   5. Run in terminal `system_profiler SPUSBDataType`
   6. Copy the UUID listed for your USB Drive
   - This will lists more than just your USB Drive and you will have to find what your looking for.
   - Mine looks like this:
		```
		USB X.X Bus
			Host Controller Driver:
			...
			Bus Number:
				...
					Product ID:
					...
						...
							Capacity:
							...
							Volumes:
								EFI:
									...
									Volume UUID: 0E239BC6-F960-3107-89CF-1C97F78BB46B
		```

4. Edit KillKey.py
   1. Change `device_uuid` to your UUID you took note of earlier
		- Note: if you re-eraseDisk your UUID will change
	2. There is a `test` variable you can set to `true` or `false`
		- if `test`
			- wont log you off
			- wont loop
			- provides feedback via term

## Starting
You will need to decide you to launch the script.  
possible options include:
	
- create a `plist`
	- Edit com.user.killkeyinterval.plist
	- Copy `com.user.killkeyinterval.plist` to `~/Library/LaunchAgents/`
	- TEST: Would a link work (ln)?
	- Run in terminal `launchctl load ~/Library/LaunchAgents/com.user.killkeyinterval`
	- logout / login
- use `Script Editor` to make a startup app
	- `do shell script "python /path/KillKey.py"`
- manually open via terminal
	- `python /path/KillKey.py`


## Notes

This is not a ['USB KILL'](https://usbkill.com/). This script will do no damage to your computer\*

This is not a ['BAD USB'](https://maltronics.com/collections/malduinos) type device.

*it might

## FAQ

- Can I use the usb drive as a drive?
	- Technically yes but not recommended.
- What happens if I lose my key?
	- Unknown, its **untested**.
- Is there recommended hardware?
	- There will be a wiki page on hardware.
- Does this cause: `error: gpg failed to sign the data`?
	- It seems to mess it up somehow. Probably because of the 'FORCE' logout.
	- Run `gpgconf --kill gpg-agent` and it should reload and work again.

## Hardware

- `magnetic 20-pin usb-c adapter` is a good starting search string.
	- I found mine on aliexpress for about $6 shipped. When I got them they were branded 'Upmely'.
- just buy the smallest, in both dimensions and capacity, usb drive you can find.
	- I bought the SanDisk Ultra 16GB on Amazon for $7.

## TODO

- [ ] Change the name? I think KillKey might not what people expect a utility like this to be called.
	- quitKey
	- securityKey
	- lanyardProtection
	-  LogOffOMatic
- [ ] Maybe an existing utility like fswatch could be used to monitor the filesystem.
- [ ] Remove the startup plists. This can easily be started another way when the user wants the functionality. It could be an app or hot key or a number of other options.
- [ ] Does the plist prevent sleep?
	- `pmset -g assertions` doesn't seem like it
- [ ] Would [Monitoring a Directory](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html#//apple_ref/doc/uid/10000172i-SW7-BCIEDDBJ) be a better option?
	- /dev/disk#
	- This could be good if you could somehow extrapolate the disk location from the UUID.
	- /Volume/mount-point
	- I don't like this option
- [ ] Add an off option
	- Since the script is being run over and over it could check for a switch
	- Maybe a file on the desktop or something
- [ ] Make a wiki to breakup the READMEs
	- Hardware suggestions page
	- Installation page
	- Configurable's
- [ ] config.py automatically assigning username
	- could easily get `whoami` into a var to build the logoff command with
- [ ] Can the plist be loaded from a `ln`?
	- This would allow the plist to then live in the repo directory
- [ ] Is there any long term damage from having the log files?
	- Should the automatically cleanup?
- [ ] Could installation be turned into a script or makefile?
- [ ] Branch the current project and go back to a 'keep alive' plist
	- The interval plist doesn't run quickly enough
	- [ ] Go back to a while loop with delay
- [ ] ISSUE: it appears when the computer falls asleep it will trigger the logout event.
	- I don't know if it is a certain duration after maybe locking. Where the script could check to see if computer is locked and stop running script?
