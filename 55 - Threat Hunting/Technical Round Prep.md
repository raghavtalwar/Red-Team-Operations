Here are short answers tailored to your offensive security experience, aligning with the technical interview for a **Threat Hunter** role:

### **1. Incident Response (IR) Focused Questions:**

- **Detection and Response**:
  - *How would you identify and respond to an active threat in the network?*  
    **Answer**: I’d start by reviewing SIEM alerts for any anomalous behavior, isolate affected systems, and analyze logs for IoCs such as unusual outbound traffic or suspicious command execution. I’d also focus on containing the threat to prevent lateral movement.
```markdown
# Event IDs
**Event ID 4624** (successful logon)
**Event ID 4625** (failed logon)
4679 - kerberoasting | Service ticket was requested
**Event ID 4688** (process creation)
```

- **Log Analysis & Monitoring**:
  - *How do you work with SIEM systems?*  
    **Answer**: I’ve used SIEM systems like Splunk and ELK to monitor for suspicious patterns. I focus on building effective detection rules and querying logs for indicators like repeated failed logins, privilege escalations, or unusual file modifications.


  - *What are key IoCs you look for in logs?*  
    **Answer**: Key IoCs include unusual user logins, PowerShell execution, modifications to system files, registry changes, and outbound connections to known malicious IPs or domains.
```markdown
# Event IDs
unusual logins (Event ID 4624)
PowerShell execution (Event ID 4104)
registry modifications (Event ID 4657)
```

- **Forensic Investigation**:
  - *How would you investigate a compromised endpoint?*  
    **Answer**: I would collect artifacts such as memory dumps, running processes, network connections, and registry hives. I’d use tools like Volatility to analyze the memory and identify any malware signatures or persistence mechanisms.

- **Incident Handling**:
  - *How do you contain a network-wide compromise?*  
    **Answer**: First, isolate the affected machines from the network, disable compromised accounts, block malicious IPs/domains, and coordinate with the network team to segment areas at risk. Then, I’d work on identifying and neutralizing the root cause.

- **Root Cause Analysis**:
  - *How do you perform root cause analysis after an incident?*  
    **Answer**: I review logs, endpoint telemetry, and network traffic to trace back the attack to its initial point of entry, often patient zero. I then determine how the threat actor gained access and what vulnerabilities were exploited.

### **2. Threat Hunting Focused Questions:**

- **Threat Hunting Techniques**:
  - *How would you set up a hypothesis-driven hunt?*  
    **Answer**: I’d start by forming a hypothesis around an emerging threat, such as malware using PowerShell for persistence. I would focus on searching for suspicious script executions, abnormal process behaviors, or registry changes that indicate script-based malware.

  - *How would you detect lateral movement activity?*  
    **Answer**: I’d monitor for unusual SMB or RDP connections, identify abnormal Kerberos ticket-granting behavior, and look for tools like `PsExec` or `wmic` being used for unauthorized access across systems.
```markdown
# Event ID
**Event ID 4769** (Kerberos service ticket request)
```

- **Threat Intelligence**:
  - *How do you integrate threat intelligence feeds into your hunting?*  
    **Answer**: I incorporate threat intelligence to enrich my hunts by matching IoCs like IPs, hashes, and domains with data from known attack groups and their TTPs. This helps refine my detection strategies for specific threats.
  
  - *How would you track an APT in the network?*  
    **Answer**: I’d analyze their behavior using MITRE ATT&CK mappings, focusing on persistent foothold techniques like backdoors or credential harvesting. Then I’d hunt for related anomalies in network traffic and endpoint activity
```markdown
# Citrix breakout
- Weak Creds
- Predictable IDs
- No 2FA > Citrix Login > Breakout 
- Finance.exe > VersionInfo
- Temp Folder
- Purple team exercise

- Collected citrix logs
Logging in through Citrix AVD generates Event ID 4624, and when the user opens PowerShell using "RunAs" with another account, Event ID 4648 is generated.
```

- **Endpoint & Network Detection**:
  - *What anomalies would you look for in network traffic?*  
    **Answer**: I’d search for high-volume outbound traffic to suspicious domains, unusual port activity, or encrypted traffic to unexpected destinations, as these often indicate data exfiltration or command-and-control.

- **Tooling & Automation**:
  - *What tools do you use for threat hunting?*  
    **Answer**: I’ve used tools like Splunk, Elastic, Sysmon, and EDR platforms like CrowdStrike. For automation, I write scripts in Python to streamline data collection and pattern matching for quick detection of anomalies.
```markdown
# Story
- Hunting for Keylogger 
	- WINAPI calls 

- Velociraptor
	- Hunt for printnightmate vuln on host
```
### **3. Overlapping Concepts:**

