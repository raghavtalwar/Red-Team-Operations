
### Introduction
- Experience
	- Red Team & Penetration testing
	- Early this year > Blue Team
		- Bit of incident response and threat hunting. 
		- I believe this role will allow me to push myself and dive into blue team
- Value Delivered
	- End to end delivery model - i plan to use this experience to help explain customers XSS in non technical terms
	

### SOC & SIEM

SIEM

SOC
- Event viewer 
	- Event source - Application | System | Security
- Sysmon - View events + capture / monitor system activity

- Procmon - Monitor malware process upon execution

Malware analysis 
- Static
	- Strings analysis
	- File hashing
	- Metadata

- Dynamic
	- Regshot - Comparing windows registry snapshots before and after the execution of suspicious software. 
	- Fiddler - Monitor and understand network behavior of malware. Used to capture web traffic between a client and a server

- Get-WinEvent - Fetch all logs from event viewer. We can even write a PS script to export them into CSV for analysis
	- Not all company will have the budget to use a SIEM to collect logs from all servers.

### Threat landscape
Business email compromise


### Ransomware
Ransomware incident
- AWS example - On cloud its different, new VPC and resource tag and capture memory
- PsExec - Deploy it on the network


### Endpoint Forensic + Artefacts for investigation

Endpoint Forensics
- Threat actor juicy things
	- Browser attacks
	- Application
	- Configuration
	- Hardening 
	- Network
	- User
	- Creds in cleartext
