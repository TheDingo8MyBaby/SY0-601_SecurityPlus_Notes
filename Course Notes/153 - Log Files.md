## Network log files
	- Switches
	- Routers
	- Access points
	- VPN concentrators
		- And other infrastructure devices
![](../Images/240606-1%205.png)
- Network changes
	- Routing updates
	- Authentication issues
	- Network security issues
## System log files
- Operating system information
	- Extensive logs
	- File system information
	- Authentication details
- Can also include security events
	- Monitoring apps
		- Brute Force
		- File changes
- May require filtering
- Don't forward everything
![](../Images/240606-2%203.png)
## Application log files
- Specific to the application
	- Information varies widely
- Windows
	- Event Viewer
		- Application log
- Linux / macOS
	- /var/log
- Parse the log details on the SIEM
	- Filter out unneeded info
## Security log files
- Detailed security-related information
	- Blocked and allowed traffic flows
	- Exploit attempts
	- Blocked URL categories
	- DNS sinkhole traffic
- Security devices
	- IPS
	- Firewall
	- Proxy
- Critical security information
	- Documentation of every traffic flow
	- Summary of attack info
	- Correlate with other logs
## Firewall logs
![](../Images/240606-3%202.png)
![](../Images/240606-4%201.png)
## Web log files
- Web server access
	- IP Address
	- Web page URL
- Access errors
	- Unauthorized or non-existent folders/files
- Exploit attempts
	- Attempt to access files containing known vulnerabilities
- Server activity
	- Startup and shutdown notices
	- Restart messages
## DNS log files
- View lookup requests
	- And other DNS queries
- IP address of the request
	- The request FQDN or IP
- Identify queries to known bad URLs
	- Malware sites
	- Known command and control domains
- Block or modify known bad requests at the DNS server
	- Log the results
	- Report on malware activity
## Authentication log files
- Know who logged in (or didn't)
	- Account names
	- Source IP address
	- Authentication method
	- Success and failure reports
- Identify multiple failures
	- Potential brute force attacks
- Correlate with other events
	- File transfers
	- Authentications to other devices
	- Application installation
![](../Images/240606-5%201.png)
## Dump files
- Store all contents of memory into a diagnostic file
	- Developers can use this info
- Easy to create from the Windows Task Manager
	- Right-click
		- Create dump file
![](../Images/240606-6%201.png)
- Some applications have their own dump file process
	- Contact the appropriate support team for additional details
## VoIP and call manager logs
- View inbound and outbound call info
	- Endpoint details
	- Gateway communication
- Security information
	- Authentications
	- Audit trail
- SIP traffic logs
	- Session Initial Protocol
		- Call Setup
		- Management
		- Teardown
	- Inbound and outbound calls
	- Alert on unusual numbers or country codes

