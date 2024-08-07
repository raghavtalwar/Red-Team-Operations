# Red Team Operation & Adversary Simulation
## Course Notes & Discord Buddies
- Pyro: sick! SANS is pretty good stuff, be sure to take advantage of asking the SANS people questions and learning from them because that's fantastic
- Noopy | RedByte | SkelSec
---
## Lab Setup
- Root Password - Woodywood
- sec565 Password - Woodywood

IP Check - `ip a | grep tun0 - inet 10.254.252.2/23
Ping Check - `ping -c 4 www.draconem.io

----
## Lab 0 - Slingshot Linux VM Setup
The SEC565 Exercise Workbook is full of critical information that will help you conduct impactful Red Team Operations by reinforcing the knowledge from the courseware with hands-on practical exercises.
- Make sure to read Exercise Objectives
- Exercise preparation needs to be followed
- Learn the tradecraft of Tools - Focus on output and understand it 
- "On Your Own" and "Walkthrough" 
- For every exercise, the conclusion section highlights the important concepts and reinforces any Red Team Tips picked up along the way.
![[Pasted image 20240113175942.png]]

**Crush Labs inside out - Take advantage of the structure of the exercises to facilitate the maximum learning possible for your particular skill level and background. Good luck!

----
## SANS SME Support

Tags: #customExecutables #obfuscation
### 3.1 Weaponization - Slide 7 - Custom Executables
1. How to obfuscate tools like Rubeus or Cred dumping technique to use them on engagements

There are many ways to do this, however, the most effective way is to understand your target environment. Knowing the detective capability, sophistication of capability, alertness of the team, etc.  In general, you may obfuscate using the following consideration:

- **Source Code Modification:** If the tool is open-source (like Rubeus), you can modify its source code. This could involve renaming functions and variables, changing the control flow, or implementing custom encryption for data handling.
- **Binary Packing and Encryption:** Use binary packers or encryptors to alter the binary's signature, making it harder for antivirus programs to detect.
- **Using Custom Scripts:** Instead of using well-known tools directly, write custom scripts that perform similar functions but have different signatures and behaviors.
- **Execution in Memory:** Techniques like reflective loading or in-memory execution can help avoid disk-based detections.
- **Bypassing Anti-Virus Heuristics:** Continuously test the tool against various antivirus solutions and modify your approach to bypass heuristic detections.
- **Utilizing Trusted Binaries:** Leveraging trusted system binaries (Living off the Land techniques) can help in evading detection.

2. Difference in modification of C# and PS tools

The two have very different way of modification.

**C# Modifications:**

- **Compilation Required:** C# is a compiled language, so any modification requires recompiling the source code.
- **Rich Library Support:** C# has extensive libraries and frameworks, allowing more complex modifications.
- **Obfuscation Techniques:** Tools can be obfuscated at the code level or post-compilation using .NET obfuscators.
- **Strong Typing:** Modifications must adhere to strict type-checking rules.

**PowerShell Modifications:**

- **Scripting Language:** PowerShell is a scripting language and doesn't require compilation, making on-the-fly modifications easier.
- **Cmdlet Usage:** Modifications often involve the creative use of existing cmdlets.
- **Easier to Obfuscate:** Scripts can be obfuscated by altering command names, using aliases, or encoding scripts.
- **Integrated with Windows Environment:** Modifications can leverage deep integration with the Windows OS for specific tasks.

---
## Final Course Content
- Audio Material
- Books
- PDF
- Lab Videos & Guide

----
## INDEX

![[Pasted image 20240402011753.png]]

Go through all the books 
- Make notes of each slide

![[Pasted image 20240402011834.png]]

- Slide Title Name
	- Pg 2 Slide 6
	- Time is the enemy 
	- 90 seconds - 1 question

- Index 
	- Not to open the book
	- Master Cheatsheet
	- Close to 20 to 25 days
	- Improve and Refresh Knowledge
	- 90 to 95%

Create 
- Go Book by Book
	- GO one for the Book

Q > tcpdump > Hey what does this command will accomplish 

600 Lines of entry
- Index good but not finding info
- Make index > A to Z arrange krrdo
- Organise it via Index alphabetically

![[Pasted image 20240402012338.png]]

![[Pasted image 20240402013408.png]]