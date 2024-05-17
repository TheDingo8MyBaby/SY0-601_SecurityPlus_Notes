- There's a lot of security that happens at the physical switch interface
	- Often the first and last point of transmission
- Different options are available
	- Manage different security issues
## Broadcasts
- Send information to everyone at once
	- One frame or packet, received by everyone
	- Every device must examine the broadcast
- Limited scope
	- The broadcast domain
- Routing updates, ARP requests
	- Can add up quickly
- Malicious software or a bad NIC
	- Not always normal traffic
- Not used in IPv6
	- Focus on multicast
## Broadcast storm control
- The switch can control broadcasts
	- Limit the number of broadcasts per second
- Can often be used to control multicast and unknown unicast traffic
	- Tight security posture
- Manage by specific values or by percentage
	- Or the change over normal traffic patterns
## Loop protection
- Connect two switches to each other
	- They'll send traffic back and forth forever
	- There's no "counting" mechanism at the MAC layer
- This is an easy way to bring down a network
	- And somewhat difficult to troubleshoot
	- Relatively easy to resolve
- IEEE Standard 802.1D to prevent loops in bridged (switched) networks (1990)
	- Created by Radia Perlman
		- Used practically everywhere
## Spanning tree protocol
![](../Images/240516-1%203.png)
## BPDU guard
- Spanning tree takes time to determine if a switch port should forward frames
	- Bypass the listening and learning states
	- Cisco calls this  `PortFast`
- BPDU (Bridge Protocol Data Unit)
	- The spanning tree control protocol
- If a BPDU frame is seen on a PortFast configured interface.  ||  i.e:) A workstation
		- Shut down the interface
	- This shouldn't happen
	- Workstations don't send BPDUs
## DHCP snooping
- IP tracking on a layer 2 device (Switch)
	- The switch is a DHCP firewall
	- Trusted:
		- Routers
		- Switches
		- DHCP Servers
	- Untrusted:
		- Other computers
		- Unofficial DHCP Servers
- Switch watches for HDCP conversations
	- Adds a list of untrusted devices to a table
- Filters invalid IP and HDCP information
	- Static IP addresses
	- Devices acting as DHCP servers
	- Other invalid traffic patterns
## MAC filtering
- Media Access Control
	- The "hardware" address
- Limit access through the physical hardware address
	- Keeps the neighbors out
	- Additional administration with visitors
- Easy to find working MAC addresses through wireless LAN analysis
	- MAC addresses can be spoofed
		- Free open-source software
- Security through obscurity
