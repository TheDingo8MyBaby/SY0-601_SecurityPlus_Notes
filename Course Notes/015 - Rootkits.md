- Originally a Unix technique
	- The "root" in rootkit
- Modifies core system files
	- Part of the kernel
		- Foundational building blocks of the OS
- Can be invisible to the operating system
	- Won't see it in Task Manager
- Also invisible to traditional anti-virus utilities
	- If you can't see it, you can't stop it

## Kernel drivers
- Zeus/Zbot malware
	- Famous for cleaning out bank accounts
- Now combined with Necurs rootkit
	- Necurs is a kernel-level driver
- Necurs makes sure you can't delete Zbot
	- Access denied
- Trying to top the Windows process?
	- Error terminating process: Access denied

## Finding and removing rootkits
- Look for the unusual
	- Anti-malware scans
- Use a remover specific to the rootkit
	- Usually built after the rootkit is discovered
- Secure boot with UEFI
	- Security in the BIOS
![](Images/Pasted%20image%2020231127211031.png)