- **Adversary Simulation**:
  - *How does your knowledge of offensive security inform your approach to threat hunting?*  
    **Answer**: My offensive experience gives me insight into how attackers bypass defenses. I can predict which attack vectors they’ll likely exploit, which helps me proactively hunt for those specific tactics in the network.

- **Detection Bypass Techniques**:
  - *How would you expect adversaries to bypass traditional detection, and how would you hunt for them?*  
    **Answer**: Adversaries often use fileless malware or LOLBins like PowerShell or WMI. I’d hunt by monitoring for unusual script executions, memory-based payloads, and monitoring for changes in security configurations.
```markdown
# BYOD (Story)
- Bring your own driver 
```

- **MITRE ATT&CK Framework**:
  - *How do you map adversary techniques to the MITRE ATT&CK framework?*  
    **Answer**: I use the MITRE ATT&CK framework to track TTPs. For example, I look for signs of credential dumping (T1003) or process injection (T1055) in logs and telemetry to align potential attacks with known threat behaviors.

### **4. Other Important Areas:**

- **Malware Analysis**:
  - *What’s your approach to identifying ransomware behavior?*  
    **Answer**: I’d look for signs like files being encrypted with unusual extensions, processes generating high disk usage, or abnormal use of Windows Shadow Copy deletion commands (`vssadmin`).
```markdown
# Ransomware post incident analysis (Story)
- PsExec -d > Dont wait | @ > Specify hosts
```

- **EDR/XDR and SIEM Systems**:
  - *How do you use these systems to detect attacks?*  
    **Answer**: I use EDR systems like CrowdStrike to track abnormal process execution and lateral movement. With SIEM systems, I build and refine correlation rules to detect suspicious user behavior and anomalous network patterns.
```markdown
# Direct vs Indirect Syscalls 
To combat the issue that direct syscalls bring, the way we can make our program seem more "legitimate" and not have it stick out as much is with the following: Instead of executing a syscall instruction directly in our assembly function stubs, we can instead _replace_ the syscall instruction with the address of a legitimate syscall elsewhere in ntdl.dll
Link: [Indirect System Calls | Crow's Nest](https://www.crow.rip/crows-nest/mal/dev/inject/syscalls/indirect-syscalls)
```

- **Cloud Security**:
  - *How would you hunt for threats in cloud environments?*  
    **Answer**: I would monitor cloud service logs (e.g., AWS CloudTrail) for suspicious actions like privilege escalations, unusual login times, or misconfigured access policies that could be exploited by attackers.
```markdown
# AWS Incident response (Story)
- Create new VPC & Isolate EC2 & Tag them
- Take memory dumps
- Prevent them from shutting down
```

---

This approach ties your **offensive knowledge** to a **defensive mindset**, highlighting your understanding of attacker techniques and how you can leverage that experience in the **Threat Hunter** role.

----
# Notes (Reading + Writing + Revision)

## NTFS
- Windows underlying filesystem
	- NTFS Features - Access control lists

- Important NTFS Forensic Artifacts
	- $MFT - Master File Table stores records of every file and directory
		- Keeps record of every file and directory
	- $ LogFile - Tracks MFT metadata changes
		- If MFT gets changed - maintains records
	- $UsnJrnl - Tracks file changes
		- If file was accessed or move - maintains evidence (Not for very long)
		- For ex - we can find evidence of deleted files


## Registry


## Persistence
- DLL Proxying - BlackHills
## IOC vs IOA 
### Indicators of Attack (IoA)
1. **Unusual PowerShell Activity**
2. **Suspicious Memory Usage**
3. **Abnormal Log Manipulation**
4. **Suspicious Privilege Escalation or Lateral Movement**
### Indicators of Compromise (IoC)
1. **Unusual PowerShell Execution Logs**
2. **Network Connections Initiated by PowerShell**
3. **In-memory Artifacts**
4. **Log Manipulation Evidence**
5. **Persistence Mechanisms**
## Adversary emulation (ISO Inital drop)


## High Fidelity Artefacts
1. File Analysis
	1. NTFS
		 **Small files (resident)**: Content can be stored in the MFT.
		 **Large files (non-resident)**: Content is stored outside the MFT, with pointers in the MFT to the file's location.
2. System & User Information
	1. Registry
			DEFAULT (mounted on HKEY_USERS\\DEFAULT)
			SAM (mounted on HKEY_LOCAL_MACHINE\\SAM)
			SECURITY (mounted on HKEY_LOCAL_MACHINE\\Security)
			SOFTWARE (mounted on HKEY_LOCAL_MACHINE\\Software)
			SYSTEM (mounted on HKEY_LOCAL_MACHINE\\System)
