- Minimize the attack surface
	- Remove all possible entry points
- Remove the potential for all known vulnerabilities
	- As well as the unknown
- Some hardening may have compliance mandates
	- HIPAA Servers
	- PCI DSS
	- Etc...
- There are many different resources
	- Center for Internet Security (CIS)
	- Network and Security Institute (SANS)
	- National Institute of Standards and Technology (NIST)
## Open ports and services
- Every open port is a possible entry point
	- Close everything except required ports
- Control access with a firewall
	- NGFW would be ideal
- Unused or unknown services
	- Installed with the OS or from other applications
- Applications with broad port ranges
	- Open port `0` through `65,535`
- Use Nmap or similar port scanner to verify
	- Ongoing monitoring is important
## Registry
- The primary configuration database for Windows
	- Almost everything can be configured from the registry
- Useful to know what an application modifies
	- Many third-party tools can show registry changes
- Some registry changes are important security settings
	- Configure registry permissions
	- Disable SMBv1
## The Windows registry
![](../Images/240515-1%202.png)
## Disk encryption
- Prevent access to application data files
	- File system encryption
- Full disk encryption (FDE)
	- Encrypt everything on the drive
		- BitLocker
		- FileVault
		- Etc...
- Self-encrypting drive (SED)
	- Hardware-based full disk encryption
	- No operating system software needed
- Opal storage specification
	- The standard for the SED storage
## Operating system hardening
- Many and varied
	- Windows
	- Linux
	- iOS
	- Android
	- Etc...
- Updates
	- Operating system updates
		- Service packs
	- Security patches
- User accounts
	- Minimum password lengths and complexity
	- Account limitations
- Network access and security
	- Limit network access
- Monitor and secure
	- Anti-virus
	- Anti-malware
## Patch management
- Incredibly important
	- System stability
	- Security fixes
- Monthly updates
	- Incremental (and important)
- Third-party updates
	- Application developers
		- Device drivers
- Auto-update
	- Not always the best option
- Emergency out-of-band updates
	- Zero-day and important security discoveries
## Sandboxing
- Applications cannot access unrelated resources
	- They play in their own sandbox
- Commonly used during development
	- Can be a useful production technique
- Used in many different deployments
	- Virtual machines
	- Mobile devices
	- Browser iframes (Inline Frames)
	- Windows User Account Control (UAC)

