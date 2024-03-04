
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
```markdown

```
### Exploitation
```markdown
### SSH Command
# Local port forwarding
ssh -N -L $LOCAL_ADDRESS:$LOCAL_PORT:$REMOTE_ADDRESS:$REMOTE_PORT user@target

# Remote port forwarding
ssh -N -R $REMOTE_ADDRESS:$REMOTE_PORT:$LOCAL_ADDRESS:$LOCAL_PORT user@target
```
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

**Scenario: Attacker Machine > Bastion / Pivot Machine > Target Range > Target Host** 
### Enumeration 
Identifying range
```markdown
# Scan Envrionment for Live Machines via Ping
for i in $(seq 1 254); do (ping -c 1 10.2.2.${i} | grep "bytes from" &); done;

# Alternative to Nmap Scan via Netcat
for p in $(seq 1 65535); do (nc -nvzw1 192.168.56.101 $p 2>&1 | grep open &); done
(UNKNOWN) [192.168.56.101] 1194 (openvpn) : Connection refused
(UNKNOWN) [192.168.56.101] 8080 (http-alt) open

# Fast Nmap Via Proxychains Trick using xargs and multithreading
- To scan 65535 ports at a normal speed :
seq 1 65535 | xargs -P 50 -I port proxychains -q nmap -p port -sT -T4 10.42.42.2 -oG 10.42.42.2 --open --append-output 10.42.42.2 -Pn -n
```
### Exploitation
```markdown
# Method 1 - Local Port Forwarding + SSH into the Target host
ssh -p 2222 bastion@pivotclub -L2223:10.212.243.13:22

# Method 2 - Single SSH Command to gain access to the Target host
ssh tyler@10.212.243.13 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -J bastion@pivotclub:2222

- Before you exit the SSH session in your first terminal window, run ifconfig and take note of the two network adapters.
```
![[Pasted image 20240206233249.png]]
#### Notes
- Local and Remote port forwarding both will make the Target machine port accessible from the Attacker machine
- When you are ready to tear down / close the SSH sessions and tunnels, (Double Pivoting via SSH)
	- Start from the inner most tunnel. If you try to kill your initial bastion connection, SSH will leave the exit in a pending status until inner tunnels/sessions have had a chance to exit.
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

