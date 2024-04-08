PowerView: https://raw.githubusercontent.com/ZeroDayLab/PowerSploit/dev/Recon/PowerView.ps1

# C2 BOF
The syntax for the Situational Awareness BOF is as follows `netLocalGroupListMembers [groupname] [optional: server]

# Windows
## Specific Computer / User Check via PowerView

Finds users who have local admin rights over hr01 through GPO correlation.
`powershell Find-GPOComputerAdmin -ComputerName hr01

# Linux
## Spraying
- CME
