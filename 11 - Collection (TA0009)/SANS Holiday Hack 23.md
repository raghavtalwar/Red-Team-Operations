
![[Pasted image 20231215015053.png]]
![[Pasted image 20231215015522.png]]
However you decide to relax, be sure to soak in all the whimsical beauty of these magical islands, and enjoy the activities to the fullest!

### Task - Recursive search text in a given directory recursively
```
find . -type f -exec grep -il "troll" {} \;
```
### Task - Find a file in a given directory recursively
```
 find . -iname '*troll*'
```

### Task - Find the file somewhere in /opt/troll_den that is owned by the user troll.
```
find /opt/troll_den/ -user troll
```

------
### Challenges
#### Challenge 1 - Reportinator
![[Pasted image 20231215210435.png]]
![[Pasted image 20231215210732.png]]
![[Pasted image 20231215211157.png]]



az group list
az functionapp list --resource-group northpole-rg2
az vm list --resource-group northpole-rg2


invoke a run-command against the only Virtual Machine (VM) so you can RunShellScript and get a directory listing to reveal a file on the Azure VM.
- az vm run-command invoke --resource-group "northpole-rg2" --name "NP-VM1" --command-id RunShellScript --scripts 'ls -l'

![[Pasted image 20231217014336.png]]

![[Pasted image 20231217014550.png]]

Done

### Challenge 2 - Hashcat

`hashcat -w 1 -u 1 --kernel-accel 1 --kernel-loops 1`

Solution:
```
hashcat -m18200 -w 1 -u 1 --kernel-accel 1 --kernel-loops 1 '$krb5asrep$23$alabaster_snowball@XMAS.LOCAL:22865a2bceeaa73227ea4021879eda02$8f07417379e610e2dcb0621462fec3675bb5a850aba31837d541e50c622dc5faee60e48e019256e466d29b4d8c43cbf5bf7264b12c21737499cfcb73d95a903005a6ab6d9689ddd2772b908fc0d0aef43bb34db66af1dddb55b64937d3c7d7e93a91a7f303fef96e17d7f5479bae25c0183e74822ac652e92a56d0251bb5d975c2f2b63f4458526824f2c3dc1f1fcbacb2f6e52022ba6e6b401660b43b5070409cac0cc6223a2bf1b4b415574d7132f2607e12075f7cd2f8674c33e40d8ed55628f1c3eb08dbb8845b0f3bae708784c805b9a3f4b78ddf6830ad0e9eafb07980d7f2e270d8dd1966' --force password_list.txt
```

![[Pasted image 20231217015547.png]]
![[Pasted image 20231217024926.png]]
---------

### Challenge - The Captain Comms
![[Pasted image 20231230195921.png]]

![[Pasted image 20231230195951.png]]

![[Pasted image 20231230200023.png]]

GET /jwtDefault/rDecoder.tok > Decoder Token

radioUser role > radioMonitor role > radioDecoder role

Summary:

Decoding 1
![[Pasted image 20231230194832.png]]

Decoding 2
![[Pasted image 20231230194503.png]]

Decoding 3
![[Pasted image 20231230195019.png]]

##### Summary
- Creativity of these challenges are very good
- Always fun to play 