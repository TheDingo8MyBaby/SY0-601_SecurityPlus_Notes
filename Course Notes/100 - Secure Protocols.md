## Voice and Video
- SRTP
	- Secure Real-Time Transport Protocol / Secure RTP
- Ads security features to RTP
	- Keeps conversations private
- Encryption
	- Uses AES to encrypt the voice/video flow
- Authentication, Integrity, and Replay protection
	- HMAC-SHA1
		- Hash-Based message authentication code using SHA1
## Time synchronization
- Classic NTP has no security features
	- Exploited as amplifiers in DDoS attacks
	- NTP has been around prior to 1985
- NTPsec
	- Secure network time protocol
	- Began development in June of 2015
- Cleaned up the code base
	- Fixed a number of vulnerabilities
## Email
- S/MIME
	- Secure/Multipurpose Internet Mail Extensions
	- Public key encryption and digital signing of mail content
	- Requires a PKI or similar organization of keys
- Secure POP and Secure IMAP
	- Use a STARTTLS Extension to encrypt POP3 with SSL or use IMAP with SSL
- SSL/TLS
	- If the mails is browser based
		- Always encrypt with SSL
## Web
- SSL/TLS
	- Secure Sockets Layer
	- Transport Layer Security
- HTTPS
	- HTTP over TLS
		- HTTP over SSL
	- HTTP Secure
- Uses public key encryption
	- Private key on the server
	- Symmetric session key is transferred using asymmetric encryption
	- Security and speed
## IPsec (Internet Protocol Security)
- Security for OSI Layer 3
	- Authentication and encryption for every packet
- Confidentiality and integrity/anti-replay
	- Encryption and packet signing
- Very standardized
	- Common to use multi-vendor implementations
- Two core IPsec protocols
	- Authentication Header (AH)
	- Encapsulation Security Payload (ESP)
## File transfer
- FTPS
	- FTP over SSL (FTP-SSL)
	- File Transfer Protocol Secure
		- This is NOT SFTP
- SFTP
	- SSH File Transfer Protocol
	- Provides file system functionality
		- Resuming interrupted transfers
		- Directory listings
		- Remote file removal
## LDAP (Lightweight Directory Access Protocol)
- Protocol for reading and writing directories over an IP network
	- An organized set of records
		- Like a phone directory
- X.500 Specification was written by the International Telecommunications Union (ITU)
	- They know directories!
- DAP ran on the OSI protocol stack
	- LDAP is lightweight, and uses TCP/IP
- LDAP is the protocol used to query and update an X.500 directory
	- Used in:
		- Windows Active Directory
		- Apple OpenDirectory
		- OpenLDAP
		- Etc...
## Directory services
- LDAP (Lightweight Directory Access Protocol)
- LDAPS (LDAP Secure)
	- A non-standard implementation of DAP over SSL
- SASL (Simple Authentication and Security Layer)
	- Provides authentication using many different methods
		- IE:) Kerberos or client certificate
## Remote access
- SSH (Secure Shell)
	- Encrypted terminal communication
	- Replaces Telnet (and FTP)
	- Provides secure terminal communication file transfer features
## Domain name resolution
- DNS had no security in the original design
	- Relatively easy to poison a DNA
- DNSEC
	- Domain Name System Security Extensions
- Validate DNS responses
	- Origin authentication
	- Data integrity
- Public key cryptography
	- DNS records are signed with a trusted third party
	- Signed DNS records are published in DNS
## Routing and switching
- SSH - Secure Shell
	- Encrypted terminal communication
- SNMPv3 - Simple Network Management Protocol version 3
	- Confidentiality
		- Encrypted Data
	- Integrity
		- No tampering of data
	- Authentication
		- Verifies the source
- HTTPS
	- Browser-based management
	- Encrypted communication
## Network address allocation
- Securing DHCP
	- DHCP does not include any built-in security
	- There is no "secure" version of the DHCP protocol
- Rogue DHCP servers
	- In Active Directory
		- DHCP server must be authorized
	- Some witches can be configured with "Trusted" interfaces
	- DHCP distribution is only allowed form trusted interfaces
	- Cisco calls this DHCP Snooping
- DHCP client DoS - Starvation attack
	- Use spoofed MAC addresses to exhaust the DHCP pool
- Switches can be configured to limit the number of MAC addresses per interface
	- Disable an interface when multiple MAC addresses are seen
## Subscription services
- Automated subscriptions
	- Anti-virus / Anti-malware signature updates
	- IPS updates
	- Malicious IP address databases
		- Firewall updates
- Constant updates
	- Each subscription uses a different update method
- Check for encryption and integrity checks
	- May require an additional public key configuration
	- Set up a trust relationship
		- Certificates
		- IP Addresses

