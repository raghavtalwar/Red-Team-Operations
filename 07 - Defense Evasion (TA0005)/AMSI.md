
## AMSI Bypass in Action	
- AMSI is not a global patch, its patched for the current process only. 
- On a red team leveraging C2 framework, as some tasks might spawn a new process > Detected and Burned if we dont patch AMSI for the newly spawned process
## Over ride AMSI 
- n order to override the `amsiContext` we need to find it
- Identify the memory address of `amsiContext`
- What type of detection is that?