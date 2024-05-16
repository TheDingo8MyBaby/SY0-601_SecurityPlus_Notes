## Segmenting the network
- Physical, Logical, or Virtual Segmentation
	- Devices
	- VLANs
	- Virtual Networks
- Performance
	- High-bandwidth applications
- Security
	- Users should not talk directly database servers
	- The only applications in the core are SQL and SSH
- Compliance
	- Mandated segmentation (PCI compliance)
	- Makes change control much easier
## Physical segmentation
- Devices are physically separate
	- Air gap between `Switch A` and `Switch B`
- Must be connected to provide communication
	- Direct connect
		- Or another switch or router
- Web servers in one rack
	- Database servers on another
- Customer A on one switch, customer B on another
	- No opportunity for mixing data
## Physical segmentation
- Separate devices
	- Multiple units
		- Separate infrastructure
![](../Images/240515-1%203.png)
## Logical segmentation with VLANs
- Virtual Local Area Networks (VLANs)
	- Separated logically instead of physically
	- Cannot communicate between VLANs without a Layer 3 device / router
![](../Images/240515-1%204.png)
## Screened subnet
- Previously known as the demilitarized zone (DMZ)
	- An additional layer of security between the Internet and you
	- Public access to public resources
## Extranet
- A private network for partners
	- Vendors
	- Suppliers
- Usually requires additional authentication
	- Only allow access to authorized users
![](../Images/240515-2%202.png)
## Intranet
- Private network
	- Only available internally
- Company announcements
	- Important documents
	- Other Company business
		- Employees only
- No external access
	- Internal or VPN access only
![](../Images/240515-3%201.png)
## East-west traffic
- Traffic flows within a data center
	- Important to know where traffic starts and ends
- East-west
	- Traffic between devices in the same data center
	- Relatively fast response times
- North-south traffic
	- Ingress/Egress to an outside device
	- A different security posture than east-west traffic
## East-west traffic
![](../Images/240515-5%201.png)
## Zero trust
- Many networks are relatively open on the inside
	- Once you're through the firewall
		- There are few security controls
- Zero trust is a holistic approach to network security
	- Covers every device
		- Every process
		- Every person
- Everything must be verified
	- Nothing is trusted
		- Multifactor authentication
		- Encryption
		- System permissions
		- Additional firewalls
		- Monitoring and analytics
		- Etc...

