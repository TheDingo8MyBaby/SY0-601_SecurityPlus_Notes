## Online and offline CAs
- A compromised certificate authority
	- A very, very bad thing
	- No certificates issued by that CA can be trusted
- Distribute the load
	- Then take the root CA offline and protect it
![](../Images/240603-1%208.png)
## OCSP stapling
- Online Certificate Status Protocol
	- Provides scalability for OCSP checks
- The CA is responsible for responding to all client OCSP requests
	- This may not scale well
- Instead, have the certificate holder verify their own status
	- Status information is stored on the certificate holder's server
- OCSP status is "Stapled" into the SSL/TLS handshake
	- Digitally signed by the CA
## Pinning
- You're communicating over TLS/SSL to a server
	- How do you really know it's a legitimate server?
- "Pin" the expected certificate or public key to an application
	- Compiled in the app or added at first run
- If the expected certificate or public key doesn't match, the application can decide what do do
	- Shut down
	- Show a message
## PKI trust relationships
- Single CA
	- Everyone receives their certificates from one authority
- Hierarchical
	- Single CA issues certs to intermediate CAs
![](../Images/240603-1%209.png)
- Mesh
	- Cross-certifying CAs
	- Doesn't scale well
![](../Images/240603-1%2010.png)
- Web-of-trust
	- Alterative to Traditional PKI
![](../Images/240603-2%201.png)
- Mutual Authentication
	- Server authenticates to the client and the client authenticates to the server
## Key escrow
- Someone else holds your decryption keys
	- Your private keys are in the hands of a 3rd-party
- This can be a legitimate business arrangement
	- A business might need access to employee information
	- Government agencies may need to decrypt partner data
## It's all about the process
- Need clear process and procedures
	- Keys are incredibly important pieces of information
- You must be able to trust your 3rd-party
	- Access to the keys is at the control of the 3rd-party
- Carefully controlled conditions
	- Legal proceedings and court orders
## Certificate chaining
- Chain of trust
	- List all of the certs between the server and the root CA
- The chain starts with the SSL certificate
	- And ends with the Root CA certificate
- Any certificate between the SSL certificate and the root certificate is a chain certificate
	- Or intermediate certificate
- The web server needs to be configured with the proper chain
	- Or the end user may receive an error
![](../Images/240603-1%2011.png)

