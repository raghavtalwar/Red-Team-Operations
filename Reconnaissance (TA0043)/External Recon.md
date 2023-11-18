
Tags: [[Reconnaissance (TA0043)]]

## RustScan Scanning
**{{Rustscan}}** - SKmakmcklam. ^1

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

## RustScan Scanning


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