1. Evidence of Execution
	1. Background activity moderator
		1. BAM keeps track of background applications running on Windows to manage system performance.
		2. For threat hunting, I can use BAM to check if any suspicious processes were running in the background that the attacker may have used to stay hidden
	3. ShimCache - *Program that were executed
		1. Windows has a compatibility feature (ShimCache) that stores details about programs that have run, even if the malware tries to delete itself after running.
		2. Even if the malware tries to delete itself, I can use ShimCache to find evidence that it was executed
	4. Amcache - *Program that were executed + Installation or Modification date 
		1. Similar to ShimCache but more detailed, Amcache logs information about programs that were executed on the system. This includes things like when the program was installed or modified.
		2. For threat hunting, Amcache helps me dig deeper into when and what programs were run
	5. Prefetch - *Program last executed date and time*
		1. By analyzing Prefetch data, I can find out when a suspicious program was last executed, even if the attacker tries to cover their tracks.
2. Persistence Mechanisms 
	1. Run Keys - I look at Run Keys in the registry to check if any malicious programs are set to start automatically when the system boots.
	2. Startup Folder - The Startup Folder is a place in Windows where you can put shortcuts for programs you want to start when the computer is turned on.
	3. Scheduled Tasks - I check Scheduled Tasks to find any suspicious tasks set by attackers to make sure their malware continues to run at specific times.
	4. Services - Windows Services are background programs that run automatically and stay active even if you’re not logged in.
3. Event Logs

Reference: [Practical Windows Forensics for Fun and Profit w/ Markus Schober #infosec - YouTube](https://www.youtube.com/watch?v=7Z-Su-jkUnQ&t=2027s)

### Note: Startup Folder Vs Registry 
When an executable is copied into the **Startup folder** to maintain persistence, there is typically **no direct registry entry created** for that action.
- The Windows **Startup folder** is a specific directory that allows applications placed there to be launched automatically upon user login, without needing any registry changes.

However, persistence through the **Startup folder** and the registry are separate mechanisms. Here's how they differ:
1. Start up Folder - Any executable file (or a shortcut to it) placed in the **Startup folder** will automatically run when the user logs in.
	1. **Specific user**: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
	2. **All users**: `%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\StartUp`

2. Registry Method - If persistence is set up through the **Windows Registry**, an entry will be made under one of the following keys:
	-  **User-specific** (HKCU):
     `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
    - **System-wide** (HKLM): `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run`

Example: Registry Path for System-Wide Persistence (All Users):
- **Key**: `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run`
- **Value Name**: `MaliciousApp`
- **Value Data**: `"C:\malware\malicious.exe"`

----
# Ransomware scenario
### Indicators of Compromise (IOCs)
- Look for suspicious processes or anomalous memory usage using **Sysmon** or **Windows Event Logs** (e.g., Event IDs 4688 for process creation).
- IPs 
- Hashes

1. Unusual File Extensions
2. Ransom Notes - DECRYPT_INSTRUCTIONS
3. Suspicious Network Traffic
4. Changes to System Files - Some ransomware families modify system files to make the attack more effective or persistent.
5. Registry Changes - Ransomware can use the Windows registry for persistence, ensuring it runs on reboot.
6. Abnormal CPU and Disk Usage 
7. Unusual File Renaming Behavior - A high volume of file rename events or file changes in a short time frame.

### Indicators of Attack (IOAs)
**Log Clearing Activity**:
**Memory-based Attacks**:
**Command-Line Execution**:
**PowerShell Abuse**: - Behavioral patterns like PowerShell scripts that bypass execution policies, obfuscate commands, or connect to external IP addresses are strong IOAs. or Download scripts

1. Execution of Suspicious PowerShell Commands
2. Unusual Process Activity - disable system recovery options
3. Disabling Security Features - AV / Firewall
4. Suspicious Scheduled Tasks - From non standard directories
5. Unexpected SMB (Server Message Block) Traffic
6. Privilege Escalation
7. Stopping or Modifying Backup Services - Commands like `vssadmin delete shadows` or stopping backup-related services (`backup`, `shadow copy`, `system restore`). Ransomware tries to delete shadow copies and backups to prevent recovery without paying the ransom.
8. Lateral Movement Indicators - Tools like `PsExec` or `Remote Desktop Protocol (RDP)` being used to move across systems.
### Once you've identified any of these IOCs or IOAs, your threat-hunting actions would include:

- **Isolating the impacted systems** to prevent further spread.
- **Terminating suspicious processes** and blocking the IP addresses or domains associated with C2 traffic.
- **Restoring backups** if encryption has begun, but ensuring that the ransomware hasn't already tampered with backup systems.
- **Patching vulnerabilities** to prevent re-entry and reviewing access logs to identify how the attack occurred.