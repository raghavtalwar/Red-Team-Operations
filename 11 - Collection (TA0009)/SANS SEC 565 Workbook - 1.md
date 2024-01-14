## Lab 1.1 - Environment Orientation
#### Objectives
1. Understand the lab environment for the course
2. Preview labs for the course
3. VM review
### Lab Environment 
This course will stress the importance of redirecting traffic from the target environment to our command-and-control servers.
- Although we are attached to the target environment via the VPN, we want to ensure we logically separate the assets belonging to the target (red space) from our redirectors in our attack infrastructure (gray space) and our C2 servers and VMs (blue space).
- Note: Technically speaking, all assets are part of the same Local Area Network (LAN), but we want to treat each "space" with a different set of rules and best practices.
	- During sections 1 through 5 you will be able to communicate directly from your VMs to target space, 
	- During section 6 there are routing rules in place to prevent those direct communications. In section 6 all communications must be redirected through gray space.
	
##### Threat Landscape
- Red space encompasses anything owned by the target.
- Gray space is anything that is owned by a 3rd party like redirectors in our attack infrastructure  and not associated with the target nor the Red Team.
- Blue space is anything that is owned/registered to the Red Team, any friendly assets like VMs and C2 servers.

![[Pasted image 20240114153709.png]]

##### Troubleshooting
Be methodical when troubleshooting network communications, start testing connections where you maintain control instead of generating unnecessary activity. TLDR: We maintain control of all those assets.
- First check the communication between blue and gray space. 
	- This means testing data flow, redirector or proxy settings, ip addresses, etc. 
- Then check that gray space is able to communicate with red space, 
	- This generates traffics and logs! 
- Lastly, or sometimes firstly, ensure the exploit is weaponized for the system you are targeting, test the exploit in a local lab environment.
*Exa*