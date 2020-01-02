# MacOS_KillKey
A script that watches for a UUID to be no longer present and locks, logs out, or shuts down your mac

This is just a placeholder for my idea and notes.

`system_profiler SPUSBDataType | grep *device uuid*`  
`ioreg -p IOUSB | grep *device name*`

This could be a simple bash script or c or python or whatever that just every few seconds checks for the device. If its not there then:  
`shutdown -r now`  
[] TEST: Will the command below invoke 'FileVault' when logging back in.  
[] TEST: Will it save previous session: "Reopen windows when logging back in"  
`sudo launchctl bootout user/$(id -u <username>)`  

---
## Concerns
[] Speed, resource use  
[] Ability to interrupt the script  
[] failure of the script starting or stopping prematurely

---
## External resources
I found [this](https://tech.michaelaltfield.net/2020/01/02/buskill-laptop-kill-cord-dead-man-switch/) for Linux. 