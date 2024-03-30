#### Tags: [[12 - Command and Control (TA0011)]]

## Objectives
    Conduct Host-Based Discovery
    Search for Privilege Escalation
    Escalate to SYSTEM
    Dump Password Hashes

### Launch [[Empire C2#Create an Empire listener|Empire & Starkiller]]

### Execute Stager on wk01.draconem.io - [[Creating and Testing Payloads#PowerShell HTTP Stager with rundll32.exe|Create interactive HTTP PowerShell Stager & Execute via rundll32.exe or PowerShell console]]

#### Operational Security
In real engagements, we should take the following into consideration:
1. **RDP:** Service will not be accessible directly to workstations
2. **Redirector:** Traffic must be redirected
3. **Interaction:** 
	- Inbound traffic must go through a Pivot to the target workstation.
	- Outbound traffic must go direct to the redirector.

----
## Host Enumeration
```markdown
# whoami
$env:username

# System name
### [System.Net.Dns]::GetHostByName(($env:computerName))

# Domain name
### [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
```


----
## Conduct Host-Based Discovery with Seatbelt


### Review Seatbelt Results

1. *Antivirus check:* Failed then review the Process list to identify security products.
2. *ARPTable check:*
3. *DNSCache check:*
4. *DotNet check:*
5. *InterestingProcesses:*
6. *WindowsDefender:*
7. *WindowsEventForwarding:*
8. *WindowsFirewall:*

## Privilege Escalation with PowerUp
- mango
- sui

### Review PowerUp Results


## Exploiting Unquoted Service Path
### Create a Windows Service Binary

### Serve and Transfer the Payload


## Dump Hashes with the Elevated Agent


#### Notes | Bonus
- Create Links


## Conclusion