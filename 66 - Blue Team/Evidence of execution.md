
## Prefetch
- Evidence of execution + File referenced
	- Its a process that creates a record of files that have been executed
	- Windows uses this to enhance the spin up of executables
- Note: Delta - 10 seconds is what we need to subtract from creation and modification date. As prefetch process might take that many seconds to actually monitor execution and update its record.
- Eric Zimmerman tool to review PF files is PECmd.exe
- Example: sdelete which is an sysinternal tool is being used to clear all prefetch files.
	- If we analyse this via PECmd.exe > we can see that under 'File referenced' > All the deleted files have been referenced
- **System32 is the 64-bit Windows system directory and SysWOW64 is the 32-bit Windows system directory** — entirely the opposite way
	- Example: Malware are mostly written in 32 bit as an 64 bit operating system will execute an 32 bit binary but 32 bit wont execute 64 bit. So if we analyse the pf of an malware executable on an 64 bit system and its referencing 32 bit files then maybe we can conclude it's an malware. 

Cons: Not present on Windows Server.

-----
## Shimcache / AppCompatCache
- Shimming an executable to make it compatible with newer version of Windows

**Location of ShimCache Database:** `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache`
- Entries will be pulled from here. Size for *Maximum ShimCache entries* on newer > Windows 2008 and above > 1024 entries
- There can be multiple ControlSet having their own ShimCache DB.

**Eric Zimmerman Tools** 
`AppCompatCacheParser.exe
- Perform analysis via Timeline Explorer
- Timeline Explorer marks "Yes" under "Executed"
#### Determine current control set
In a dead box forensic image > There will be multiple ControlSet1.. ControlSet2.. and no CurrentControlSet Folder!

- SYSTEM > Select > Current - The value of the key can be used to determine the current / most recently used control set 
![[Pasted image 20250123184448.png]]

#### Determine Execution / Limitations
- Leverage other forensic artefacts alongside to verify execution! [[Registry Forensics#Prefetch]]
- Timestamp - ShimCache Tracks Modification Time
	- It is not the time something executed
	- Example: Threat actors does time stopping which is uploads Evil.exe inside Temp Folder. Before moving the file to its final location of execution. 
		- If the threat actor moves this file OR changes its name - The modification timestamp will not change as the content of the file have not been changed. 
		- Thus, ShimCache DB shows us 2 Files with 2 different paths but with the *exact same timestamp* > That can confirm its the same file either renamed / moved. 
- Cache Entry Position (Numerical) - The lower the number means recently shimmed files
	- Example continued - Threat actor renamed and moved the Evil.exe to Svchost.exe, At this point the file will be re-shimmed again > And the cache entry position will be lesser now.
	- Thus, Last modification timestamp being used as a Hash to confirm "File rename"
- ShimCache is written on reboot or shutdown
	- Contents are flushed into the SYSTEM registry hive
	- Example: System has been compromised, As an investigator after acquiring volatile memory (Step 1) > Asked the customer to reboot the Server to flush the ShimCache (Step 2)
	- New Update: Volatility 3 now includes a plugin called `windows.shimcachemem` that parses this artifact from memory.

Cons: This will not track native windows binary such as PowerShell, CMD

---
## AmCache
- Location: `C:\Windows\AppCompact\Programs\AmCache.hve` &  Transactional: `.lOG.1` files
- Registry Explorer being used to load the artefact
- 3 Important sub keys under Root:
### Inventory Applications
- Installed applications
- Example: Things which get showed up in Add / Remove 
### Inventory Application File
- Loose standalone executable

### Inventory Driver Binary
- Drivers

----
## PCA
- Windows 11 artefact

---

## MUICache


----

## UserAssist

---
## SRUM


----
#### Common categorisation
1. Tool Used
2. Location
3. Overview
4. Limi
