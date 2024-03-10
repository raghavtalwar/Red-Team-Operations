#### Tags: [[12 - Command and Control (TA0011)]]
## Objectives

    Understand the use of redirectors in attack infrastructure
    Create a listener on Empire that will expect redirector routing
    Create stager payloads that will route through the redirector
    Execute the stager payload in the lab environment

## Overview
This lab will focus on the:
- Use of redirectors to create a buffer between the C2 server (Blue Space) and the Target network (Red Space). 
- We will create an account on a Virtual Private Server (VPS) vendor and 
- Provision two VPS's to redirect traffic through.
- Thus, we will leverage Empire C2 stager (Red Space) to perform routing via redirector (Grey Space) to reach the Empire listener (Blue Space).

![[Pasted image 20240310163005.png]]

### 1. Launch [[Empire C2#Create an Empire listener|Empire C2 & Setup Communication]]

Redirector Communication Pattern
1. C2 Listener will get Redirector IP Address
2. The VPS running Redirector will leverage socat to redirect traffic from Stager to Listener
3. C2 Stager will callback to Redirector IP Address
### 2. Provision VPS


### 3. socat Redirection


#### 4. Create Listener
- Create an Empire listener with a Host set to a redirector address

#### 5. Create Stager
- Create a stager payload

#### 6. Deliver Stager
- Execute the stager to create an Agent in the target environment via RDP: 
`xfreerdp +clipboard /cert-ignore /u:Gareth.Kilgallen /p:Hu825meapvsAq#Rx /v:wk01.draconem.corp

#### 7. Agent Interaction

```markdown
```

### Conclusion


### Resources | Notes | Bonus

```markdown
```

#### Notes
- Add a link to Empire on how we are leveraging C2 stager to perform routing via redirector to reach the Empire listener





## Conclusion
