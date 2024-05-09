## Directory services
- Keep all of an organization's usernames and passwords in a single database
	- Computers
	- Printers
	- Other Devices...
- Large distributed database
	- Constantly replicated
- All authentication requests reference this directory
	- Each user only needs one set of credentials
		- One username
		- One password
- Access via Kerberos or LDAP

## Federation
- Provide network access to others
	- Not just employees
		- Partners
		- Suppliesrs
		- Customers
		- Etc...
- Third-parties can establish a federated network
	- Authenticate and authorize between the two organizations
		- Login with your Facebook credentials
- The third-parties must establish a trust relationship
	- And the degree of the trust

## Attestation
- Prove the hardware is really yours
	- A system you can trust
- Easy when it's just your computer
	- More difficult when there are 1,000
- Remote attestation
	- Device provides an operational report to a verification server
	- Encrypted and digitally signed with the TPM
	- An IMEI or other unique hardware component can be included in the report

## Short message service (SMS)
- Text messaging
	- Includes more than text these days
- Login factor can be sent via SMS to a predefined phone number
	- Provide username and password
	- Phone receives an SMS
		- Input the SMS code into the login form
- Security issues exist
	- Phone number can be reassigned to a different phone
	- SMS messages can be intercepted

## Push notification
- Similar process to an SMS notification
	- Authentication factor is pushed to a specialized app
		- Usually on a mobile device
- Security challenges
	- Applications can be vulnerable
	- Some push apps send in the clear
- Still more secure than SMS
	- Multiple factors are better than one factor

## Authentication apps
- Pseudo-random token generators
	- A useful authentication factor
- Carry around a physical hardware token generator
	- Where are my keys again?
- Use software-based token generator on your phone
	- Powerful and convenient

## TOTP
- Time-based One-Time Password algorithm
	- Use a secret key and the time of day
	- No incremental counter
- Secret key is configured ahead of time
	- Timestamps are synchronized via NTP
- Timestamp usually increments every 30 seconds
	- Put in your username, password, and TOTP code
- One of the more common OTP methods
	- Google
	- Facebook
	- Microsoft
	- Etc...

## HOTP
- One-time passwords
	- Use them once, and never again
		- Once a session
		- Once each authentication attempt
- HMAC-based One-Time Password algorithm
	- Keyed-hash message authentication code (HMAC)
	- The keys are based on a secret key and a counter
- Token-based authentication
	- The hash is different every time
- Hardware and software tokens available
	- You'll need additional technology to make this work

## Phone call
- A voice call provides the token
	- The computer is talking to you
		- "Your code is: 1-6-2-5-1-7"
- Similar disadvantages to SMS
	- Phone call can be intercepted or forwarded
	- Phone number can be added to another phone

## Static codes
- Authentication factors that don't change
	- You just have to remember
- Personal Identifcation Number (PIN)
	- Your secret numbers
- Can also be alphanumerical
	- A password or passphrase

## Smart cards
- Integrated circuit card
	- Contact or contactless
- Common on credit cards
	- Also used for access control
- Must have physical card to provide digital access
	- A digital certificate
- Multiple factors
	- Use the card with a PIN or fingerprint

