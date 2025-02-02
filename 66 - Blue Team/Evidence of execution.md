
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

### Tool
- RegEdit (Easiest)
### Location
- Artefact: `KEY_CURRENT_USER > SOFTWARE > CLASSES > Local Settings > Software > Microsoft > Windows > Shell > MUICache` 
	- `KEY_CURRENT_USER > SOFTWARE > CLASSES > Local Settings > MUICache`
	
- Stored in each user USRCLASS.dat > `KEY_CURRENT_USER > SOFTWARE > CLASSES`
	- This is the location of USRCLASS.dat on a Live System!
### Overview
- Easy artefact > Allows us to check PER User artefact of execution for GUI based programs w/o timestamp of execution.

- *Purpose:* Introduced in Windows 2000 for multi-language support. 
	- 1 binary can be used in different language

- *Technical Usage:* Binary has version info section > metadata of the executable
	- This is what we see in RegEdit
### Limitations
-  No timestamp of the execution
	- Values will not have the timestamp but the Reg Keys does
	- We could find that MuiCache was last updated at XX but cant say which set of values were updated in this Key. As there is no Most Recently Used here!
### Example
![[Pasted image 20250202171653.png]]
- Every GUI executed will have 2 values
	- ApplicationCompany
	- FriendlyAppName

- Even if a threat actor renames the binary > MUICache will pull the metadata and help us to see what was really executed
	- Everything GUI being executed will be tracked and populated here even if its from a different drive or USB.

----

## UserAssist

### Tool
- Parsing required
- RegistryExplorer
	- GUI 
	- CMD > ReCMD.exe > Preferred > Large Scale of data
- RegEdit

- Eric Zimmerman Tools > ReCmd.exe > Batch Examples > Kroll_Batch.reb > UserAssist is one of the artefacts collected by this Batch File
### Location
- Stored in NTUser.dat whereas MUICache is stored in USRClass.dat
- `HEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`\
	- CEB SubKey > Count - Tracks Application execution
	- F4E Subkey > Count - Tracks Links Files

### Overview
- Per user evidence of execution artefact for GUI Programs with LAST execution timestamp in UTC.
	- Stored in NTUser.dat whereas MUICache is stored in USRClass.dat

- *Purpose:* Trust but verify with other artefacts.

- *Technical Usage:* ROT 13 is used by this Key

### Limitations
- Recent version of Windows parsing of this artefact has been having inconsistencies. 
	- Always make sure to check different artefacts to confirm Story!
![[Pasted image 20250202180258.png]]

### Example
![[Pasted image 20250202180614.png]]


---
## SRUM (System Resource Utilization Monitor)

### Tool Used
SRUM is stored in a DB > Parse the data > Need to grab its DB copy, we can leverage volume shadow copy `vssadmin list shadows`
- Extract Volume Shadow Copies: There is a kape target that can pull this artefact or use FTK imager.

**FTK Imager method to grab a copy of SRU
- File > Add evidence item > Physical drive > Chose the OS drive
	- Go to Root > Windows > System32 > Select SRU > Rclick > Export Files > Save on Desktop
- Software Hive - Tool that will parse this artefact, will leverage this to resolve network information
	- Go to Root > Windows > System32 > Config > Select Software & Grab its Transactional logs as well > Rclick > Export Files > Save on Desktop

**Parse data via SrumECmd.exe (Zimmerman Tool) 
- SrumECmd.exe
	- `-d` will look for SRUDB.dat and Software Hive
	- `--csv` output location

### Location
- Database: `C:\Windows\System32\sru\SRUDB.dat`
	- All other files are transactional logs and supporting files.
![[Pasted image 20250202183905.png]]
### Overview
- Goes way beyond artefact of execution
	- Usually for 60 to 30 days, it will collect the following usage: 
		- Energy 
		- Network related connectivity
		- Detailed application 

- *Technical Usage:* Open Task Manager > App History > All of the data is being fetched from SRUM. 
	- Backend this information is stored in a Database.

### Limitations 


### Example
![[Pasted image 20250202190542.png]]

----
## Template > Common categorisation
### Tool Used

### Location

### Overview

- *Purpose:*

- *Technical Usage:*

### Limitations


### Example
