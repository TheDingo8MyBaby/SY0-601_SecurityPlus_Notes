## Honeypots
- Attract the bad guys
	- And trap them there
- The "attacker" is probably a machine
	- Makes for interesting recon
- Honeypots
	- Create a virtual world to explore
- Many different options
	- Kippo
	- Google Hack Honeypot
	- Wordpot
	- Etc...
- Constant battle to discern the real from the take

## Honeyfiles and Honeynets
- Honeynets
	- More than one honeypot on a network
	- More than one source of information
	- Stop spammers
		- https://projecthoneypot.org
- Honeyfiles
	- Bait for the honeynet (passwords.txt)
	- An alert is sent if the file is accessed
		- A virtual bear trap

## Fake Telemetry
- Machine learning
	- Interpret big data to identify the invisible
- Train the machine with actual data
	- Learn how malware looks and acts
	- Stop malware based on actions instead of signatures
- Send the machine learning model fake telemetry
	- Make malicious malware look benign

## DNS sinkhole
- A DNS that hands out incorrect IP addresses
	- Blackhole DNS
- This can be bad
	- An attacker can redirect users to a malicious site
- This can be good
	- Redirect known malicious domains to a benign IP address
	- Watch for any users hitting that IP address
	- Those devices are infected
- Can be integrated with a firewall
	- Identify infected devices not directly connected

