# MacOS_KillKey
A script that watches for a UUID to be no longer present and locks, logs out, or shuts down your mac

This is just a placeholder for my idea and notes.


---
## Check for Device
`system_profiler SPUSBDataType | grep *device uuid*`  
`ioreg -p IOUSB | grep *device name*`

This could be a simple bash script or c or python or whatever that just every few seconds checks for the device. If its not there then:  

---
## Security Lock
`shutdown -r now`  
[X] TEST: Will the command below invoke 'FileVault' when logging back in.  

 - No. Well, I just did a tradition logout via menu and that also doesn't appear to reinvoke FileVault. And by reinvoke I mean see the slider when you first logon that appears to be the filesystem doing its fileVault thing.

[X] TEST: Will it save previous session: "Reopen windows when logging back in"  

 - Yes  

`sudo launchctl bootout user/$(id -u <username>)`  

---
## Auto Start
Could just be a login item under user account  
[launchd](https://stackoverflow.com/questions/6442364/running-script-upon-login-mac/13372744#13372744), launchctl, .plist  
[] Would the script be able to check, and lock if non-sudo start?  

[Running a Job Periodically](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html#//apple_ref/doc/uid/10000172i-SW7-BCIEDDBJ)  

 - this may be better than a while loop with sleep

---
## Concerns
[] Speed, resource use  
[] Ability to interrupt the script  
[] failure of the script starting or stopping prematurely

---
## External resources

I found [this](https://tech.michaelaltfield.net/2020/01/02/buskill-laptop-kill-cord-dead-man-switch/) article for Linux.  
USB-C Magnet 90˚ [Adapter](https://www.amazon.com/Magnetic--Connector-Quick-Charge/dp/B07MMKZ8XD/ref=sr_1_3?crid=1FY699KGN2YH9&keywords=usb-c+magnetic&qid=1578008301&sprefix=usb-c+mag%2Caps%2C166&sr=8-3).  
Tiny USB-C [drive](https://www.amazon.com/SanDisk-Ultra-Type-C-Flash-SDCZ450-016G-G46/dp/B01BUSMYHC/ref=sxin_3_osp5-33b4c257_cov?ascsubtag=33b4c257-b57e-46cb-9f6d-0f9cfe520b4f&creativeASIN=B01BUSMYHC&crid=3RWB7TZ32FVGK&cv_ct_cx=usb-c+thumb+drive&cv_ct_id=amzn1.osp.33b4c257-b57e-46cb-9f6d-0f9cfe520b4f&cv_ct_pg=search&cv_ct_wn=osp-search&keywords=usb-c+thumb+drive&linkCode=oas&pd_rd_i=B01BUSMYHC&pd_rd_r=26cb7ef2-d6ff-484d-b2bf-28d7cf58c2ca&pd_rd_w=kYWcI&pd_rd_wg=0aPu5&pf_rd_p=eb3e5cda-5ec9-4d94-919d-310a5d641b8b&pf_rd_r=RCBWS4SD3EKSKD4KJ7XZ&qid=1578008333&sprefix=usb-c+thumb%2Caps%2C164&tag=androidcentralosp-20).  

 - [] Small enough to fit into magnet adapter without tail?
 - [] Could the plastic housing be removed to make it even smaller?
 - [] Perhaps remove the drive housing and just do a resin dip to make it as small as possible.
 - [] Final solution needs a lanyard attachment.

 ---
 ## Install
 The file config_example.py needs to be copied to config.py and the internal values changed. You need to find the UUID of the device you plan on using as the \*key\*.

 ---
 ## Make device
 I took an old flash drive and just did a `diskutil eraseDisk free KillKey /dev/disk#`. This should make a drive that doesn't mount when plugged in. So you will not get a "improperly ejected disk" warning when you unplug it.