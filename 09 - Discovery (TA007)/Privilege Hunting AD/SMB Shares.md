
# C2 BOFs

`execute-assembly C:\Tools\sharpshares.exe shares`

![[Pasted image 20240408232026.png]]
# Linux

## Check Share
`cme smb fs01.draconem.corp -u 'Gareth.Kilgallen' -p 'Hu825meapvsAq#Rx' --shares`

![[Pasted image 20240408232447.png]]

*Resolve Domain*
`nslookup <domainName>`

## Access a Share
### SMBClient
`smbclient //10.10.175.182/Enterprise-Share -U 'enterprise-security%sand_0873959498'

### SMBMap


### SMB Impacket
`smbclient.py Gareth.Kilgallen:Hu825meapvsAq#Rx@fs01.draconem.corp`
- `shares
- `use <Share>
- `ls`
- `get <file>`
- `exit

# Windows