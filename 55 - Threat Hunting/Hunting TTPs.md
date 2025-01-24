
Key question asked me to was
- How would you build your own Threat hunting platform if you have all the money in the world
- What does success in threat hunting looks like

Tactic - Collection
Technique - Keylogging
Procedure -  API Execution

I want to provide value while doing threat hunting > I will find threats in my hunt
## Final Interview Prep

```markdown
# Introduction
- Present yourself > Short and Solid one

# Sharing experience 
- 3 years contribution based on resume pls
  + SANS > GIAC Certified > GRTP > Threat hunting
  + Incident response on call

# War Stories 
- Use the STAR Format > We have 3 stories

# Talking points based on Job description
- Ask AI what ques can come up based on this description
	- I can talk about registry, forensics, malware & Velociraptor

**Velociraptor**
_Velociraptor provides you with the ability to more effectively respond to a wide range of digital forensic and cyber incident response investigations and data breache_
- Velociraptor executable can act as a **server** or a **client**
- Velociraptor can be deployed across thousands,
- Amazing Open source tool > Great to see how Rapid7 will enhance it even further

1) Interacting on client machine
2) ﻿﻿**Creating a new collection** - Windows.KapeFiles.Targets > bulk collector tool
Kroll Artifact Parser and Extractor. A tool created by Eric Zimmerman used to parse and extract forensic artifacts from a system.
1) **The Virtual File System**
	- **file - uses operating system APIs to access files**
	- **ntfs - uses raw NTFS parsing to access low level files**
	- **registry - uses operating system APIs to access the Windows registry**
	- **artifacts - previously run collections.**
2) **Velociraptor Query Language**
3) Velociraptor Plugins - execve() to run run PowerShell code
4) **Hunt for a nightmare**
	1) Use Velociraptor to create an artifact to detect the PrintNightMare vulnerability!
	Artifact Exchange > Detect > Windows.Detection.PrintNightmare
```

Hi Raghav, all the best with the interview, isn't much more I can share unfortunately.

Just be yourself and 
- have some key examples of work you can share about to showcase your expertise and 
- Try and have some other talking points prepared base on the job description too.

```markdown
# Why Rapid 7
- Vulnerability Risk Management (VRM)
- Threat Detection & Response
- Application Security
- Security Operations
	+ Contibute to product development

# Introduction
My name is Raghav, i am a senior consultant with the offensive security team. I have demonstrated experience in red teaming and offensive security activities. I recently passed my SANS SEC 565 and got GIAC GRTP certified. Apart from this i hold OSCP, CRTP and CARTP.

# Leaving Offensive sec?
I plan to contribute to threat hunting, leveraging my red team backgorund to defend and respond in a better way. Stepping up to do more interesting work

# Terms
Dwell time - time attack can be undetected after initial access
Patient zero 
- Identify system that was compromised first
	+ Initial infection vectors (phishing, exploit, etc.)
	+ Unusual outbound traffic or suspicious processes on endpoints.
	+ Lateral movement attempts

- key indicators that a system is the 'Patient Zero' in an attack?
	+ First occurrence of malicious activity.
	+ Initial signs of malware installation.
	+ Compromised user credentials used for lateral movement.

- How do you detect persistence mechanisms in a compromised system?
	+ List techniques used by adversaries (e.g., registry changes, scheduled tasks, services), and explain how you’d investigate using tools like Sysinternals (Autoruns), PowerShell, or EDR to find evidence of persistence.

- Process of threat hunting in an enterprise environment
	+ Establishing a baseline of normal activity.
	+ Looking for anomalies (e.g., unusual port usage, processes).
	+ Using YARA rules or other threat intel to detect malware signatures.
	
# Ransomware removal
1. Identify and isloate the source, maybe disable admin and network shares 
2. Isolate the affected machine at the same time
3. If EDR is present then endpoint which are compromised - we can identify those
4. Identify the accounts that were used 
5. Disable and Reset Credentials
6. Identify Patient Zero - Identify system
7. Eradication - Remove malware and threat actor presence
8. Recovery
```

```markdown
## Stories
# Story 1 (STAR) - Adversary emulation
Involved in adversary emulation / red team against a Logistics and shipping organisation, where i was tasked to initally to gather TTPs of an APT group that was likely gonna target them

> Tactic - Access sensitive data
> Technique - SQL injection
> Procedure - SELECT * FROM TABLE --

Once a targeted adversary is selected, the goal is to identify all TTPs categorized with that chosen adversary and map them to a known cyber kill chain.

To begin the process of mapping TTPs, an adversary must be selected as the target. An adversary can be chosen based on,

1. Target Industry
2. Employed Attack Vectors
3. Country of Origin
4. Other Factors

Traveling Spider was the APT group that 

I was able to find an SQL injection and authorisation bypass on their website, which leaked some of their clients sensitive data

# Story 2 (STAR) - Threat hunting
Weak creds > Citrix breakout > no 2FA > Temp folder > Finance.exe > Checked versioninfo > mimikatz > alerted and initiated > collected logs and performed threat hunting and incident response

While being engaged on a red team, we discovered finance.exe inside windows temp folder

It looked very sus as we gained access to this box via Citrix breakout. So i quickly checked the versioninfo

Stopped , informed and initiated Incident response - a bit of threat hunting on citrix logs was conducted

Isolated citrix box
Conducted investigating
Stopped the attempts from moving forward
Red team became purple team exercise which went about for a month

Learned KQL to perform threat hunting

# Story 3 (STAR) - Incident response

Dark web monitoring for corp leaks

Setup the whole infra on cloud to perform this and automated process

## Must Share
# Dark web monitoring for corporate leaks
Automated whole infra setup on AWS
- Ec2 instance > Lambda function > Runs a script  
	+  Script to compare hash > Alert / notify > Also check for client names
	+ Incaase found then it uses SNS > Alert on mail along with a screenshot link
- S3 buckets and Clam AV 
	- Scan and upload
	- Forensic download and perform Autopsy
		- **Verifying the Integrity of Data**
		- File System and Metadata Analysis
		- Identifying Malicious Files

# Ransomware Detection > Threat hunting
PsExec execution 
-d option > Imp > It means run the following command all over the place but dont wait 
	+ Push ransomware
	+ @Can be used to specify target file containing host names

# Threat hunting > WinAPI calls > Search for Keylogger presence > KQL on ELK instance
```
![[Pasted image 20241011005830.png]]
```
```

#### Love doing research on malware 
- Leveraging new TTPs
- Indicator of attack (Proactive)
	- Credential theft
	- Command and Control
	- Credential exploitation
	- Data exfilteration
- Indicator of compromise (Reactive) - Static - Conduct targeted hunts during major incidents
	- IP addresses
	- Vuln exploitation
	- Malware injection
	- Cyber threat signatures

**Handling Pressure:**
- Strict deadlines while conducting an red team exercise, so we started with social engineering and and via vishing we were able to gain access and from that point we observed that we were not within the corp network 
- So we had to move laterally across the network and in the end i was able to reach the crown jewels
---

## Questions - Joining date
1. Can we make my offer letter to start from next year Jan?
	1. Yes - Easy 
		1. PR Nomination - I have been nominated for PR which means i will become a permanent resident within an year. The employment letter has been submitted under my current firm - I can change this but i need to check with my Visa agent. 
			1. Once i receive the nomination within a month and a half i can then switch roles.
		2. Leaves in Dec 
	2. No - What is the last joining date you can give me
		1. PR Nomination - This will take around 1 and a half month
		2. Leaves in Dec - Can i work from India or Till what date you want me to work in Australia so i can reschedule flights accordingly 

----
