
## Position: Senior Threat Analyst

### Generic Questions
1. Why you want to leave the current job?
```markdown
# Story
Timesheets
Salesforce 
Presentations
Review security controls

Basic penetration tests
> More technical 
I want to be part of a team where I’m directly contributing to mitigating risks, analyzing breaches, and building scalable solutions. I believe a technical-focused role like this aligns with my long-term goals and skillset.
```
1. Why do you want to work for Coalition?
```markdown
# Story
Coalition brings together active monitoring, incident response, and comprehensive insurance to solve cyber risk.

I believe in the products and services that are being offered by the business and can see a great impact that it has been making. Give an example

2 case studies
Example 1: For example, A manufacturer that produces industrial components, experienced a cyber attack on their industrial control systems (ICS).
The company was insured and their Bodily Injury and Property Damage and Business Interruption coverages went into effect. Even better, Coalition’s Security Incident Response Team (SIRT) helped them regain control of their systems and secure their network to prevent another attack from occurring.

Example 2: Healthcare > Affected > The policyholder had been hit with HelloKitty malware, a dangerous new ransomware variant known to exfiltrate its victims’ data before encrypting it. > CIR was able to negotiate the ransom demand down by nearly 75%
```
1. Describe a time you learned from a mistake.
```markdown
# Story
- On an internal pentest > Compromised a low level user account but did not enumerate much with it
- Found it had local admin right on a computer that had Unconstrained delegation enabled > TRUSTED_FOR_DELEGATION flag in the User Account Control (UAC) flags.
- A setting in Active Directory that allows a user/computer/service account to impersonate users to access resources on their behalf.
- Systems which are configured for unconstrained delegation will have the TGT (Ticket Granting Ticket) stored into LSASS memory
- Coerce authentication from the DC$ Comp account to the Host that had Uncons Dele enabled, and ran Rubeus in monitor mode
- The ticket granting ticket (TGT) of the domain controller machine account will received and captured by Rubeus.
- Using the Pass the Ticket within Mimikatz the current user account will get high privilege rights on the domain controller.

- So it was kind of attention to detail lesson for myself and dont underestimated
```
1. Talk about your background and experience
```markdown
# Story
I currently work as a Senior Associate specializing in offensive security. My role involves red team operations, incident triaging, and threat detection. I’ve gained strong expertise in scripting for automation, analyzing TTPs, and monitoring the dark web for corporate data leaks.

I’ve also been part of projects where my red team knowledge has enhanced defensive strategies, such as improving detection rules for SOCs or testing them out
- Or mentoring the blue team
```
1. When dealing with multiple things at a time, how do you stay organized?
```markdown
# Story
- For technical projects, I document progress and set milestones
	- I dedicate focused time blocks for deep technical work and allocate time for team collaboration or documentation
```
### Interview Prep
1. Basic questions around experience and toolsets used.
```markdown
# Windows XML Event Log | EvtxECmd 
- Timeline Explorer to view CSV created via EvtxECmd

# Registry Explorer
ShellBags

# Prefetch - Evidence of execution
Eric Zimmerman tool to review PF files is PECmd.exe
```
1. Heavy focus on values and culture.
2. Asked about my background and my familiarity with certain tools.
3. Why our company over others?
4. Difference between EDR and Ant-virus.
```markdown
# Story
- EDR: Behavioural analytics

Svchost.exe, or Service Host, is an important Windows process hosting one or more Windows services.

**Process Hollowing:**
- **What it is:** A technique > Malicious program > Creates a new process (e.g., a legitimate system process like `svchost.exe`) and then "hollows out" > memory of that process by replacing its code with malicious code.
	- This allows the malware to run under the guise of a trusted process, making it harder to detect.

**Process Injection:**
- **What it is:** A broader technique where malware injects its code into the memory of a running process. 
	- This could involve adding malicious code into the memory space of another process (like a browser or system service), allowing the malware to run in the context of that process.

# Mimikatz
Mimikatz works by interacting with the Local Security Authority Subsystem Service (LSASS) process to extract authentication credentials, such as plaintext passwords, hashes, and Kerberos tickets, stored in memory. It typically does this by reading LSASS memory directly or injecting code to access sensitive data.
```
1. Explain DNS
2. Basic questions like background and skills
3. What is one project you are most proud of?
4. What pen testing experience do you have?
5. Have you stood up a pen testing process?
6. How many people have you directly managed?
7. Interview questions ranged from prior industry experience with business email compromises to network intrusions and ransomware.
```markdown
## Industry Expereince - Story + Tool leveraged
# Business email compromise
- RedLine Stealer > Malpedia > Information stealer like browser creds + crypto + info
	- Malware bazaar > Download Sample EXE + (Leaked source code is avaible on Github)
- User receive a phishing mail and macro file fetched EXE
- SentinelOne > Incident Tab > Threats | Alerts
	- Threats > Based on file hash > Triggered it as malicious > Virus Total confirms
		- Also Detecting engine > SentinelOne Cloud when binary ran
	- Threat Overview > Indicators > shown > Suspicious WMI query > Execution, Discovery, Collection and Defense Evasion
- Explore Threat > Process tree > All Events | Network Actions
	- Network Actions > Destination IP > This is their C2 server
	- Leverage who.is / virus total > Lookup IP 
- Now select the threat > Threat actions > Mitigation actions 
	- Select kill, quarantine, remediate, rollback
	- Select remediate > mark as resolved 
	- Analyst verdict: True positive or Suspicious
	- Not doing rollback as nothing was encrypted or exfilteration. But if compromised would have been more than WMI query then we could have selected this

# Network intrusion

# Ransomware

# Malware fam
Malware Families

```
1. How do you stay organized? How do you help clients succeed?
2. Just a technical case study to gauge your abilities as an analyst.
3. Tell me about a time when you faced a difficult situation and what you did?
```markdown
# Story
- Led an red team engagement
- Client was happy and the exercise became purple team as he wanted to me bring me on the defensive side to train and remediate all those vulnerabilities
```

