
### Objectives

    SSH to the bastion host
    Request the website at 10.199.2.120 through the bastion host
    Pivot to 10.212.243.13 through the bastion with a forward tunnel to port 22
    Catch the beacon on pivot-1 on port 58671
    Find the port for the FTP Server on 10.212.243.13
    Review the walkthrough
##### Scenario for Pivoting
Attacker Machine > Pivot Machine > Target Machine
1. Once we gain access to the Pivot Machine
2. `ipconfig / ifconfig` > We are connected to a another network
3. Check other Live Machines on that Target Network
4. Scan for Open Ports > Target Machine
##### Scenario for Local & Remote Port forwarding (with SSH) 
Attacker Machine </> Pivot Machine
- We might discover Services running on Localhost or on another internal network range
	- Internal ports can be reached by a Threat attacker via Port Forwarding
##### Scenario for Dynamic Port forwarding (Tunneling)
Attacker Machine < Pivot Machine
- EDR Bypass: We can create a Dynamic port forwarding socks Tunnel

##### Scenario for Redirection


```markdown
sec565@slingshot:/labs/sec-2/pivoting/backup$ ls
config  config-with-comments  id_ed25519

# SSH to the bastion host

```
-----
# Port Forwarding

## [[Local Port Forwarding]]

### Overview
**Bastion Host** - Bastion Hosts are an amazing way to provide secure access from a public internet 
to a private subnet.
- In certain network configurations, the bastion host is hardened and available on the public internet.
- The key is to configure this host to have as little attack surface as possible, resiliency to internet traffic, and to perform authentication on incoming connections.

Challenge 1: The next challenge is to forward a port to view a web server on an internal network. The address is 10.199.2.120 and it is listening on port 80.
### Enumeration 


### Exploitation
```markdown
# SSH Command
ssh -p 2222 bastion@pivotclub -L 0.0.0.0:5080:10.199.2.120:80
```
![[Pasted image 20240206224447.png]]
#### Notes
```markdown
# Syntax Formatting
- L <local_port>:<remote_host>:<remote_port>.
	- In Local port forwarding, <Local Port> comes first whereas
	- Remote port forwarding we <Remote Port> comes first
```

-----
## [[Remote Port Forwarding]]

Fill from Gitbook & PwC Notes
### Overview

### Enumeration 

### Exploitation
#### Notes

-----
## [[Dynamic Port Forwarding]] 

### Overview
Challenge 2: The next challenge is to create a forward tunnel to view a web server on an internal network. The address is 10.199.2.120 and it is listening on port 80.
### Enumeration 

Learn how can we identify the internal network range that is only accessible by the Pivot Machine
- Attacker Machine > Pivot Machine > Target Machine
```markdown
# Network
```
### Exploitation
```markdown
# SSH 
ssh -p 2222 bastion@pivotclub -D 9050
- Proxychains config
cat /etc/proxychains.conf
	+ socks4 	127.0.0.1 9050  

# Proxychains to reach internal subnet
proxychains curl http://10.199.2.120
```
#### Notes

-----
# Pivoting

## [[Double Pivoting via SSH]]

### Overview
Challenge 3: The next challenge is to SSH to the pivot host (Target host) through the bastion. 
The address is `10.212.243.13` with `user: tyler and password: fightclub`
- We will use the bastion host to communicate with a Jumphost or an intermediary host. In the first method we will use a forward tunnel to the second SSH host in order to connect.

### Enumeration 

### Exploitation
```markdown

```
![[Pasted image 20240206233249.png]]
#### Notes

----
## [[Pivoting w/o SSH - Chisel (HTTP Tunnel)]] 
### Overview

### Enumeration 

### Exploitation

#### Notes
- Method works on both Linux & Windows

----
## [[Pivoting w/o SSH - Socat]] 
### Overview

### Enumeration 

### Exploitation

#### Notes
- Method works on both Linux & Windows

----
## [[Pivoting w/o SSH - SShuttel]] 
### Overview

### Enumeration 

### Exploitation

#### Notes

-----
## Research | Bonus

[Tunneling and Port Forwarding Cheat Sheet](https://github.com/twelvesec/port-forwarding)

1. Link SSH , Proxychains Configuration & its Usage > Access Methods with this one
	1. Simple method is to take a page and see how can you link it to other pages

#### [[Proxychains Cheatsheet & Configuration]]
```markdown



# Proxychains in action
proxychains curl http://10.199.2.120
```

## Conclusion

