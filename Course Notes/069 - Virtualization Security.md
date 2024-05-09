## VM sprawl avoidance
- Click a button
	- You've built a server
		- Or Multiple servers, networks, and firewalls
- It becomes almost too easy to build instances
	- This can get out of hand very quickly
- The virtual machines are sprawled everywhere
	- You aren't sure which VMs are related to which applications
	- It becomes extremely difficult to deprovision
- Formal process and detailed documentation
	- You should have information on every virtual object

## VM escape protection
- The virtual machine is self-contained
	- There's no way out
		- Or is there?
- Virtual machine escape
	- Break out of the VM and interact with the host operating system or hardware
- Once you escape the VM, you have great control
	- Control the host and control other guest VMs
- This would be a huge exploit
	- Full control of the virtual world

## Escaping the VM
- March 2017:  Pwn2Own competition
	- Hacking Contest
		- You pwn it, you own it
- JavaScript Engine bug in Microsoft Edge
	- Code execution in the Edge sandbox
- Windows 10 kernel bug
	- Compromise the guest operating system
- Hardware simulation bug in VMware
	- Escape to the host

