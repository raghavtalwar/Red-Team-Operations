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


###### Red Team Tip: Only use web shells with authentication, otherwise others could leverage your web shell.

### Launch [[Empire C2#Create an Empire listener]]


### Create Interactive HTTP pwsh PowerShell Stager


### Interact with the Web Shell


### Deploy Agent on mail.draconem.io


### Enumerate Users


### Export User Emails


#### Notes | Bonus



## Conclusion