### Responsibilities
- Lead end-to-end event investigations, from MDR alert to client reporting, with Coalitions customers.
- Identify and investigate incidents to understand the cause and extent of a breach by leveraging technical tooling and threat intelligence sources.                                                                        
- Conduct forensics, log, and malware analysis across a client’s environment in support of our investigations.                                                                        
- Leverage findings from the investigation to develop and articulate expert-level opinions to both technical and executive audiences.                                                                        
- Develop comprehensive written reports and oral presentations to both technical and executive audiences.                                                                        
- Effectively communicate and collaborate with customers including legal counsel, and technical and executive stakeholders.                                                                        
- Collaborate with practice leadership in leveraging subject matter expertise in the scoping of customer engagements

### Skills and Qualifications
- 5+ years of experience in MDR/security monitoring space, including commonly used tools such as SentinelOne and Crowdstrike.    
```markdown 
# Story
- Leveraged SentinelOne to monitor for threats
- Saw an alert on the Threat page.
- Open the Threat overview to check the process tree and command line being executed
	- It was leveraging wget to fetch the reverse shell
	- Checked the IP via virus total and found that it had been used in the past to host malicious stuff
- Closed the threat by peforming the quarantine mitigation action which will kill and encrypt and isolate the threat
	- The client usually asked us to not remediate as they might leverage remaining files and system changes to understand why the activity occured on the host.
- Leveraged the Alert tab and setup a new rule 
	- incase malicious IP communicates again with the system then trigger an alert
	- PowerShell downgrade

# SentinelOne has following actions when you wish to close an threat
1) Kill
2) Quarantine
3) Remediate
4) Rollback
```
- 5+ years of experience and deep technical knowledge of techniques to contain an active incident, collect event data, analyze data for IOCs/IOAs, and evidentiary reporting to internal and external stakeholders. 
```markdown
# Story
Velociraptor offline installer incase of an incident response
```
- 5+ years of experience and an understanding of cyber security operations, security monitoring, EDR, and SIEM tooling, e.g., Endgame, Falcon, and Splunk.


### Questions to the Panel - 5 

What are the key challenges the MDR team is currently facing?

What opportunities are there for collaboration with other teams, like Engineering, or IT Security, to improve detection and response capabilities?

How does Coalition support ongoing learning and professional development for its MDR team members, especially in staying ahead of emerging threats and tools?

What does success look like in this role, especially in the first few months?

What qualities or skills are you looking for in an candidate for this role?

----
1) L&D opportunities
2) Challenges team in facing
3) Day to Day activity
4) Reverse engineering 

### Questions
5. Understand that they ask me - Why do you want this job
	1. I know i can provide value from my background and deep dive
6. What do you see yourself after this job / how your future look like in this role
	1. Enhance my skills

### Nick Romano (Senior Threat Analyst) Interview
- Looking for an Engineer
	- Offensive Security
	- SOC Monitoring
	- Threat Hunting
- Make sure to state indirectly how good you will be an engineering role
	- Use AI to analyse last call and give me output on what they are looking for
	- Tweak that data and share it over call along with achievements

