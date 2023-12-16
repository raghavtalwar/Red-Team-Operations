
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





---
##### Summary
- Creativity of these challenges are very good
- Always fun to play 