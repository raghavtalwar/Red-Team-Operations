#### Tags: [[06 - Privilege Escalation (TA0004)]] [[Empire C2]]

## Overview 
- Goal: Use our elevated agent to pull password hashes using mimikatz. 

### Operating via Agent or PowerShell
Always check for the following:
1. Integrity - High
2. Running as - System
3. Arch / Bit - 32 Bit or 64 Bit PowerShell Process

This is due to the fact that the binary we compiled with PowerUp is only 32-bit and there is not a 64-bit option.
- If we run mimikatz with this agent, it will fail due to the architecture mismatch. In fact, many of the modules will not function properly with this 32-bit agent. 

### PowerShell Process
On 64-bit Windows, the System32 folder holds the 64-bit binaries and the SysWOW64 folder holds the 32-bit binaries. Remember that WOW64 stands for "Windows 32-bit on Windows 64-bit"

`32-bit (x86) PowerShell is located at %SystemRoot%\SysWOW64\WindowsPowerShell\v1.0\powershell.exe

`64-bit (x64) PowerShell is located at %SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe

![[Pasted image 20240331023805.png]]
## Enumeration 

```markdown
```

## Exploitation 

```markdown
```

![[Pasted image 20240331023854.png]]

#### Notes | Bonus


## Conclusion
In this lab we took advantage of our foothold on wk01.draconem.io. 
- First, we had to make sure it was safe to operate. We used Seatbelt to pull a lot of information from the system, we reviewed the results and didn't notice anything particularly risky to our engagement.
- Then we continued host-based discovery in search of Privilege Escalation opportunities with PowerUp. 
- Once we found the unquoted service path we had to jump through a few hoops to take advantage of it. 
- In the end we were able to elevate to SYSTEM and we dumped password hashes! Now we have a new password hash for the user Wesley.Thurner.