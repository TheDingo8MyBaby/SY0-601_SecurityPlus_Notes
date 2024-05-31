## HA across zones
- Availability Zones (AZ)
	- Isolated locations within a cloud region
		- Geographical location
	- AZ commonly spans across multiple regions
	- Each AZ has independent power
		- HVAC
		- Networking
- Build applications to be highly available (HA)
	- Run as active/standby
		- Or active/active
	- Application recognizes an outage and moves to the other AZ
- Use load balancers to provide seamless HA
	- Users don't experience any application issues
## Resource policies
- Identify and access management (IAM)
	- Who gets access
	- What they get access to
- Map job functions to roles
	- Combine users into groups
- Provide access to cloud resources
	- Set granular policies
		- Group
		- IP Address
		- Data and Time
- Centralize user accounts
	- Synchronize across all platforms
## Secrete management
- Cloud computing includes many secrets
	- API Keys
	- Passwords
	- Certificates
- This can quickly become overwhelming
	- Difficult to manage and protect
- Authorize access to the secretes
	- Limit access to the secret service
- Manage an access control policy
	- Limit users to only necessary secrets
- Provide an audit trail
	- Know exactly who accesses secrets and when
## Integration and auditing
- Integrate security across multiple platforms
	- Different operating systems and applications
- Consolidate log storage and reporting
	- Cloud-based Security Information and Event Management (SIEM)
- Auditing
	- Validate the security controls
	- Verify compliance with financial and user data

