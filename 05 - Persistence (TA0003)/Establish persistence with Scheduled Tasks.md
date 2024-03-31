#### Tags: 

## Objectives
    Establish persistence on wk01.draconem.corp with two methods
    Create a Scheduled Task using a persistence module
    Examine the Indicators of Compromise (IoC) from that module
    Create a shortcut, .lnk file, on the user's desktop
    Backdoor the shortcut, .lnk file, using a persistence module

### Launch [[Empire C2#Create an Empire listener|Empire & Starkiller]]

##### Operational Security
In real engagements, we should take the following into consideration:
1. **RDP:** Service will not be accessible directly to workstations
2. **Redirector:** Traffic must be redirected
3. **Interaction:** 
	- Inbound traffic must go through a Pivot to the target workstation.
	- Outbound traffic must go direct to the redirector.

### Execute Stager on wk01.draconem.io - Create [[Creating and Testing Payloads#PowerShell HTTP Stager with rundll32.exe|interactive HTTP PowerShell Stager & Execute via rundll32.exe or PowerShell console]]


## Establish Persistence with Scheduled Tasks

![[Pasted image 20240331062433.png]]

### Examine IoCs


### Create Shortcut to Backdoor


## Establish Persistence with Backdoored .LNK

![[Pasted image 20240331062359.png]]

### Examine IoCs


#### Notes | Bonus


## Conclusion

