#### Tags: [[]] | #DFIR

## Overview 
Learn Velociraptor, an advanced open-source endpoint monitoring, digital forensic and cyber response platform.
- Rapid7's newly acquired tool known as [Velociraptor](https://www.rapid7.com/blog/post/2021/04/21/rapid7-and-velociraptor-join-forces/).
### Start the Velociraptor Server (Ubuntu Terminal)
```markdown
# Start server on Ubuntu via WSL (Windows Subsystem for Linux)
./velociraptor-v0.5.8-linux-amd64 --config server.config.yaml frontend -v

# Start client on Windows
Visit 127.0.0.1:8889

# Instant Velocptor GUI (https://github.com/Velocidex/velociraptor)
Velociraptor.exe gui
```
### Adding Windows client to Velociraptor. 
Run the commands for 'Add Windows as a client (CMD)' from the commands.txt on the desktop.
```powershell
C:\Program Files\Velociraptor> velociraptor-v0.5.8-windows-amd64.exe --config velociraptor.config.yaml client -v
```
![[Pasted image 20240929152950.png]]

![[Pasted image 20240929154036.png]]
#### Overview | Click on agent and view the additional information
- **Client ID**
- **Agent Version**
- **Agent Name**
- **Last Seen At**
- **Last Seen IP**
- **Operating System**
- **Hostname**
- **Release**
- **Architecture**
- **Client Metadata**
#### VQL Drilldown
- **Orange** - Memory usage
- **Blue** - CPU usage
- **AD Domain** 
- **Active accounts**
#### Shell
Commands can be run in PowerShell, CMD, Bash, or VQL
#### Collected
-  **Commands executed** previously from Shell.
- **VFS** (**Virtual File System**)
![[Pasted image 20240929155757.png]]
#### Interrogate

## VQL Query Lang

![[Pasted image 20240929173752.png]]

### Notes | Bonus
- Create Links to this Page!

---
## Endpoint investigation via Velociraptor

- D - Detection
- A - Analysis
- C - Containment
- E - Eradication
- R - Removal

![[Pasted image 20241020001931.png]]
### Problem Statement
- 6 to 8 hours to take a full disk image 
- Only 8 minutes with Velociraptor

![[Pasted image 20241020002000.png]]

#### Rapid Triage workflow
![[Pasted image 20241020003512.png]]
- IOCs themselves are the clues or artifacts that indicate potential malicious activity or compromise > Look around > Make a decision

**Remember: IOCs are reactive - Static - Conduct targeted hunts during major incidents > (Post incident)

##### Collection - Windows endpoint > Collect the following artifacts:
- Event Logs
- MFT 
- Tactical forensics - Insight into network via Netstat
- *Running processes with command line - FAVOURITE*
- Autoruns - Looks for persistence location
- Artifacts of execution - Things that were ran on that system (memory cache)
	- Eg: Use a tool like **Volatility** (or similar memory forensics tools) to extract and analyze memory dumps.
- Web Actions / History - Significant as well

Note: A full disk image + Memory will include the above mentioned artifacts, as full disk image does not contain volatile data from the system's memory (RAM).

Now lets see how we can achieve the above via Velociraptor (Full disk image + Memory) + KAPE (Analyzing artifacts)

![[Pasted image 20241020004902.png]]
### Velociraptor - Acquisition tool 
*Offline Collector* - This means no velociraptor server required, i provide client with an executable and it collects the data i need. 
- No Velociraptor server communication required

2 Primary reason to go this way
1. No infrastructure or communication setup needed - We can create a offline collector in few min and ask the client to upload it to a secure s3 bucket!
2. It works!

Artefacts Collection > We will select the ones shown above!
#### Build offline collector
Download Velociraptor > We can even configure our collector to upload to S3 or ZIP the file
![[Pasted image 20241020005615.png]]
#### Analysis
![[Pasted image 20241020010047.png]]

### KAPE - Post processing tool
- We will download these components shown above
- After using Velociraptor for collection > Ingest into KAPE > Run KAPE script onto the data collected > Excel & Other files created for easy reviewing of artifacts