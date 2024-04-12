
###### OPSEC
- Following enumeration is not OPSEC safe for a Red Team assessment
## RunAs


## Service Discovery



## Process Discovery


## Security Software and Controls



## Account Discovery



## Network Sniffers, Ping Sweeps & Port Scans


## WMIC for Discovery
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


# File Search


# Local User Account


# Domain Enum
```