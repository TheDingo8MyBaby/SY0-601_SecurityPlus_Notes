## Virus
- Malware that can reproduce itself
	- It needs you to execute a program
		- Requires human interaction
- Reproduces through file systems or the network
	- Just running a program can spread a virus
- May or may not cause problems
	- Some viruses are invisible, some are annoying
		- Annoying = Pop-up Ads
- Anti-virus is very common
	- Thousands of new viruses every week
	- Is your signature file updated?

## Virus types
- Program viruses
	- It's part of the application
- Boot sector viruses
	- Who needs an OS?
		- Held within the storage device
- Script viruses
	- Operating system and browser-based
- Macro viruses
	- Common in Microsoft Office

## Fileless virus
- A stealth attack
	- Does a good job of avoiding anti-virus detection
- Operates in memory
	- But never installed in a file or application
- Example:
	- User clicks a malicious link
		- Runs as a Flash/Java/Windows vulnerability
			- Launches a PowerShell payload in RAM
				- Can run scripts and executables in memory
					- Adds an auto-start to Registry (RegEdit)

## Worms
- Malware that self-replicates
	- Doesn't need you to do anything
	- Uses the network as a transmission medium
	- Self-propagates and spreads quickly
- Worms are pretty bad things
	- Can take over many systems very quickly
- Firewalls and IDS/IPS can mitigate many worm infestations
	- Doesn't help much once the worm gets inside

## Wannacry worm
![](Images/Pasted%20image%2020231127204843.png)
