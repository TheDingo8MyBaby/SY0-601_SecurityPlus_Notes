- No system is secure with the default configurations
	- You need some guidelines to keep everything safe
- Hardening guides are specific to the software or platform
	- Get feedback from the manufacturer
		- Or internet interest groups
	- They'll have the best details
- Other general-purpose guides are available online
## Web server hardening
- Access a server with your browser
	- The fundamental server on the Internet
		- Microsoft Internet Information Server
		- Apache HTTP Server
		- Etc...
- Huge potential for access issues
	- Data leaks
	- Server access
- Secure configuration
	- Information leakage;
		- Banner information
		- Directory browsing
	- Permissions;
		- Run from a non privileged account
		- Configure file permissions
	- Configure SSL;
		- Manage and install certificate
	- Log files;
		- Monitor access and error logs
## Operating system hardening
- Many and varied
	- Windows
	- Linux
	- iOS
	- Android
	- Etc...
- Updates
	- Operating system updates
		- Service packs
	- Security patches
- User accounts
	- Minimum password lengths and complexity
	- Account limitations
- Network access and security
	- Limit network access
- Monitor and secure
	- Anti-virus
	- Anti-malware
## Application server
- Programming languages, runtime libraries, etc..
	- Usually between the web server and the database
	- Middleware
- Very specific functionality
	- Disable all unnecessary services
- Operating system updates
	- Security patches
- File permissions and access controls
	- Limit rights to what's required
	- Limit access from other devices
## Network infrastructure devices
	- Switches
	- Routers
	- Firewalls
	- IPS
	- Etc...
		- You never see them, the they're always there
- Purpose-built devices
	- Embedded OS
	- Limited OS access
- Configure authentication
	- Don't use the defaults
- Check with the manufacturer
	- Security updates
	- Not usually updated frequently
	- Updates are usually important

