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
		2. Otherwise, send it somewhe

------------------------------------------------------------------------


## Functional Segregation


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