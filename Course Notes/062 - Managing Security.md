## Geographical Considerations
- Legal implications
	- Business regulations vary between states
	- For a recovery site outside of the country
		- Personnel must have a passport and be able to clear immigration
	- Refer to your legal team
- Offsite Backup
	- Organization-owned site or 3rd-party secure facility
- Offsite recovery
	- Hosted in a different location
		- Outside the scope of the disaster
	- Travel Considerations for support staff and employees

## Response and recovery controls
- Incident response and recovery has become commonplace
	- Attacks are frequent and complex
- Incident response plan should be established
	- Documentation is critical
	- Identify the attack
	- Contain the attack
- Limit the impact of an attacker
	- Limit data exfiltration
	- Limit access to sensitive data

## SSL/TLS inspection
- Commonly used to examine outgoing SSL/TLS
	- Secure Sockets Layer
	- Transport Layer Security
	- For Example, from your computer to your bank
- Examine Encrypted Traffic
	- How is that possible?
- SSL/TLS relies on trust
	- Without trust, none of this works

## Trust me, I'm SSL
- Your browser contains a list of trusted CAs (Certificate Authority)
	- My browser contains about 170 trusted CAs certificates
- Your browser doesn't trust a web site, unless a CA has signed the Web Server's encryption certificate
	- The web site pays some money to the CA for this
- The CA has ostensibly performed some checks
	- Validated against the DNS record
	- Phone Call
	- Etc...
- Your browser checks the web server's certificate
	- If it's signed by a trusted CA, the encryption works seamlessly

## SSL/TLS proxy
![](Images/Pasted%20image%2020240321204706.png)
## Hashing
- Represent data as a short string of text
	- A message digest
- One-way trip
	- Impossible to recover the original message from the digest
	- Used to store passwords / confidentiality
- Verify a downloaded document is the same as the original
	- Integrity
	- If a hash you generate, matches the original hash
		- It's a valid download
- Can be a digital signature
	- Authentication
	- Non-Repudiation
	- Integrity
- Will not have a collision (hopefully)
	- Different messages will not have the same hash

## A hash example
- SHA256 hash
	- 256 bits / 64 Hexadecimal Characters
- My name is Professor Messer.
	- SHA256 hash:
```
19da9a2e26f3bff67f0522f962851c42542b8659333ac53397c8d65aa7a3f871
```
- My name is Professor Messer!
	- SHA256 hash:
```
54381cae1eea10892d81c8688d06d1928b4ee8495061a792864f83092b033aea
```

## API considerations
- API (Application Programming Interface)
	- Control software or hardware programmatically
- Secure and harden the login page
	- Don't forget about the API
- On-path attack
	- Intercept and modify API messages
	- Replay API commands
- API injection
	- Inject data into an API message
- DDoS (Distributed Denial of Service)
	- One bad API call can bring down a system

## API security
- Authentication
	- Limit API access to legitimate users
	- Over secure protocols
- Authorization
	- API should not allow extended access
	- Each user has a limited role
		- A read-only user should not be able to make changes
- WAF (Web Application Firewall)
	- Apply rules to API communication

