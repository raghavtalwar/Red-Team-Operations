
###### OPSEC
- Following enumeration is not OPSEC safe for a Red Team assessment
## RunAs


## Service Discovery



## Process Discovery


## Security Software and Controls



## Account Discovery



## Network Sniffers, Ping Sweeps & Port Scans


## WMIC for Discovery
###### OPSEC
- WMI Activity is logged in Event Log under ID 5957
```markdown
# Local System
wmic computersystem LIST full

# Target System
wmic /node:[targetIP] /user:[admin_user] /password:[password] computersystem LIST full
```