
# Overview
A Beacon Object File (BOF) is a compiled C program designed to run within the Beacon process, leveraging Beacon's internal APIs.
- Use Case: Extends the Beacon agent with new post-exploitation features without creating new processes.
- Some BOF directly call WIN32 APIs (User Land) whereas Others might leverage direct system calls (Kernel)
## Benefits of BOFs

    - OPSEC Friendly: Executes within the Beacon process, no new process creation required.
    - Memory Efficient: Uses Malleable C2 profiles within the process-inject block for better memory management.

    - Small Size: BOFs are significantly smaller than equivalent Reflective DLLs, important for bandwidth-constrained operations (e.g., DNS communication).

    - Ease of Development: Simple C code compiled with a Win32 C compiler like MinGW or Microsoft's compiler, without complex project configurations.


# Situational Awareness BOF


# InlineWhispers
A tool to facilitate the use of direct system calls in Cobalt Strike's Beacon Object Files (BOFs) to evade common security product hooks that monitor Win32 API functions.

What is this repository for? To demonstrate the ability to make direct syscalls from within BOFs, enhancing the stealth of the operations by avoiding hooked API calls.



##### **BOFAllTheThings**
https://github.com/N7WEra/BofAllTheThings/blob/main/README.md
