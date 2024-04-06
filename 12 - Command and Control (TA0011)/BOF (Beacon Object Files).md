
# Overview
A Beacon Object File (BOF) is a compiled C program designed to run within the Beacon process, leveraging Beacon's internal APIs.
- Use Case: Extends the Beacon agent with new post-exploitation features without creating new processes.
## Benefits of BOFs

    - OPSEC Friendly: Executes within the Beacon process, no new process creation required.
    - Memory Efficient: Uses Malleable C2 profiles within the process-inject block for better memory management.

    - Small Size: BOFs are significantly smaller than equivalent Reflective DLLs, important for bandwidth-constrained operations (e.g., DNS communication).

    - Ease of Development: Simple C code compiled with a Win32 C compiler like MinGW or Microsoft's compiler, without complex project configurations.


# Situational Awareness BOF



# InlineExecute-Assembly
Execute .NET in an Existing Process. This tool is an alternative to traditional fork and run execution for Cobalt Strike. The loader can be injected into any process, including the current Beacon. Long-running assemblies will continue to run and send output back to the Beacon, similar to the behavior of execute-assembly. 
- Link: https://github.com/kyleavery/inject-assembly

##### **Resources**
https://github.com/N7WEra/BofAllTheThings/blob/main/README.md
