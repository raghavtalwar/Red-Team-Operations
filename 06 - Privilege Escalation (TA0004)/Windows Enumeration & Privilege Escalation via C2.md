#### Tags: [[12 - Command and Control (TA0011)]]

## Objectives
    Conduct Host-Based Discovery
    Search for Privilege Escalation
    Escalate to SYSTEM
    Dump Password Hashes

### Launch [[Empire C2#Create an Empire listener|Empire & Starkiller]]


### Create [[Creating and Testing Payloads#*Payload * Create interactive HTTP Powershell Stager|Payload: Interactive HTTP Powershell Stager]]


#### Operational Security
In real engagements, we should take the following into consideration:
1. **RDP:** Service will not be accessible directly to workstations
2. **Redirector:** Traffic must be redirected
3. **Interaction:** 
	- Inbound traffic must go through a Pivot to the target workstation.
	- Outbound traffic must go direct to the redirector.

### Execute Stager on wk01.draconem.io
#### [[Creating and Testing Payloads#*Execution Technique*|Execute interactive HTTP PowerShell Stager via rundll32.exe or ]]

## Conduct Host-Based Discovery with Seatbelt


### Review Seatbelt Results


## Privilege Escalation with PowerUp


### Review PowerUp Results


## Exploiting Unquoted Service Path
### Create a Windows Service Binary

### Serve and Transfer the Payload


## Dump Hashes with the Elevated Agent


#### Notes | Bonus
- Create Links


## Conclusion