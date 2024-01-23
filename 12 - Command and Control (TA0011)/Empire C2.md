
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

### Execute the stager to create an Agent on your Slingshot Linux VM
1. **Deliver** your stager to Slingshot Linux. On the Stagers dashboard, click the three vertical dots icon under actions to bring up the actions menu. Click Copy to Clipboard.
2. **Execute:** Open up a new terminal window as the user sec565 and enter Ctrl+Shift+v to paste the stager code. You can see here that we are echoing python code into python3. The stager is base64 encoded by default.

![[Pasted image 20240123204357.png]]
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
		- **Redirectors:** Redirectors are used to hide the true C2 server by acting as an intermediary. When an infected system attempts to communicate with the C2 server, it is redirected through the redirector. This adds a layer of obfuscation, making it more challenging for defenders to identify and block the malicious traffic.
		- **User-Agent Spoofing:** Customizing the User-Agent string allows the malware to mimic legitimate user agents, making it harder for network defenders to identify malicious traffic based on this attribute.
		- **Custom Encryption:** Encrypting C2 traffic helps in avoiding signature-based detection. Malleable C2 profiles often allow users to customize encryption algorithms, keys, and other parameters.
		- **DNS Tunneling:** Instead of traditional HTTP or HTTPS traffic, some C2 frameworks support DNS tunneling, where communication occurs through DNS requests and responses, making detection more challenging.
		- **Custom Headers:** Modifying and customizing headers, such as User-Agent or Referer, helps to make the C2 traffic look more like legitimate traffic.
		- **Sleep Time and Jitter:** Introducing random sleep times and jitter in communication intervals makes the C2 traffic less predictable and more difficult to detect.
		- **Proxy:** Proxies act as intermediaries between the infected system and the actual C2 server. They help hide the true source of the communication, making it harder for defenders to trace back to the malicious activity.
		- **HTTP Methods:** Modifying the HTTP methods used for communication (e.g., GET, POST) can make the traffic appear more like regular web browsing.
		- **Encrypted and Authenticated Communication:** Using advanced encryption algorithms and authentication mechanisms for C2 communication adds a layer of security and makes it more difficult for defenders to intercept or manipulate the communication.
		- **Domain Generation Algorithms (DGA):** DGAs dynamically generate domain names, making it challenging for defenders to predict and block C2 communication. The algorithm may incorporate time-based or pseudo-random elements.
		- **Data Exfiltration Techniques:** Customizing how data is exfiltrated can be crucial. This includes techniques like chunked transfer encoding, binary data transmission, or breaking data into multiple requests.
		- **Dynamic Profile Switching:** Switching between different communication profiles dynamically during an operation can make it harder for defenders to create static signatures or patterns for detection.
		- **Anti-Sandbox Techniques:** Implementing techniques to detect or avoid sandboxes, such as checking for virtualized environments or sandbox artifacts, helps the malware remain undetected during analysis.
		- **Payload Encoding:** Encoding the payload in transit can help evade signature-based detection. Malleable C2 profiles often allow customization of payload encoding.
		- **Dynamic Payload Generation:** Generating payloads on-the-fly or using polymorphic techniques can make it challenging for signature-based detection to identify the malicious
		- **Protocol Mimicking (e.g. Mimicking DNS Over HTTPS - DoH):** Mimicking legitimate protocols, such as DNS over HTTPS, can help blend malicious traffic with normal, encrypted web traffic.

#### Network Footprinting
Lessons learned
1. The main take away from this bonus section is to dig a little deeper and see what your tool looks like on the network. 
2. A few extra steps in the setup will make it much harder for the Blue Team to detect your actions. 
3. As you improve your skillset, learn more and more about your tools to inform decisions during Red Team Engagements.

## Conclusion