<<<<<<< HEAD
#### Preparations


=======

```markdown
# Structure
1. Introduction
2. Background & Experience
3. Basic questions
	1. Why Coaltion - I am impressed by Coalition's growth in the MDR space and its comprehensive approach, combining cyber insurance with proactive security measures. With my background in threat detection and offensive security, I am confident in my ability to contribute effectively to your team.
	2. Why Leave - Looking for more challenges. This role at Coalition allows me to leverage my experience in leading incident investigations while growing my skills in security monitoring and response, which aligns with my long-term career goals.
4. Job Description questions
	- Offensive Security
		- Red Team engagement > Purple Team > Sit with SOC and deliver penetration test
		- Cool Bugs 
		- Threat modelling for an web application & Developed test cases accordingly
		- End to End delivery model
		- Coached People - On Mitre TTPs & Analysing PowerShell scripts
		- Creating/Improving and Testing detection ruleset for SOCs
	- Blue Team
		- Incident response using velociraptor
		- SOC monitoring using SentinelOne
			-BEC example
		- Investigating Windows Endpoints 
			-Event Logs
			-Registry
			-Evidence of execution
			-Persistence, Priv Esc & Lateral Movement
			
5. Atleast 5 questions to the Interviewer
	1. What does success look like in this role, especially in the first few months?
	2. What opportunities are there for collaboration with other teams, like Engineering, or IT Security, to improve detection and response capabilities?
	3. What are the key challenges the MDR team is currently facing?
	4. What has your experience been like working at this company, and what do you enjoy most about being part of the team?
```

```markdown
Experience in **ransomware incidents**, **sending Velociraptor for artefact collection**, and your familiarity with **registry explorer, shell bags,** and **timeline explorer**. Bring up concrete examples like this to demonstrate your hands-on skills, not just the technical concepts.

# Examples - Solidify this further via checking for correctness 
IMRPOVE YOUR EXAMPLES | STAR METHOD

- Ransomware incident > PsExec being allowed & Encrypted > Backup servers > Velociraptor offline executable for artfact collection
	- Analysed 
		- Event logs via Timeline explorer - (Event Log Explorer Command Line)
			- Collect: C:\Windows\System32\winevt\Logs
			- Analysis: C:\Tools\Zimmerman\net6\EvtxECmd.exe -d C:\Users\davisrg\Desktop\Logs --csv log_timeline.csv
		- Registry & shell bags 
			1. MuiCache - Evidence of execution of GUI programs
			2. ShellBags - Windows Folder Browsing artefact

**Real world example**
1. We would get handed an image
2. Mount the image via Arsenal Image Mounter
3. Pull off UserClass.dat and NtUser.dat from the users of interest.
4. Use ShellBags explorer > Load offline hive option to load those hives and investigate.

		- Evidence of execution artefacts like Prefetch & Shimcache
			1. Prefetch - - Its a process that creates a record of files that have been executed. Windows uses this to enhance the spin up of executables
			2. Shimcache - `AppCompatCacheParser.exe > Perform analysis via Timeline Explorer > Timeline Explorer marks "Yes" under "Executed"

- Malware Family that was used
```

```markdown
# How to isolate an host in SentinelOne
& Other basic quesiton about the Tool but impactful (Maybe checkout a guide)
```

### Last interview
- Detection engineering is key priority this financial year
- Make sure to talk about experience
	- Value delivered 
- Looks like an extremely talented and curious person. 
	- MDR space - Windows endpoint
	- ⁠Offensive security - best stories
	- ⁠Speak about how you can leverage this experience and help them grow in the market. 
	- ⁠Speak about detection engineering building ruleset to catch threat across ( Huntress blog can help )

Understand the business process from him, what are they trying to achieve / key goals
- Coalition values > ??
- Purpose > ??
- What is a day to day in your life, is it more hands on or business capability

Tell him what i loved after talking with Nick, Alec and Yohannes
- The definition of threat analyst over here is not just resolving tickets - which is so great.. it helps me grow and do more! The drive for passion and success is something i loved to see.

Question i should prepare
1. Where do you see yourself in next 5 years
2. Value
3. Why do you think you will be suitable 
	1. i have been studying and working in this field for last 5 years
	2. Broaden my perspective and i provide value
	3.  ⁠journey started from masters & ctf
	4. experience and in security for a while
	5. familiar with sentinel one.. using my offensive security skills.. i can help a company grow

1. Experience align with this role
2. Some strengths and weakness


