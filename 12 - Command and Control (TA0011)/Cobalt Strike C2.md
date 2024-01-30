
### Objectives

    Review the features of Cobalt Strike
    Create a listener
    Create a payload and host it on the C2 server
    Execute the payload in the target environment
    Interact with the Beacon
    Explore Cobalt Strike modules

## Overview 

The cobalt strike client can be found on the student instance, which can be reached via guacamole only. The credentials are:

    url: http://10.130.2.22:8080/guacamole
    username: student
    password: Sec565!!

##### Installation
1. Start the Cobalt Strike client by navigating to C:\Tools\cobaltstrike and double clicking the cobaltstrike application.

![[Pasted image 20240130225807.png]]

2. In the client please fill in the following values:
    `Host:` 10.130.4.100
    Select a username that you really like (or keep Neo)
    As password, please fill in the following sec565@!

3. If everything looks OK, click the Connect button. 

![[Pasted image 20240130225923.png]]
### Create an Cobalt Strike listener
1. A command and control server is useless if we do not listen for new incoming connections, Let's fix that right now.

In Cobalt Strike there are multiple ways to setup a listener.:
1.  Click Headphone icon on menu or Click on Cobalt Strike on the top of the menu and then select Listeners. 
2. A new tab is now going to open in the bottom half of your client called Listeners, go ahead and click the Add button.
	1. `Name:` The name of the listener, pick something descriptive for example HTTPS-Short or DNS-Long
	2. `Payload:` This is what type of payload the listener should expect, there are a bunch of options here as Cobalt Strike supports:
        `Peer-to-peer` connections over `TCP` or `SMB`.
        Can communicate to the internet over `DNS, HTTP or HTTPS`.
        There is also support for metasploit through `Foreign` listeners
    3. Finally, the concept of `externalC2` which allows you to create your own command and control channel that will interface with Cobalt Strike.

###### Host Rotation 
Cobalt Strike supports host rotation as well, This will make sure that the beacon will rotate hosts on a predefined set of rules.
- It can be set to Random or set as a fallback mechanism. 
- Not only does this help reduce indicators of compromise as the beacon will not phone home to the same IP all the time, it also makes it more robust in case one of your IPs or domain names get blacklisted. 

![[Pasted image 20240130231227.png]]
### Create a Launcher payload


### Deliver Beacon  


### Interacting with our beacon 


### Modules 


## Research | Bonus

[Malleable-C2-Profiles](https://github.com/BC-SECURITY/Malleable-C2-Profiles)

[GraphStrike: Cobalt Strike HTTPS beaconing over Microsoft Graph API](https://github.com/RedSiege/GraphStrike)

## Conclusion
- In this lab we explored another command and control framework. 
- We created a listener and a PowerShell launcher. 
	- We RDP directly into the environment and used a download cradle to retrieve and execute our launcher. 
	- We explored a few of the tasks/modules that the framework provides including how to transform our shorthaul into an interactive haul instead.


