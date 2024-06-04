## Web server SSL certificates
- Domain validation certificate (DV)
	- Owner of the certificate has some control over a DNS domain
- Extended Validation certificate (EV)
	- Additional checks have verified the certificate owner's identity
	- Browsers used to show a green name on the address bar
	- Promoting the use of SSL is now outdated
## Web server SSL certificates
- Subject Alternative Name (SAN)
	- Extension to an X.509 certificate
	- Lists additional identification information
	- Allows a certificate to support many different domains
- Wildcard domain
	- Certificates are based on the name of the server
	- A wildcard domain will apply to all server names in a domain
		- `*.professormesser.com`
## Code signing certificate
- Developers can provide a level of trust
	- Applications can be signed by the developer
- The user's operating system will examine the signature
	- Checks the developer signature
	- Validates that the software has not been modified
- Is it from a trusted entity?
	- The user will have the opportunity to stop the application execution
## Root certificate
- The public key certificate that identifies the root CA (Certificate Authority)
	- Everything starts with this certificate
- The root certificate issues other certificates
	- Intermediate CA certificates
	- Any other certificates
- This is a very important certificate
	- Take all security precautions
	- Access to the root certificate allows for the creating of any trusted certificate
## Self-signed certificates
- Internal certificates don't need to be signed by a public CA
	- Your company is the only one going to use it
	- No need to purchase trust for devices that already trust you
- Build your own CA
	- Issue your own certificates signed by your own CA
- Install the CA certificate (Trusted chain) on all devices
	- They'll now trust any certificates signed by your internal CA
	- Works exactly like a certificate you purchased
## Machine and computer certificates
- You have to manage many devices
	- Often devices that you'll never physically see
- How can you truly authenticate a device?
	- Put a certificate on the device that you signed
- Other business processes rely on the certificate
	- Access to the remote access VPN from authorized devices
	- Management software can validate the end device
## Email certificates
- Use cryptography in an email platform
	- You'll need public key cryptography
- Encrypting emails
	- Use a recipient's public key to encrypt
- Receiving encrypted emails
	- Use your private key to decrypt
- Digital signatures
	- Use your private key to digitally sign an email
	- Non-repudiation
		- Integrity
## User certificates
- Associate a certificate with a user
	- A powerful electronic "ID card"
- Use as an additional authentication factor
	- Limit access without the certificate
- Integrate onto smart cards
	- Use as both a physical and digital access card

