# KillKey

## Neat Find:
I was watching this [video](https://youtu.be/-a9UjN_37lg?t=63) from seytonic and he mentions the exact circumstance this utility is trying to prevent. Click the link to watch the blerb.

## Description
This project allows you to have a physical 'key' connected to your computer. When that key is removed the computer will quickly logout keeping your data safe.

Example Situation: You are out in pulic with your laptop at a cafe or similar. Some crazy person pops out of nowhere and grabs your laptop and is gone before you can get up.

The thief knowing better leaves the lid of your laptop open and after a few minutes of running starts to go through your files. Because you were diligently working you have your password manager open and email and bank account and taxes and EVERYTHING!

If you had the KillKey on a lanyard around your wrist, chair leg, or table leg while working on the laptop as soon as the thief picked up your laptop it would be locked. Not just locked but the FileVault would have been reenabled. Sure you laptop is stolen but at least thats all.

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
		  ...
		   Product ID:
		   ...
		   Media:
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
	- Run in terminal `launchctl load ~/Library/LaunchAgents/com.user.killkeyinterval`
	- logout / login
- use `Script Editor` to make a startup app
	- `do shell script "python /path/KillKey.py"`
- manually open via terminal
	- `python /path/KillKey.py`


## Notes

This is not a [USB KILL](https://usbkill.com/). This script will do no damage to your computer\*

This is not a [BAD USB](https://maltronics.com/collections/malduinos) type device.

*it might

## FAQ

- Can I use the usb drive as a drive?
	- Technically yes but not recommended.
- What happens if I lose my key?
	- If you have setup the script to automatically run you will probably need to boot into safe mode and stop it.
	- I haven't actually tested this.
- Is there recommended hardware?
	- [see: Hardware below](#hardware)
- Does this cause: `error: gpg failed to sign the data`?
	- Yes. I have this error after using the KillKey
	- Run `gpgconf --kill gpg-agent` and it should reload and work again.

## Hardware

- `magnetic 20-pin usb-c adapter` is a good starting search string.
	- I found mine on aliexpress for about $6 shipped. When I got them they were branded 'Upmely'.
- just buy the smallest, in both dimensions and capacity, usb drive you can find.
	- I bought the SanDisk Ultra 16GB on Amazon for $7.

## TODO

- [x] running in a while 1: gets things cooking. Need to make this check every few seconds not @ 4GHz
	- Just added a sleep(1)
- [ ] Change the name? I think KillKey might not what people expect a utility like this to be called.
	- quitKey
	- securityKey
	- lanyardProtection
	-  LogOffOMatic
- [ ] Can the plist or boot script be loaded from a `ln`?
	- This would allow it to then live in the repo directory
- [ ] ISSUE: it appears when the computer falls asleep it will trigger the logout event.
	- I don't know if it is a certain duration after maybe locking. Where the script could check to see if computer is locked and stop running script?
- [ ] Investigate a dedicated hardware solution.
	- Doesn't seem work it since the hardware to make it work is already so cheap and small. And it 'looks' like a usb stick so doesn't raise suspicion.
