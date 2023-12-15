
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

