
###### OPSEC
- Following enumeration is not OPSEC safe for a Red Team assessment
## RunAs


## Service Discovery



## Process Discovery



## Security Software and Controls



## Account Discovery 



## Network Sniffers, Ping Sweeps & Port Scans



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
#  Host Enumeration
• Get-SystemDrivesWMI: Lists all local and network connected drives on target system
• Get-ActiveNICSWMI: Lists all NICs on target system with an IP address

• Invoke-RemoteScriptWithOutput: Executes a powershell script in memory on the
target host via WMI and returns the output
• Invoke-SchedJobManipulation: Allows you to list, delete, or create jobs on a system 

# User Operations
• Find-ActiveUsersWMI: Checks if a user is active at the desktop on the target machine
• Get-ProcessOwnersWMI: Returns all accounts which have active processes on the target syste

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

```
numeration
• Get-SystemDrivesWMI: Lists all local and network connected drives on target system
• Get-ActiveNICSWMI: Lists all NICs on target system with an IP address
System Manipulation Operations
• Invoke-CreateShareandExecute: Creates a share, copies file into it, uses WMI to invoke the script
• Invoke-RemoteScriptWithOutput: Executes a powershell script in memory on the target host via WMI
• Invoke-SchedJobManipulation: Allows you to list, delete, or create jobs on a system over WMI
• Invoke-ServiceManipulation: Allows you to start, stop, create, or delete services on a targeted system
• Invoke-PowerOptionsWMI: Force logs off all users, reboots, or shuts down targeted system
```
### Notes | Bonus
- Create Links to this Page!

