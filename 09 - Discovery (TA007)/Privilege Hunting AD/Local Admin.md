PowerView: https://raw.githubusercontent.com/ZeroDayLab/PowerSploit/dev/Recon/PowerView.ps1

# C2 BOF
the syntax for the Situational Awareness BOF is as follows `netLocalGroupListMembers [groupname] [optional: server]

# Manual
## Spraying


## Specific Computer / User Check

Finds users who have local admin rights over hr01 through GPO correlation.
`powershell Find-GPOComputerAdmin -ComputerName hr01
