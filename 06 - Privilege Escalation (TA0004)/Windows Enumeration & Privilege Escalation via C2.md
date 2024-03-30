#### Tags: [[12 - Command and Control (TA0011)]]

## Objectives
    Conduct Host-Based Discovery
    Search for Privilege Escalation
    Escalate to SYSTEM
    Dump Password Hashes

### Launch [[Empire C2#Create an Empire listener|Empire & Starkiller]]

### Execute Stager on wk01.draconem.io - [[Creating and Testing Payloads#PowerShell HTTP Stager with rundll32.exe|Create interactive HTTP PowerShell Stager & Execute via rundll32.exe or PowerShell console]]

### Operational Security
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

![[Pasted image 20240330182528.png]]
### Review Seatbelt Results
Each section throws information back at us, we should know how to interpret those results!

1. *Antivirus check:* Failed then review the Process list to identify security products.
2. *ARPTable check:* The ARPTable section will show relevant network interfaces and the ARP cache.
	1. ARP cache entries are short lived, the information is usually reliable. The cache may reveal other targets in the same network segment.
	2. The network interfaces are important as you begin to create a network map of the targets and any device that sits on two networks, has multiple adapters, is a **valuable target**.
3. *DNSCache check:* The DNSCache should direct you to the DNS servers in the network.
4. *DotNet check:*
5. *InterestingProcesses:*
6. *WindowsDefender:*
7. *WindowsEventForwarding:*
8. *WindowsFirewall:*

## Privilege Escalation with PowerUp
- mango
- sui

### Review PowerUp Results


## [[Unquoted Service Path Enum & Exploitation]]
### Create a Windows Service Binary

### Serve and Transfer the Payload


## Dump Hashes with the Elevated Agent


#### Notes | Bonus
- Create Links


## Conclusion