
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
