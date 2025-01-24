
### HKCU
- UsrClass.dat - `HKCU\Software\Classes`
	- Everything under this path comes from UsrClass.dat
- NtUser.dat 
	- All of the other content from the HKCU is stored inside NtUser.dat

Cheatsheet: https://13cubed.s3.amazonaws.com/downloads/windows_registry_cheat_sheet.pdf

#### UsrClass.dat
2 main Artefacts 
1. MuiCache - Evidence of execution
2. ShellBags - Windows Explorer artefact (Browsing paths like Bags6MRU which is most recently used bag)

##### Shell Bags 
- Zip Files are treated as Folders and Logged within Shell Bags
- Files are not tracked except Zip Files in Shell Bags 
- Only tracks Folders when using Explorer not PowerShell / Etc

##### Shell Bags Explorer by Eric Zimmerman
- 2 Options - Load active registry or Load offline hive
- Most Shell Bags are located in UsrClass.dat
- Desktop and Network locations like `\\ComputerName\c$\` are stored in NtUser.dat

**Real world example**
1. We would get handed an image
2. Mount the image via Arsenal Image Mounter
3. Pull off UserClass.dat and NtUser.dat from the users of interest.
4. Use ShellBags explorer > Load offline hive option to load those hives and investigate.

-----
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
**Location of ShimCache Database:** `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache`
- Entries will be pulled from here. Size for *Maximum ShimCache entries* on newer > Windows 2008 and above > 1024 entries
- There can be multiple ControlSet having their own ShimCache DB.


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