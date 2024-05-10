## The MAC address
- Ethernet Media Access Control address
	- The "physical" address of a network adapter
	- Unique to a device
- 48 bits / 6 bytes long
	- Displayed in hexadecimal
![](Images/Pasted%20image%2020231204224406.png)## LAN switching
- Forward or drop frames
	- Based on the destination MAC address
- Gather a constantly updating list of MAC addresses
	- Builds the list based on the source MAC address of incoming traffic
	- These age out periodically, often in minutes
- Maintain a loop-free environment
	- Using Spanning Tree Protocol (STP)

## Learning the MACs
- Switches examine incoming traffic
	- Makes a note of the **source** MAC address
- Adds unknown MAC addresses to the MAC address table
	- Sets the output interface to the received interface
![](Images/Pasted%20image%2020231204224632.png)## Frame switching
![](Images/Pasted%20image%2020231204224746.png)## MAC flooding
- The MAC table is only so big
- Attacker starts sending traffic with different source MAC addresses
	- Force out the legitimate MAC addresses
- The table fills up
	- Switch begins flooding traffic to all interfaces
- This effectively turns the switch into a hub
	- All traffic is transmitted to all interfaces
	- No interruption in traffic flows
- Attacker can easily capture all network traffic
- Flooding can be restricted in the switch's port security settings

## MAC cloning / MAC spoofing
- An attacker changes their MAC address to match the MAC address of an existing device
	- A clone / a spoof
- Circumvent filters
	- Wireless or wired MAC filters
	- Identify a valid MAC address and copy it
- Create a DoS
	- Disrupt communication to the legitimate MAC
- Easily manipulated through software
	- Usually a device driver option

