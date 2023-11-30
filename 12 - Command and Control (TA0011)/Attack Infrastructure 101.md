# Setting up the Attack Infrastructure

## Standard Infrastructure 
- Setting up Command and Control server to listen on a IP or a Domain and is accessible by anyone on the internet.
- Weakness in simple / standard infrastructure
	1. Defenders can easily enumerate hosted payloads
	2. C2 may be easily blocked by IP or Domain name
	3. Fragile to outages incase DNS server goes down
	4. Infrastructure will be continuously scanned
	5. Easy to secure but easily probed by the Blue team
------------------------------------------------------------------------
## Advanced Infrastructure 
- Goal: Build a Resilient infrastructure and has stealth and separation!
- Segregate assets by their function, designated roles and do not cross-contaminate during execution
	- Eg1: Email servers will be at 1 domain and will be used to only send emails
	- Eg2: Payloads will be hosted on another domain, same goes for redirectors and c2 servers
- Use protocol diversity, a mix of channels (eg: HTTP and DNS)
- Place redirectors before every host
	- Objective is to not expose the c2 server directly

### Example: RedELK
- Advanced Red Team Infrastructure - RedELK available on GitHub
	1. Setup C2 Servers - We can have 2 C2 Servers such as Cobalt strike & Covenant
	2. We should never connect a Target system back to a C2 Server. We need to setup Redirectors
		1. Redirectors are 1st line of infrastructure
	3. Run implant on Compromised system, it goes to redirectors which forwards the traffic to the C2 Server
		1. Redirectors Configuration - Tracking pixels, Access control rules that say if traffic is coming from the Target network then forward it to C2 Server
		2. Otherwise, send it somewhere else! - Protect C2 Servers from SOC. SOC will investigate the C2 traffic
		3. SOC will see that compromised host is talking to IPs in the redirectors, they will use tools like virus total, domain classifiers, IBM X-Fore to check reputation of the redirectors
		4. SOC will query the redirectors to identify anything there. They will never hit C2 servers and they remain protected
	4. RedELK - Its an elastic stack, it is a Red Team SIEM for us, we can get logs from redirectors, c2 servers and query SOC tool set for indicators of our attacks!
###### Resource: https://github.com/outflanknl/RedELK 
![[Pasted image 20231201001010.png]]
------------------------------------------------------------------------------------
## Functional Segregation
- Goal: We want different assets for different things!
	- 


------------------------------------------------------------------------

## Redirectors


------------------------------------------------------------------------

## Domain Names


------------------------------------------------------------------------

## Digital Certificates


------------------------------------------------------------------------

## Cloud Providers


------------------------------------------------------------------------

## DNS Settings for Phishing

------------------------------------------------------------------------


## Third Party Email Hosting

```markdown
```


------------------------------------------------------------------------

## Enumeration 

```markdown
```

## Exploitation 

```markdown
```

## Resources

```markdown
```