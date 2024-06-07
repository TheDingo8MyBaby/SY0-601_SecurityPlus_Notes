## Wireless authentication
- We've created many authentication methods through the years
	- A network administrator has many choices
- Use a username and password
	- Other factors can be included
- Commonly used on wireless networks
	- Also works on wired networks
## EAP
- Extensible Authentication Protocol (EAP)
	- An authentication framework
- Many different ways to authenticate base on RFC standards
	- Manufacturers can build their own EAP methods
- EAP integrates with `802.1X`
	- Prevents access to the network until the authentication succeeds
## IEEE 802.1X
- Port-based Network Access Control (NAC)
	- You don't get access to the network until you authenticate
- Used in Conjunction with an access database
	- RADIUS
	- LDAP
	- TACACS+
## IEEE 802.1X and EAP
- Supplicant
	- The client
- Authenticator
	- The device that provides access
- Authentication server
	- Validates the client credentials
## EAP-FAST
- EAP Flexible Authentication vs Secure Tunneling
	- Authentication Server (AS) and Supplicant share a Protected Access Credential (PAC)
		- (Shared Secret)
- Supplicant receives the PAC
- Supplicant and AS mutually authenticate and negotiate a Transport Layer Security (TLS) Tunnel
- User authentication occurs over the TLS tunnel
- Need a RADIUS Server
	- Provides the authentication database and EAP-FAST services
## PEAP
- Protected Extensible Authentication Protocol
	- Protected EAP
	- Created by Cisco, Microsoft, and RSA Security
- Also encapsulates EAP in a TLS tunnel
	- AS uses a digital certificate instead of a PAC
	- Client doesn't use a certificate
- User authenticates with `MS-CHAPv2`
	- Authenticates to Microsoft's `MS-CHAPv2` databases
- User can also authenticate with a GTC
	- Generic Token Card
	- Hardware Token Generator
## EAP-TLS
- EAP Transport Layer Security
	- Strong security & wide adoption
	- Support from most of the industry
- Requires digital certificates on the AS and all other devices
	- AS and supplicant exchange certificates for mutual authentication
	- TLS Tunnel is then built for the user authentication process
- Relatively complex implementation
	- Need a Public Key Infrastructure (PKI)
	- Must deploy and manage certificates to all wireless clients
	- Not all devices can support the use of digital certificates
## EAP-TTLS
- EAP Tunneled Transport Layer Security
	- Support other authentication protocols in a TLS Tunnel
- Requires a digital certificate on the AS
	- Does not require digital certificate on every device
	- Builds a TLS Tunnel using this digital certificate
- Use any authentication method inside the TLS Tunnel
	- Other EAPs
	- `MSCHAPv2`
	- Anything else
## RADIUS Federation
- Use RADIUS with federation
	- Members of one organization can authenticate to the network of another organization
	- Use their normal credentials
- Use 802.1X as the authentication method
	- Rand RADIUS on the backend
	- EAP to authenticate
- Driven by EduRoam (Education Roaming)
	- Educators can use their normal authentication when visiting a different campus
		- https://www.eduroam.org/

