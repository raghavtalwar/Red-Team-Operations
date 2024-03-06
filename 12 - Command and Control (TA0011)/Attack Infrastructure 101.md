#### Tags: [[02 - Resource Development (TA0042)]] 
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
----------------------------------------------------------------------------------
## Functional Segregation
- Goal: We want different assets for different things!
	- Phishing SMTP: We are planning to send phishing mails from our Phishing server, it will have its own domain, own TLS cert, point to its own service provider (cloud or hosted)
	- Phishing payloads: The payloads that will be downloaded from the Phishing mails are hosted on a different domain with a different TLS cert. Eg2: such as AWS s3 bucket
	- Long Term C2 - Has its own domains + TLS Cert + Own Hosting
	- Short Term C2 - Same as above
- We don't want everything to get burned if one gets caught by the Blue Team!
	- New red engagement means new set of infrastructure should be established
	- Each of these functions will likely be required for social engineering campaign
------------------------------------------------------------------------
## 
- Goal: ALWAYS have a redirector in front of c2 Server!
	- Do not expose c2 server to the internet
- Objective: Act as a disposable server that redirect traffic in order to obfuscate the backend systems.
------------------------------------------------------------------------
## Domain Names
- Access a website we use a Domain name, direct IP access sometimes is blocked as well
- Red team always purchases a number of domains:
	1. Get away with IP address blocking
	2. Allows us to do load balancing to different IP address
	3. They are portable and not tied to a particular hosting provider
- Make sure when we purchase a domain name its not attributable back to us!

### Domain Name Consideration
- Multiple considerations come to mind when thinking about Domain name
	1. Purpose - It should have a purpose, tailored to target organisation
	2. Spam - Make sure its not already added to a blocklist
	3. Age - Defenders are looking at this, domain only used for a couple of weeks is a red flag
	4. Categorisation - Domains are categorised, a lot of block occurs due to this for example pornography or guns or hacking are blocked
	5. Domain history - Look at this especially when buying a old domain.

### Purchase Domains & Categorisations
- Direct access to IP is often blocked outbound
- Some outbound proxies blocks domain based on categories. Thus purchase domains and categorise them!
	- Categorisation Sites - Enumerate which ones of the below proxy is being used and categorise accordingly. Note: Red Teamer needs to a put a website up and running before they can request categorisation
		1. BrightCloud
		2. Fortiguard
		3. McAfee
		4. Palo Alto Network
		5. Symantec / BlueCoat
		
Summary: Red Team purchase domain name and then purchase hosting and put up a website related to that domain. Go to categorisation and request them, some are automated otherwise manual process!
- Do your recon and figure out 'what is being used at the target organisation' and get your domain categorised!

- Another way - Purchase categorised domain that has expired, we can buy a domain with good age and reputation!
	- To check if its reputation is good we can use
		- https://www.expireddomains.net
		- https://domainhuntergatherer.com
	- Note: These domains cost more, eg- brand new domain may be 15$ and expired domain may cost us 100$

- Categorisation - 2 Types either for blocking domains or intercepting TLS 
	- Red Team Tip: Its a possibility that certain organisations might not intercept - a Health or Financial site, Example - If Red team can get a domain and categorised it as a healthcare domain then we might get away with few controls! 

------------------------------------------------------------------------
## Digital Certificates
1. Acquire TLS certificated for all domains
	1. Encrypt all Command and Control (C2) communication
	2. Provide TLS - Hosting payload, using it for phishing or credential stealing sites.
2. Free TLS cert via LetsEncrypt, but Blue Teamer are looking at if the cert is new, when it was renewed and who is the provider. Keep this in mind, free one can get us caught
3. Don't get burned!
	1. Paid TLS cert - User check if TLS is used before putting creds into a site
	2. Modern browsers are not happy about cleartext HTTP

------------------------------------------------------------------------
## Cloud Providers
- Hosting Linux or Windows systems!
- 

------------------------------------------------------------------------
## DNS Settings for Phishing

------------------------------------------------------------------------
## Third Party Email Hosting

```markdown
```


------------------------------------------------------------------------
## Resources

```markdown
```