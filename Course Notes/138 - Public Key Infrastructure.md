## Public Key Infrastructure (PKI)
	- Policies
	- Procedures
	- Hardware
	- Software
	- People
		- Digital certiicates:
			- Create
			- Distribute
			- Manage
			- Store
			- Revoke
- This is a big, big, endeavor
	- Lots of planning
- Also refers to the binding of public keys to people or devices
	- The certificate authority
		- It's all about trust
## The key management lifecycle
- Key generation
	- Create a key with the requested strength using the proper cipher
- Certificate generation
	- Allocate a key to a user
- Distribution
	- Make the key available to the user
- Storage
	- Securely store and protect against unauthorized use
- Revocation
	- Manage keys that have been compromised
- Expiration
	- A certificate may only have a certain "Shelf life"
## Digital certificates
- A public key certificate
	- Binds a public key with a digital signature
	- And other details about the key holder
- A digital signature adds trust
	- PKI uses Certificate Authority for additional trust
	- Web of Trust adds other users for additional trust
- Certificate creation can be built into the OS
	- Part of Windows Domain services
	- 3rd-party Linux options
## Commercial certificate authorities
- Built-in to your browser
	- Any browser
- Purchase your web site certificate
	- It will be trusted by everyone's browser
- Create a key pair
	- Send the public key to the CA to be signed
		- A certificate signing request (CSR)
- Many provide different levels of trust and additional features
	- Add a new "Tag" to your web site
## Private certificate authorities
- You are your own CA
	- Build it in-house
	- Your devices must trust the internal CA
- Needed for medium-to-large organizations
	- Many web servers and privacy requirements
- Implement as part of your overall computing strategy
	- Windows Certificate Services
	- OpenCA (Linux)
## PKI trust relationships
- Single CA
	- Everyone receives their certificates from one authority
- Hierarchical
	- Single CA issues certs to intermediate CAs
	- Distributes the certificate management load
	- Easier to deal with the revocation of an intermediate CA than the root CA
![](../Images/240603-1%202.png)
## Registration authority (RA)
- The entity requesting the certificate needs to be verified
	- The RA identifies and authenticates the requester
- Approval or Rejection
	- The foundation of trust in this model
- Also responsible for revocations
	- Administratively revoked or by request
- Manages renewals and re-key requests
	- Maintains certificates for current cert holders
## What's in a digital certificate?
![](../Images/240603-1%203.png)
## Important certificate attributes
- Common Name (CN)
	- The FQDN (Fully Qualified Domain Name) for the certificate
- Subject Alternative Name (SAN)
	- Additional host names for the cert
	- Common on web servers
		- `Professormesser.com`
		- `www.Professormess.com`
- Expiration
	- Limit exposure to compromise
	- 398 day browser limit (13 months)
![](../Images/240603-1%204.png)
## Key revocation
- Certificate Revocation List (CRL)
	- Maintained by the Certificate Authority (CA)
	- Can contain many revocations in a large file
- Many different reasons
	- Changes all the time
- April 2014:  CVE-2014-0160
	- Heartbleed
		- OpenSSL Flaw put the private key of affected web servers at risk
		- OpenSSL was patched
			- Every web server certificate was replaced
		- Older certificates were moved to the CRL
## CRL Example:
![](../Images/240603-1%205.png)
## Getting revocation details to the browser
- OCSP (Online Certificate Status Protocol)
	- The browser can check certificate revocation
- Messages usually sent to an OCSP responder via HTTP
	- Easy to support over Internet links
	- More efficient than downloading a CRL
- Not all browsers/apps support OCSP
	- Early Internet Explorer versions did not support OCSP
	- Some support OCSP, but don't bother checking

