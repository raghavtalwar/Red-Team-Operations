#### Tags: [[12 - Command and Control (TA0011)]]
## Objectives

    Understand the use of redirectors in attack infrastructure
    Create a listener on Empire that will expect redirector routing
    Create stager payloads that will route through the redirector
    Execute the stager payload in the lab environment

### Overview

```markdown
```
### Enumeration 

```markdown
```

### Exploitation

#### 1. Launch [[Empire C2#Create an Empire listener]]


#### 2. Provision VPS


#### 3. socat Redirection


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
