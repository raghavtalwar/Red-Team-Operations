
#### Tags: [[]] | #

## Registry 


## Network 
What is the VPN connection this host connected to?
```markdown
# Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles
```
![[Pasted image 20240930194719.png]]

When was the first VPN connection observed? (Format: YYYY-MM-DD HH:MM:SS)
```markdown
# C:\Users\Administrator\Desktop\Artifacts\SYSTEM: ControlSet001\Services\ProtonVPNCallout
```

There were three shared folders observed on his machine. What is the path of the third share?
```markdown
# C:\Users\Administrator\Desktop\Artifacts\SYSTEM: ControlSet001\Services\LanmanServer\Shares
```
![[Pasted image 20240930200031.png]]

What is the Last DHCP IP assigned to this host?
```markdown
# C:\Users\Administrator\Desktop\Artifacts\SYSTEM: ControlSet001\Services\Tcpip\Parameters\Interfaces\{ea458d05-f4ab-48d2-9a67-97fb05ce3a76}
```

The suspect ran multiple commands in the run windows. What command was run to enumerate the network interfaces?

- RunMRU is when a user enters a command into the START > Run prompt. Entries will be logged in the user hive under: Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
```markdown
# C:\Users\Administrator\Desktop\Artifacts\NTUSER.DAT: Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
```
![[Pasted image 20240930202206.png]]

In the file explorer, the user searched for a network utility to transfer files. What is the name of that tool?
```markdown
netcat
# C:\Users\Administrator\Desktop\Artifacts\NTUSER.DAT: Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery
```

What is the recent text file opened by the suspect?
```markdown
# C:\Users\Administrator\Desktop\Artifacts\NTUSER.DAT: Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
```

How many times was Powershell executed on this host?
and
The suspect also executed a network monitoring tool. What is the name of the tool?
and
Registry Hives also notes the amount of time a process is in focus. Examine the Hives. For how many seconds was ProtonVPN executed?
and
Everything.exe is a utility used to search for files in a Windows machine. What is the full path from which everything.exe was executed?
```markdown
# C:\Users\Administrator\Desktop\Artifacts\NTUSER.DAT: Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count
```
![[Pasted image 20240930203053.png]]

### Cheatsheet
![[Pasted image 20241005154853.png]]

![[Pasted image 20241005154916.png]]