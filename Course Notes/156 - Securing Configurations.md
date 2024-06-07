## Configuration changes
- Firewall rules
	- Manage application flows
	- Block dangerous applications
- Mobile Device Manager (MDM)
	- Enable or disable phone and tablet functionality
		- Regardless of physical location
- Data Loss Prevention (DLP)
	- Block transfer of personally identifiable information (PII) or sensitive data
		- Credit card numbers
		- Social security numbers
		- Etc...
## Configuration changes
- Content filter / URL filter
	- Limit access to untrusted websites
	- Block known malicious sites
	- Large blocklists are used to share suspicious site URLs
- Updating or revoking certificates
	- Manage device certificates to verify trust
	- Revoking a certificate effectively removes access
![](../Images/240606-1%2012.png)
## Isolation
- Administratively isolate a compromised device from everything else
	- Prevent the spread of malicious software
	- Prevent remote access or C2 (Command and Control)
- Network isolation
	- Isolate to a remediation VLAN
	- No communication to other devices
- Process isolation
	- Limit application execution
	- Prevent malicious activity 
		- But still allow device management
![](../Images/240606-2%206.png)
![](../Images/240606-3%203.png)
## Containment
- Application containment
	- Run each application in its own sandbox
	- Limit interaction with the host operating system and other applications
	- Ransomware would have no method of infection
- Contain the spread of a multi-device security event
		- i.e:) Ransomware
	- Disable administrative shares
	- Disable remote management
	- Disable local account access
		- Change local administrator password
## Segmentation
- Separate the network
	- Prevent unauthorized movement
	- Limit the scope of a breach
![](../Images/240606-4%202.png)
![](../Images/240606-1%2013.png)
## SOAR
- Security Orchestration, Automation, and Response
	- Integrate third-party tools and data sources
	- Make security teams more effective
- Runbooks
	- Linear checklist of steps to perform
	- Step-by-step approach to automation
		- Reset a password
		- Create a website certificate
		- Backup application data
- Playbooks
	- Conditional steps to follow
		- A broad process
	- Investigate a data breach
	- Recover from ransomware

