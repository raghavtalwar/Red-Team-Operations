
### Objectives

    Review the features of Empire
    Create a listener on Empire
    Create stager payloads for your Empire listener
    Execute the stager payload on your Slingshot VM
    Interact with your Agent
    Explore Empire modules

This lab will focus on the Testing Phase of a Red Team Adversary Emulation Engagement where the Red Team prepares a Command and Control listener and creates stager payloads to connect to the listener.
## Overview 

##### Installation:
- Installing & Running Empire
	- `cd /opt`
		- `git clone https://github.com/BC-SECURITY/Empire/`
	- `cd /opt/Empire`
		- `./setup/install.sh`
	-  `Run: cd /opt/Empire`
		- `./empire --rest`

- Installing & Running Starkiller
	- `Once Empire is installed we can install the GUI for Empire known as Starkiller.
		- ``cd /opt`
	- `Download an up to date version of Starkiller from the BC-Security Github repo https://github.com/BC-SECURITY/Starkiller/releases 
		- `chmod +x starkiller-0.0.0.AppImage`
	- `Run: cd /opt`
		- `./starkiller-0.0.0.AppImage`
		- `Uri: 127.0.0.1:1337`
		- `User: empireadmin`
		- `Pass: password123`

### Create an Empire listener


```markdown
# Start empire server

# Start empire client

```

### Create a stager payload


```markdown

```

### Execute the stager to create an Agent on your Slingshot Linux VM


```markdown

```

### Ensure communication works properly


```markdown

```

### Review the walkthrough

```markdown

```


## Research 

[Empire: Empire is a post-exploitation and adversary emulation framework](https://github.com/BC-SECURITY/Empire)


[Starkiller: Starkiller is a Frontend for PowerShell Empire.](https://github.com/BC-SECURITY/Starkiller)


[Malleable-C2-Profiles](https://github.com/BC-SECURITY/Malleable-C2-Profiles)

#### Malleable C2 Profile
- **Practical C2 Example:** Imagine you have a Beacon payload (a component of Cobalt Strike) implanted on a target system. The Beacon communicates with a Command and Control server controlled by an attacker.
- **Malleable C2 Profile:** The Malleable C2 profile in this context is like a script that defines how the Beacon communicates with the C2 server.  It defining how the network traffic should appear to evade detection.
	- For example, the profile may specify:
		- **Redirectors**
		- **User-Agent Spoofing:**
		- **Custom Encryption:**
		- **DNS Tunneling:**
		- **Custom Headers:**
		- **Sleep Time and Jitter:**
		- **Proxy**
		- **HTTP Methods:**
		- **Encrypted and Authenticated Communication:**
		- **Data Exfiltration Techniques:**
		- **Domain Generation Algorithms (DGA):**
		- **Dynamic Profile Switching:**
		- **Anti-Sandbox Techniques:**
		- **Payload Encoding:**
		- **Dynamic Payload Generation:**
		- **Protocol Mimicking (e.g., Mimicking DNS Over HTTPS - DoH):**

## Conclusion




