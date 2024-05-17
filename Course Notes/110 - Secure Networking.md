## Domain name resolution
- DNS had no security in the original design
	- Relatively easy to poison a DNS
- DNSSEC
	- Domain Name System Security Extensions
- Validate DNS responses
	- Origin authentication
	- Data integrity
- Public key cryptography
	- DNS records are signed with a trusted third party
	- Signed DNS records are published in DNS
## Using a DNS for security
- Stop end users from visiting dangerous sites
	- The DNS resolves to a sinkhole address
- A query to a known-malicious address can identify infected systems
	- And prevent further exploitation
- Content filtering
	- Prevent DNS queries to unwanted or suspicious sites
## Out-of-band management
- The network isn't available
	- Or the device isn't accessible from the network
- Most devices have a separate management interface
	- Usually a serial connection / USB
- Connect a modem
	- Dial-in to manage the device
- Console router / comm server
	- Out-of-band access for multiple devices
	- Connect to the console router
		- Then choose where you want to go
## The need for QoS
- Many different devices
	- Desktop
	- Laptop
	- VoIP Phone
	- Mobile Devices
- Many different applications
	- Mission critical applications
	- Streaming Video
	- Streaming Audio
- Different apps have different network requirements
	- Voice is `real-time`
	- Recorded streaming video has a buffer
	- Database application is interactive
- Some applications are "more important" than others
	- Voice traffic needs to have priority over YouTube
## QoS (Quality of Service)
- Prioritize traffic performance
	- Voice over IP traffic has priority over web-browsing
	- Prioritize by maximum:
		- Bandwidth
		- Traffic Rate
		- VLAN
		- Etc...
- Quality of Service
	- Describes the process of controlling traffic flows
- Many different methods
	- Across many different topologies
## IPv6 security is different
- More IP address space
	- More difficult to IP/Port scan
		- But not impossible
	- The tools already support IPv6
- No need for NAT
	- NAT is not a security feature
- Some attacks disappear
	- No ARP
		- So no ARP spoofing
- New attacks will appear
	- For Example:
		- Neighbor Cache Exhaustion
## Taps and port mirrors
- Intercept network traffic
	- Send a copy to a packet capture device
- Physical taps
	- Disconnect the link
		- Put a tap in the middle
	- Can be an active or passive tap
- Port mirror
	- Port redirection, SPAN (Switched Port ANalyzer)
	- Software-based tap
	- Limited functionality
		- But can work well in a pinch
## Taps and Port mirrors
![](../Images/240516-1%204.png)
## Monitoring services
- Constant cybersecurity monitoring
	- Ongoing security checks
	- A staff of cybersecurity experts at a:
		- Security Operations Center (SoC)
- Identify threats
	- A broad range of threats across many different organizations
- Respond to events
	- Faster response time
- Maintain compliance
	- Someone else ensures PCI DSS, HIPAA compliance, Etc.
## FIM (File Integrity monitoring)
- Some files change all the time
	- Some files should NEVER change
- Monitor important operating system and application files
	- Identify when changes occure
- Windows - SFC (System File Checker)
- Linux - Tripwire
- Many host-based IPS options

