
# SetUID and SetGUID
• Normally, an executable runs in the current user’s context
• Some programs may need to be elevated to function properly, but the user does not need to be a sudoer
• Any user can set their program to run as their user
```markdown
# Find SUID
$ find / -type d \( -path /snap -o -path /proc -o -path /var \) -prune -o -perm -4000 -exec ls -ldb {} \; 2>/dev/null
# fIND GUID
$ find / -type d \( -path /snap -o -path /proc -o -path /var \) -prune -o -perm -2000 -exec ls -ldb {} \; 2>/dev/null
# File permissions
## ls -al /usr/bin/backup-db
-rwxr-xr-x 1 root root 68208 Oct 21 11:32 /usr/bin/backup-db
# Set UID
## chmod +s /usr/bin/backup-db && ls -al /usr/bin/backup-db
-rwsr-sr-x 1 root root 68208 Oct 21 11:32 /usr/bin/backup-db
```