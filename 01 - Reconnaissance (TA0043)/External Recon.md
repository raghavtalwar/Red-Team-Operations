
Tags: [[Reconnaissance (TA0043)]]
[[Reconnaissance (TA0043)]]
## RustScan Scanning

Tags: #ExternalScanning [[External Recon#RustScan Scanning]] 

```
#!/bin/bash

# List of domains
domains=("blacklist.com")

# Iterate through the domains
for domain in "${domains[@]}"; do
    echo "Scanning $domain"
    
    # Execute rustscan command
    /opt/RustScan/target/release/rustscan -a "$domain" --scan-order "Random" -b 1000 -t 5000 -- -sV -sC
    
    # Add a delay if needed to avoid overloading the target
    sleep 5
done

echo "Scan complete."
```

## Subdomain Flyover

Tools: GoWitness & Chromium

```
# Gather
gowitness file -f allURL.txt   

# View
gowitness server
```


## Nuclei Scanner

```
/opt/nuclei -l allURL.txt -s medium | tee Medium.txt
```

### Vhosts Fuzzing
```
ffuf -H "Host: FUZZ.group.com" -c -w "/usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt" -u http://group.com/

## Resources
Hacker Recipes
```

### Directory Fuzzing
```
## Scan all URL 
cat allURL.txt | feroxbuster --stdin --silent -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -k
```