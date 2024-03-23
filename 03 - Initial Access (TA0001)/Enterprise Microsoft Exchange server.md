#### Tags: [[12 - Command and Control (TA0011)]] | [[Creating and Testing Payloads]]
## Objectives

    Scan the Microsoft Exchange server
    Use a web shell to interact with the mail server
    Execute an Empire stager on the mail server
    Export user emails
    Read user emails for target intelligence
### Scan Microsoft Exchange
```markdown
# Scan mail server
cd /labs/sec-3/initial-access/

curl https://raw.githubusercontent.com/GossiTheDog/scanning/main/http-vuln-exchange.nse -o http-vuln-exchange.nse

nmap --script http-vuln-exchange.nse mail.draconem.io
```
#### ProxyLogon
- ProxyLogon is the name for CVE-2021-26855 and CVE-2021-27065. CVE-2021-26855 is a vulnerability on Microsoft Exchange that allows authentication bypass. 
- CVE-2021-27065 is a post authentication file write vulnerability. When chained together, they allow remote code execution by allowing an adversary to bypass authentication and write a web shell to the server.
![[Pasted image 20240324024102.png]]
###### Red Team Tip: Only use web shells wiSth authentication, otherwise others could leverage your web shell.
- Note: Depending on client we can request White cell to allow us to simulate exploitation to avoid take down production servers.

### Launch [[Empire C2#Create an Empire listener]]
- Launch Empire and start an http listener on port 8080 for your tun0 interface. 

### Create [[Creating and Testing Payloads#*Payload * Create interactive HTTP Powershell Stager|Payload: Create interactive HTTP Powershell Stager]]


### Interact with the Web Shell

- WebShell Path on Target system: `C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\rt-webshell-xcowe83.aspx`
- Upload this WebShell on Private GitHub: [Arsenal/AspxRevShell at main · raghavtalwar/Arsenal (github.com)](https://github.com/raghavtalwar/Arsenal/tree/main/AspxRevShell)

### Deploy Agent on mail.draconem.io


### Enumerate Users


### Export User Emails


### Read User Emails


#### Notes | Bonus
- IIS Default Directory: `C:\Inetpub`
- Exchange Default Directory: `C:\Program _Files_\_Microsoft_\_Exchange Server_\V15\ClientAccess\Owa`
- Find a file via PowerShell `Get-ChildItem -Path 'C:\' -Recurse -Include 'rt-webshell-xcowe83.aspx' -File -Force`


## Conclusion