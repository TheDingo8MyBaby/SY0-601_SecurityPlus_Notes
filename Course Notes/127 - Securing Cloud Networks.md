## Cloud networks
- Connect cloud components
	- Connectivity within the cloud
	- Connectivity from outside the cloud
- Users communicate to the cloud
	- From the public Internet
	- Over a VPN tunnel
- Cloud devices communicate between each other
	- Cloud-based network
	- East/West and North/South Communication
	- No external traffic flows
## Virtual networks
- A cloud contains virtual devices
	- Servers
	- Databases
	- Storage devices
- Virtual switches
	- Virtual routers
		- Build the network from cloud console
		- The same configurations as a physical device
- The network changes with the rest of the infrastructure
	- On-demand
	- Rapid elasticity
## Public and private subnets
- Private cloud
	- All internal IP addresses
	- Connect to the private cloud over a VPN
	- No access from the Internet
- Public cloud
	- External IP addresses
	- Connect to the cloud from anywhere
- Hybrid cloud
	- Combine internal cloud resources with external
	- May combine both public and private subnets

## Segmentation
- The cloud contains separate:
		- VPCs
		- Containers
		- Microservices
	- Application segmentation is almost guaranteed
- Separation is a security opportunity
	- Data is separate from the application
	- Add security systems between application components
- Virtualized security technologies
	- Web Application Firewall (WAF)
	- Next-Generation Firewall
		- Intrusion Prevention System
## API inspection and integration
- Microservice architecture is the underlying application engine
	- A significant security concern
- API calls can include risk
	- Attempts to access critical data
	- Geographic origin
	- Unusual API calls
- API monitoring
	- View specific API queries
	- Monitor incoming and outgoing data

