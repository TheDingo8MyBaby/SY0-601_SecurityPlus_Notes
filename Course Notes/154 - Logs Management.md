## Syslog
- Standard for message logging
	- Diverse systems create a consolidated log
- Usually a central logging receiver
	- Integrated into the SIEM (Security Information and Event Manager)
- Each log entry is labeled
	- Facility code
		- Program that created the log
	- Severity Level
- Syslog daemon options
	- Rsyslog
		- Rocket-fast System for log precessing
	- Syslog-ng
		- Popular syslog daemon with additional filtering and storage options
	- NXLog
		- Collection from many diverse log types
![](../Images/240606-1%206.png)
## Journalctl
- Linux has a lot of logs
	- The OS
	- Daemons
	- Applications
	- Etc...
- System logs are stored in a binary format
	- Optimized for storage and queries
	- Can't read them with a text editor
- Journalctl provides a method for querying the system journal
	- Search an d filter
	- View as plain text
![](../Images/240606-2%204.png)
## Bandwidth monitors
- The fundamental network statistic
	- Percentage of network use overtime
- Many different ways to gather this metric
	- SNMP
	- NetFlow
	- sFlow
	- IPFIX
	- Protocol analysis
	- Software agent
- Identify fundamental issues
	- Nothing works properly if bandwidth is highly utilized
## Metadata
	- Data that describes other data sources
- Email
	- Header details
	- Sending servers
	- Destination address
- Mobile
	- Type of phone
	- GPS Location
- Web
	- Operating system
	- Browser type
	- IP address
- Files
	- Name
	- Address
	- Phone number
	- Title
## Email metadata/header
![](../Images/240606-1%207.png)
## NetFlow
- Gather traffics statistics from all traffic flows
	- Shared communication between devices
- NetFlow
	- Standard collection method
	- Many products and options
- Probe and collector
	- Probe watches network communication
	- Summary records are sent to the collector
![](../Images/240606-1%208.png)
- Usually a separate reporting app
	- Closely tied to the collector
## NetFlow Frontend
![](../Images/240606-2%205.png)
![](../Images/240606-1%209.png)
## IPFIX
- IP Flow Information Export
	- A newer, NetFlow-based standard
		- Evolved from NetFlow v9
- Flexible data support
	- Templates are used to describe the data
## sFlow
- sFlow (Sampled Flow)
	- Only a portion of the actual network traffic
		- Technically not a flow
- Usually embedded in the infrastructure
		- Switches
		- Routers
	- Sampling usually occurs in the hardware/ASICs
- Relatively accurate statistics
	- Useful information regarding;
		- Video streaming
		- High-traffic applications
![](../Images/240606-1%2010.png)
## Protocol analyzer output
- Solve complex application issues
	- Get into the details
- Gathers packets on the network
	- Or in the air
	- Sometimes built into the device
- View detailed traffic information
	- Identify unknown traffic
	- Verify packet filtering and security controls
	- View a plain-language description of the application data
![](../Images/240606-1%2011.png)
