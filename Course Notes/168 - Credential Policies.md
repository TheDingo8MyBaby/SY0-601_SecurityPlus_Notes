## Credential management
- All that stands between the outside world and all of the data
	- The data is everything
- Passwords must not be embedded in the application
	- Everything needs to reside on the server, not the client
- Communication across the network should be encrypted
	- Authentication traffic should be impossible to see
## Personnel accounts
- An account on a computer associated with a specific person
	- The computer associates the user with a specific identification number
- Storage and files can be private to that user
	- Even if another person is using the same computer
- No privileged access to the operating system
	- Specifically not allowed on a user account
- This is the account type most people will use
	- Your user community
## Third-party accounts
- Access to external third-party systems
	- Cloud platforms for payroll
	- Enterprise resource planning
	- Etc...
- Third-party access to corporate systems
	- Access can come from anywhere
- Add additional layers of security
	- 2FA (Two factor authentication)
	- Audit the security posture of third-parties
- Don't allow account sharing
	- All users should have their own account
## Device accounts
- Access to devices
	- Mobile devices
- Local security
	- Device certificate
	- Require screen locks and unlocking standards
	- Manage through a Mobile Device Manager (MDM)
- Add additional security
	- Geography-based
	- Include additional authentication factors
	- Associate a device with a user
## Service accounts
- Used exclusively by services running on a computer
	- Non interactive / user access (ideally)
		- Web server
		- Database Server
		- Etc...
- Access can be defined for a specific service
	- Web server rights and permissions will be different than a database server
- Commonly use usernames and passwords
	- You'll need to determine the best policy for password updates
## Administrator / Root accounts
- Elevated access to one or more systems
	- Super user access
- Complete access to the system
	- Often used to manage;
		- Hardware
		- Drivers
		- Software installation
- This account should not be used for normal administration
	- User accounts should be used
- Needs to be highly secured
	- Strong passwords
		- Scheduled password changes
	- 2FA

