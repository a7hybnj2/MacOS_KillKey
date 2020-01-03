# KillKey
This project allows you to have a physical 'key' connected to your computer. When that key is removed the computer will quickly logout keeping your data safe.

## Contributing
I would be very happy if someone was interested in taking a look at this and suggesting improvements. This is one of my first python projects and is my first time using plists to start scripts.

## Installation and Setup
1. Clone or download this repo to your computer
2. Open the repo and copy the two .example files and remove the .example extension
3. Create the hardware 'key'  
    1. Plug a thumb drive into your computer.
    2. Run in terminal `diskutil list`
    3. Note the path for your usb thumb drive
    4. Run in terminal `diskutil eraseDisk free KillKey /YOUR_PATH_HERE`
        - This will remove the filesystem from the disk and prevent it from showing up as a storage device. It will also prevent it from being mounted which means you will not get the "improperly ejected" warnings.
    5. Run in terminal `system_profiler SPUSBDataType`
    6. Note the UUID listed for your USB Drive
4. Edit config.py
    1. Change `device_uuid` to your UUID you took note of earlier
    2. Change `logout` so that `*username*` is replaced with your username
5. **TEST**  
    1. Now you should be able to test to make sure you have your config.py setup correctly.
    2. Open the repo in a terminal and `./KillKey.py`
    3. If your drive is plugged in you will see `FOUND` in the stdout
    4. If you have your drive removed and you run it you will see `NOT FOUND` very quickly before getting logged out of the system.
5. Edit com.user.killkeyinterval.plist
    1. Change the `<array><string>` to match your python install path
    2. Change the `<array><string><string>` to match the path to the KillKey.py file.
        - This cannot include globbing. 
    3. Change the `<key>StandardErrorPath</key><string>` to be in a location of your choosing.
        - I kept mine inside the repo folder
    4. Do the same for `<key>StandardErrorPath</key><string>`
        - Keep the log filenames different unless you want both standard out and errors in one file.
    5. Change `<integer>` to a the duration between running the script
        - I am currently using `1` and am not having any negative issues as of now.
6. Copy `com.user.killkeyinterval.plist` to `~/Library/LaunchAgents/`
7. Run in terminal `launchctl load ~/Library/LaunchAgents/com.user.killkeyinterval`
8. Logout
9. Login

# Warning
Once you have this installed you will have to have the 'key' installed to log into the machine. If you don't then as soon as you log in you will get logged back out. If you need to stop this you can `launchctl stop com.user.killkeyinterval` and/or `launchctl unload com.user.killkeyinterval` if you don't want it run again.

# Notes:
This is not a ['USB KILL'](https://usbkill.com/). This script will do no damage to your computer*  
    - * haven't tested what would happen if you lost the 'key'  
This is not a ['BAD USB'](https://maltronics.com/collections/malduinos) type device.

# FAQ:
- Can I use the usb drive as a drive?
    - Technically yes but not recommended.
- What happens if I lose my key?
    - Unknown, its **untested**.
- Is there recommended hardware?
    - There will be a wiki page on hardware.
- Does this cause: `error: gpg failed to sign the data`?
    - It seems to mess it up somehow. Probably because of the 'FORCE' logout.
    - Run `gpgconf --kill gpg-agent` and it should reload and work again.

# TODO:
- [ ] Does the plist prevent sleep?  
    - `pmset -g assertions` doesn't seem like it  
- [ ] Would [Monitoring a Directory](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html#//apple_ref/doc/uid/10000172i-SW7-BCIEDDBJ) be a better option?  
    - /dev/disk#
        - This could be good if you could somehow extrapolate the disk location from the UUID.  
    - /Volume/mountpoint
        - I don't like this option  
- [ ] Add an off option  
    - Since the script is being run over and over it could check for a switch  
        - Maybe a file on the desktop or something  
- [ ] Make a wiki to breakup the READMEs
    - Hardware suggestions page
    - Installation page
    - Configurables
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