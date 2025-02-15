
```markdown
# Responder

# Domain Name
ldapsearch -H ldap://172.21.77.2 -x -s base namingcontexts

# Find DC IPs
nslookup -type=srv _ldap._tcp.dc._msdcs.cslg1.cslg.ne
**Get Last Column**
nslookup -type=srv _ldap._tcp.dc._msdcs.cslg1.cslg.net | awk '{print $(NF)}'

# Nuclei
/opt/nuclei -list DCIPs.txt hosts.txt -rl 100 -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64)' | tee NucleiResults.txt

```

```markdown
## Test Cases w/o Creds
1) Null Bind - No Luck
2) Network Enumeration
```

3. Network
	1. Printers
	2. SQL Database
4. SMB
	1. Open Shares
5. Responder & Relay 

```markdown
# Internal Checklist
## ADCS
certipy find -u "U0036085@cslg1.cslg.net" -p "Patisserie6?" -vulnerable -dc-ip 172.21.77.2 -stdout | tee VulnTemplate.txt 


```


