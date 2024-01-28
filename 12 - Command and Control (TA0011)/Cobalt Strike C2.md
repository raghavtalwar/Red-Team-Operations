

### Objectives

    Review the features of Empire
    Create a listener on Empire
    Create stager payloads for your Empire listener
    Execute the stager payload on your Slingshot VM
    Interact with your Agent
    Explore Empire modules

This lab will focus on the Testing Phase of a Red Team Adversary Emulation Engagement where the Red Team prepares a Command and Control listener and creates stager payloads to connect to the listener.
## Overview 

##### Installation
- Installing & Running Empire
	- `cd /opt`
		- `git clone https://github.com/BC-SECURITY/Empire/`
	- `cd /opt/Empire`
		- `./setup/install.sh`
	-  `Run: cd /opt/Empire`
		- `sudo ./ps-empire server`

- Installing & Running Starkiller
	- `Once Empire is installed we can install the GUI for Empire known as Starkiller.
		- ``cd /opt`
	- `Download an up to date version of Starkiller from the BC-Security Github repo https://github.com/BC-SECURITY/Starkiller/releases 
		- `chmod +x starkiller-0.0.0.AppImage`
	- `Run: cd /opt`
		- `./starkiller-0.0.0.AppImage --no-sandbox`
		- `Uri: 127.0.0.1:1337`
		- `User: empireadmin`
		- `Pass: password123`

### Create an Empire listener
```markdown
# Start Empire server
cd /opt/Empire/
sudo ./ps-empire server

# Start Empire Terminal client
cd /opt/Empire/
sudo ./ps-empire client
	+ Welcome to the Empire
or
# Start Starkiller GUI client
cd /opt/starkiller/
./starkiller-1.9.0.AppImage --no-sandbox
	+ Login into Web Interface
		* Url: https://localhost:1337
		* Username: empireadmin
		* Password: password123
```
1. Click the Create button in the upper right corner of the screen.
2. Select http in the drop down menu. Then provide the following values:
	`Name:` interactive-https
	`Host:` https://10.254.252.2:443                   // IP address of your tun0 adapter
    `Port:` 8080
    `Bind IP:` 0.0.0.0
    `StagingKey:` AddSomethingRandomTo32Characters
    `CertPath:` /opt/Empire/empire/server/data
3. Leave the rest as defaults and click the SUBMIT button in the upper right corner of the screen.
	+ Note: Empire will Base64 encode the StagingKey if the string if it is not 32 characters.
4. New certificates are created by default and the next steps do not need to be taken but they are included in case you would like to generate new certificates.
	+ `sudo su
	+ `cd /opt/Empire/setup/
	+ `./cert.sh
5. Submit and now we have a listener listening!
	- `ss -tulpn > tcp LISTEN   0.0.0.0:443   0.0.0.0:*`
	
![[Pasted image 20240121151918.png]]

![[Pasted image 20240121151910.png]]
*Red Team Tip: Always set a Kill Date to ensure an agent doesn't live forever if it can not make contact with the C2 server.

### Create a stager payload
1. Create an Empire stager. Click on the suitcase icon on the left navigation window to bring up the Stagers dashboard. Then click CREATE in the upper right.
2. Select multi/launcher in the drop down menu. Then provide the following values:
    `StarkillerName:` https-slingshot-user
    `Listener: `interactive-https
    `Language:` python
3. Click the Submit button in the upper right corner of the screen.

![[Pasted image 20240123202431.png]]

### Deliver Stager - Execute the stager to create an Agent on your Slingshot Linux VM
1. 

### Agent Interaction - Ensure communication works properly 


### Modules 


## Research | Bonus


[Malleable-C2-Profiles](https://github.com/BC-SECURITY/Malleable-C2-Profiles)

#### Malleable C2 Profile
1. 

#### Network Footprinting
Lessons learned
	1. 

## Conclusion
- 


