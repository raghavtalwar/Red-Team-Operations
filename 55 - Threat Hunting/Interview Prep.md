## Offensive Sec to Red Team
I don’t think i am leaving offensive security, i think i am stepping up to a position to do more interesting work

I plan to use my red team experience to defend and respond in a better way

Focus on ransomware 
I’ll recall and prepare my best war stories to share in STAR format!

Also look into incident response and threat hunting and digital forensics

## Job Profile Tailoring + Stories 
Check Job profile and tailor everything to that!

1) Share red team story
- Gather TTPs
- ⁠Identify flaw in MFA config
- ⁠Citrix breakout

2) Share another post incident review story 
- This is where you identify stuff and blocked

3) Incident response helpline and assisting customers
- Ransomware incident

 4) Red team
- Discovered psexec in Temp
- ⁠Felt that there can be more to this
- ⁠threat hunting to identify the presence of threat actor in the env

```markdown
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
```

```markdown
# Story 2 (STAR) - Threat hunting

While being engaged on a red team, we discovered finance.exe inside windows temp folder

It looked very sus as we gained access to this box via Citrix breakout. So i quickly checked the versioninfo

Stopped , informed and initiated Incident response - a bit of threat hunting on citrix logs was conducted

Isolated citrix box
Conducted investigating
Stopped the attempts from moving forward
Red team became purple team exercise which went about for a month

Learned KQL, to perform threat hunting
```

```markdown
# Story 3 (STAR) - Incident response

Dark web monitoring for corp leaks

Setup the whole infra on cloud to perform this and automated process

```

I want to provide value while doing threat hunting

I will find threats in my hunt

## Ransomware incident


## Interview Preparation 

All possible questions like what are IOC and IOA on job description
And resume must be documented and prepared

## Behavioral Ques

1) What if you do a mistake

Inform senior
I will have a second eye on it

2) Tell me something very challenging, how did you got through it

3) Top accomplishments time at PwC

4) How do you explain complex security issues to non-technical stakeholders?
You need to understand their role and then try to communicate based on their level of understanding 
- Scoping meeting, explain what a pentest is and what we need from them

Apply my offsec mindset

Can i know how much the company is willing to offer

But if everything goes well i can consider that

```markdown
# Introduction
Hey - my name is Raghav, a senior consultant with the Cyber threat services - offensive security team. 
I have experience in offensive security, conducting red teams and assisting on incident response and threat hunting.

Have done my SANS SEC 565 and have completed GIAC red team professional, it included a lot of threat hunting exercises as well. 
- Also done hacking active directory (CRTP) and Azure hacking 
- Monthly dedicated tester inc scoping and explaining business risk to non tech stakeholders
- Also have exp in incident response on cloud esp AWS, been on roaster shifts
- Developed methodology to test all sort of application - thick, mobile and web
	- Help document and improve hunting processes, tools, and capabilities

- Good exp in conducting penetration test, have found vuln which led to domain compromise from the external to the internal front

# Salary
Can i know how much the company is willing to offer for this role
- I am looking for between 150 to 160k
- Currently i am at 130 plus super

# Love doing research on malware 
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

2. **Handling Pressure:**
- Strict deadlines while conducting an red team exercise, so we started with social engineering and and via vishing we were able to gain access and from that point we observed that we were not within the corp network 
- So we had to move laterally across the network and in the end i was able to reach the crown jewels

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
```

```markdown
# Story 2 (STAR) - Threat hunting

While being engaged on a red team, we discovered finance.exe inside windows temp folder

It looked very sus as we gained access to this box via Citrix breakout. So i quickly checked the versioninfo

Stopped , informed and initiated Incident response - a bit of threat hunting on citrix logs was conducted

Isolated citrix box
Conducted investigating
Stopped the attempts from moving forward
Red team became purple team exercise which went about for a month

Learned KQL, to perform threat hunting
```

---
The role is that of a Threat Hunter and i have 3 years plus Red Team experience
- Velociraptor - Done > Do some revision and highlight that you learned in a CTF
