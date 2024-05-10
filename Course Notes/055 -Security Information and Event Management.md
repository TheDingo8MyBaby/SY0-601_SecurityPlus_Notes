## SIEM
- Security Information and Event Management (Device)
	- Logging of security events and information
- Log collection of security alerts
	- Real-time Information
- Log aggregation and Long-Term storage
	- usually includes advanced reporting features
- Data correlation
	- Link diverse data types
- Forensic analysis
	- Gather details after an event

## Syslog
- Standard for message logging
	- Diverse systems
		- Consolidated log
- Usually a central log collector
	- Integrated into the SIEM
- You're going to need A LOT of disk space
	- No, more.
		- More than that.
	- Data storage from many devices over an extended timeframe

## SIEM Data
- Data inputs
	- Server Authentication attempts
	- VPN Connections
	- Firewall session logs
	- Denied outbound traffic flows
	- Network utilizations
- Packet captures
	- Network packets
	- Often associated with a critical alert
	- Some organizations capture everything

## SOC
- Security Operations Center

## Security Monitoring
- Constant Information Flow
	- Important metrics in the incoming logs
- Track important statistics
	- Exceptions can be identified
- Send alerts when problems are found
	- Email
	- Tet
	- Call
	- Etc...
- Create triggers to automate responses
	- Open a Ticket
	- Reboot a server

## EventLog Analyzer

![](Images/Pasted%20image%2020240320201522.png)
![](Images/Pasted%20image%2020240320201600.png)
## Security Reports

![](Images/Pasted%20image%2020240320201623.png)
## Analyzing the data
- Big data analytics
	- Analyze large data stores
	- Identify patterns that would normally remain invisible
- User and entity behavior analytics (UEBA)
	- Detect insider threats
	- Identify targeted attacks
	- Catches what the SIEM and DLP systems might miss
- Sentiment analysis
	- Public discourse correlates to real-world behavior
	- If they hate you
		- They hack you
	- Social media can be a barometer

## SOAR
- Security Orchestration, Automation, and Response
	- Automate routine, tedious, and time intensive activities
- Orchestration
	- Connect many different tools together
		- Firewalls
		- Account Management
		- Email Filters
- Automation
	- Handle security tasks automatically
- Response
	- Make changes immediately

