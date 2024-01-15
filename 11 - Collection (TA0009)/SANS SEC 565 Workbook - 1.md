# Lab 1.1 - Environment Orientation
### Objectives
1. Understand the lab environment for the course
2. Preview labs for the course
3. VM review
### Conclusion
This lab provided an overview of the lab environment and how traffic will flow between the VM, systems in gray space, and targets in red space. 
- A good troubleshooting methodology is important to isolate issues effectively. 
- This lab also introduced the labs for the remainder of the course. 
- Lastly, we investigated a suspicious listener using tools available on the system. 
	- We took advantage of all the information in /proc to understand exactly what the process is doing. 
	- This abbreviated investigation is a critical skill when exploring each new system that you touch.
	- This is an important step to ensure he safety of your engagement, your tradecraft, and your tools.

## Lab Environment 
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
*Example - Proxy & Redirector*
If everything is set up and an exploit is thrown through the proxy at the web server but there is no call back, then we have to methodically troubleshoot the issue. The first step is to test locally. It could be any one of these issues, listed in priority order.

    Is there a good path between blue space and the proxy?
    Is the redirector returning traffic from external sources to blue space?
    Is the proxy able to communicate with the web server in red space?
    Is the target able to communicate with redirector?
    Is the exploit weaponized properly, has it been tested against a local test system?

## VM Review
New VM for a Red Team, The first question that you should always seek to answer is: "Is it safe to op on this system?"
- Note: During a red team exercise, it was discovered that APT already had established control over the target asset to which we had gained access.

Malware is a threat to every Red Team Operator for multiple reasons: 
1. Malware indicates the presence of another adversary 
2. Malware is always a risk to the parent organization 
3. Malware may grant another adversary access to the system 
4. Malware may record and transmit your actions 
5. Finding malware on a system should pause the engagement 
6. Incident Responders must start an investigation

### Lab Walkthrough
Prep: `sudo /labs/sec-1/orientation/setup.sh`


tcp     LISTEN       0         10                          0.0.0.0:54321                0.0.0.0:*         
users:((ext4-rsv-conve",pid=5406,fd=3))                   

sec565     5389   5380  0 07:47 pts/0    00:00:00 bash

Note: The process cannot be found | We cannot find it running with that ID

Thus, we look for network connections > Found a sus service > Enumerate process ID for that service > Found that we cannot find it via `ps` > Investigated `ps` binary and identified that its Trojan > When we run `ps` it hides the malicious process and shows rest > Identified the binary its hiding > 

![[Pasted image 20240115172813.png]]

![[Pasted image 20240115173109.png]]

![[Pasted image 20240115173446.png]]

![[Pasted image 20240115175805.png]]

![[Pasted image 20240115180130.png]]

