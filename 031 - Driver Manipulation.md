## Malware hide-and-go-seek
- Traditional anti-virus is very good at identifying known attacks
	- Checks the signature
	- Blocks anything that matches
- There are still ways to infect and hide
	- It's a constant war
	- Zero-day attacks, new attack types, etc...

## Your drivers are powerful
- The interaction between the hardware and your operating system
	- They are often trusted
	- Great opportunity for security issues
- May 2016 - HP Audio Drivers
	- Conexant audio chips
	- Driver installation includes audio control software
	- Debugging feature enables a keylogger
- Hardware interaction contain sensitive information
	- Video, keyboard, mouse

## Shimming
- Filling in the space between two objects
	- A middleman
- Windows includes it's own shim
	- Backwards compatibility with previous Windows versions
	- Application Compatibility Shim Cache
- Malware authors write their own shims
	- Get around security (like UAC)
- January 2015 Microsoft vulnerability
	- Elevates privilege

## Refactoring
- Metamorphic malware
	- A different program each time it's downloaded
- Make it appear different each time
	- Add NOP (No Operation) Instructions
		- This does nothing, except makes it look different
	- Loops, pointless code strings
- Can intelligently redesign itself
	- Reorder functions
	- Modify the application flow
	- Reorder code and insert unused data types
- Difficult to match with signature-base detection
	- Use a layered approach

