
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
wmic /namespace:\\root\securitycenter2 path antivirusproduct

# File Search
wmic DATAFILE where "drive='C:' AND Name like '%password%’" GET Name,readable,size /VALUE

# Local User Account
wmic USERACCOUNT Get Domain,Name,Sid

# Domain Enum
wmic NTDOMAIN GET DomainControllerAddress,DomainName,Roles /VALUE
```

### Notes | Bonus
- Create Links to this Page!

