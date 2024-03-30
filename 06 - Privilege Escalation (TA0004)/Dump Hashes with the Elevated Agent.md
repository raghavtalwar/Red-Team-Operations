#### Tags: [[06 - Privilege Escalation (TA0004)]] [[Empire C2]]

## Overview 
- Goal

```markdown
```
Always while operating, check Agent or PowerShell for the following:
1. Integrity - High
2. Running as - System
3. Arch / Bit - 32 Bit or 64 Bit PowerShell Process

This is due to the fact that the binary we compiled with PowerUp is only 32-bit and there is not a 64-bit option.

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