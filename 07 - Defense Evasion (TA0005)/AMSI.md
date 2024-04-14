
## AMSI Bypass in Action	
- AMSI is not a global patch, its patched for the current process only. 
- On a red team leveraging C2 framework, as some tasks might spawn a new process > Detected and Burned if we dont patch AMSI for the newly spawned process
## Over ride AMSI 
- In order to override the `amsiContext` we need to find it
- Identify the memory address of `amsiContext`
- Remember, AMSI is being enforced through injecting "amsi.dll" in processes that are being spawned.

This means that all the functionality of AMSI is available in that process's address space. It is here that we will already encounter our first hurdle: the “classic” approach to get this location is identified as malicious by AMSI

## Locate amsiContext
• Static analysis is the likely mechanism
• Test this hypothesis
• Use Unicode characters using built-in PowerShell functionality
```
[Ref].Assembly.GetType('System.Management.Automation.'+[regex]::Unescape('\u
0041')+'msiUtils').GetField("ams"+[regex]::Unescape('\u0069')+"Context",'Non
Public,Static').GetValue($null)
```

## AMSI under the Hood
• Now that we have the memory location
	We can create an arbitrary byte array
	Place it where amsiContext code should be
• First look at what should be there in a debugger

## Creating the AMSI Bypass
Let's create our bypass:
1. First, we are going to create a new byte array that contains the sentence "sec565 rules!!!" in hexadecimal representation
2. We will use the Count function to dynamically compute the size of the array
3. Finally, we will copy the byte array to the amsiContext location, overriding what is currently there
