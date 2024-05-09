## Provisioning
- Deploy an application
	- Web server
	- Database server
	- Middleware server
	- User workstation configurations
	- Certificate updates
	- Etc...
- Application software security
	- Operating system
	- Application
- Network Security
	- Secure VLAN
	- Internal access
	- External access
- Software deployed to workstations
	- Check executables for malicious code
	- Verify security posture of the workstation

## Scalability and elasticity
- Handle application workload
	- Adapt to dynamic changes
- Scalability
	- The ability to increase the workload in a given infrastructure
		- Build an application instance that can handle 100,000 transactions per second
- Elasticity
	- Increase or decrease available resources as the workload changes
		- Deploy multiple application instances to handle 500,000 transactions per second

## Orchestration
- Automation is the key to cloud computing
	- Services appear and disappear automatically
		- Or, at the push of a button
- Entire application instances can be instantly provisioned
	- Servers
	- Networks
	- Switches
	- Firewalls
	- Policies
- Instances can move around the world as needed
	- "Follow the sun"
- The security policies should be part of the orchestration
	- As applications are provisioned
		- The proper security is automatically included

## Deprovisioning
- Dismantling and removing an application instance
	- All good things
- Security deprovisioning is important
	- Don't leave open holes
		- Don't close important ones
- Firewall policies must be reverted
	- If the application is gone, so is the access
- What happens to the data?
	- Don't leave information out there

