- Gain higher-level access to a system
	- Exploit a vulnerability
	- Might be a bug or design flaw
- Higher-level access means more capabilities
	- This commonly is the highest-level access
	- This is obviously a concern
- These are high-priority vulnerability patches
	- You want to get those closed very quickly
	- Any user can be an administator
- Horizontal privilege escalation
	- User A can access user B resources

## Mitigating privilege escalation
- Patch quickly
	- Fix the vulnerability
- Updated anti-virus/anti-malware software
	- Block known vulnerabilities
- Data execution prevention
	- Only data in executable areas can run
- Address space layout randomization
	- Prevent a buffer overrun at a known memory address

## Example of privilege vulnerability
- CVE-2020-1530
	- Windows Remote Access Elevation of Privilege vulnerability
	- August 20, 2020
- Windows Remote Access
	- Server 2008, 2012, 2016, 2019
	- Windows 7, 8.1, 10
- Attacker would execute a program on a victim computer
	- Vulnerability in Remote Access would elevate privileges

