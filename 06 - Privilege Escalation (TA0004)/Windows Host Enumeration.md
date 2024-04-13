
###### OPSEC
- Following enumeration is not OPSEC safe for a Red Team assessment
## RunAs


## Service Discovery
```markdown
# Get information about services on a system 
C:\> sc; tasklist /svc 
C:\> net start 
C:\> wmic service 
PS C:\> Get-service
```


## Process Discovery
```markdown
# Get info about running processes on a system. Red Team should try to understand what is installed & running - Windows C:\> tasklist C:\ wmic process C:\> Get-Process
```


## Security Software and Controls
```markdown
```


## Account Discovery 
```markdown
# Listing of local system accounts & local groups 
C:\> whoami; who; w; set 
C:\> net user; net localgroup 
C:\> wmic useraccount; wmic group - another way to fetch account info and group membership 
C:\> Get-LocalUser; Get-LocalGroup
```



## Network Sniffers, Ping Sweeps & Port Scans
```markdown
# Network Sniffers like WireShark or TcpDump - Promiscuous mode requires admin or root privileges Windows 

# Ping Sweep 

# Port Scan

```


## Local Network Enum
```markdown
# Identify network config and connections Windows 
C:\> ipconfig /all; ipconfig /displaydns - Displays the system DNS cache in Windows 
C:\> netstat -na - Display the current TCP and UDP ports being used
C:\> arp -a - ARP cache 
C:\> net session 
PS C:\> Get-NetTCPConnection
```


# WMIC for Discovery
### Overview
- WMIC is a command-line tool for controlling Windows machines via the Windows Management Instrumentation (WMI) framework
- Used to interact with systems for processes, services, startup and mor
###### OPSEC
- WMI Activity is logged in Event Log under ID 5957
```markdown
# Local System
wmic computersystem LIST full

# Target System
wmic /node:[targetIP] /user:[admin_user] /password:[password] computersystem LIST full

## Use /node:@[filename] to run command on all machines listed one per line in filename
```
### Enumeration
```markdown
# Antivirus
C:\> wmic /namespace:\\root\securitycenter2 path antivirusproduct

# File Search
wmic DATAFILE where "drive='C:' AND Name like '%password%’" GET Name,readable,size /VALUE

# Local User Account
wmic USERACCOUNT Get Domain,Name,Sid

# Domain Enum
wmic NTDOMAIN GET DomainControllerAddress,DomainName,Roles /VALUE

# List All Users:
wmic /NAMESPACE:\\root\directory\ldap PATH ds_user GET ds_samaccountname

# Members of a Group:
wmic /NAMESPACE:\\root\directory\ldap PATH ds_group where "ds_samaccountname='Domain Admins'" Get ds_member /Value

# List All Computers:
C:\> wmic /NAMESPACE:\\root\directory\ldap PATH ds_computer GET ds_samaccountname

# Execute Commands:
C:\> wmic process call create "cmd.exe /c calc.exe"
```

### Script - WMIOps
References: https://github.com/FortyNorthSecurity/WMIOps
```markdown
# Process Enumeration
• Invoke-ExecCommandWMI: Executes a user specified command on the target machine
• Invoke-KillProcessWMI: Kills a process (via process name or ID) on the target machine
• Get-RunningProcessesWMI: Returns all running processes from the target machine

# User Operations
• Find-ActiveUsersWMI: Checks if a user is active at the desktop on the target machine
• Get-ProcessOwnersWMI: Returns all accounts which have active processes on the target system

#  Host Enumeration
• Get-SystemDrivesWMI: Lists all local and network connected drives on target system
• Get-ActiveNICSWMI: Lists all NICs on target system with an IP address

# System Manipulation Operations
• Invoke-CreateShareandExecute: Creates a share, copies file into it, uses WMI to invoke the script
• Invoke-RemoteScriptWithOutput: Executes a powershell script in memory on the target host via WMI
• Invoke-SchedJobManipulation: Allows you to list, delete, or create jobs on a system over WMI
• Invoke-ServiceManipulation: Allows you to start, stop, create, or delete services on a targeted system
• Invoke-PowerOptionsWMI: Force logs off all users, reboots, or shuts down targeted system

# File Operations
• Get-FileContentsWMI: Reads the contents of a user specified file on a target system
• Find-UserSpecifiedFileWMI: Search for a file (wildcard supported) on a target system
• Invoke-FileTransferOverWMI: Uploads or downloads files to/from the target machine 
```

### Notes | Bonus
- Create Links to this Page!

