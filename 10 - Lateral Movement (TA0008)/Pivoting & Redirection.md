
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

### Enumeration 

### Exploitation
```
sudo ssh -p 2222 -L 0.0.0.0:5080:10.199.2.120:800 bastion@127.0.0.1 -i id_ed25519
```

#### Notes

```markdown
# Syntax Formatting
In Local port forwarding, <Local Port> comes first whereas Remote port forwarding we mention <Remote Port>
```

-----
## [[Remote Port Forwarding]]

`In Local port forwarding, <Local Port> comes first whereas Remote port forwarding we mention <Remote Port>

### Overview

### Enumeration 

### Exploitation

#### Notes

-----
## [[Dynamic Port Forwarding]] 

### Overview

### Enumeration 

### Exploitation

#### Notes

-----
# Pivoting

## [[Pivoting via SSH]]

### Overview

### Enumeration 

### Exploitation

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

#### [[Proxychains & SSH Configuration]]
```markdown

```
## Conclusion

