## AAA framework
- Identification
	- This is who you claim to be
	- Usually your username
- Authentication
	- Prove you are who you say you are
	- Password and other authentication factors
- Authorization
	- Based on your identification and authentication, what access do you have?
- Accounting
	- Resource used:
		- Login time
		- Data sent and received
		- Logout time

## Cloud vs. on-premises authentication
- Cloud-based security
	- Third-party can manage the platform
	- Centralized platform
	- Automation options with API integration
	- May include addition options (for a cost)
- On-premises authentication system
	- Internal monitoring and management
	- Need internal expertise
	- External access must be granted and managed

## Multi-factor authentication
- Factors 
	- Something you know
	- Something you have
	- Something you are
- Attributes
	- Somewhere you are
	- Something you can do
	- Something you exhibit
	- Someone you know

## Something you know
- Password
	- Secret word/phrase
		- string of characters
	- Very common authentication factor
- PIN
	- Personal Identification Number
	- Not typically contained anywhere on a smart card or ATM card
- Pattern
	- Complete a series of patterns
	- Only you know the right format

## Something you have
- Smart card
	- Integrates with devices
		- May require a PIN
- USB token
	- Certificate is on the USB device
- Hardware or software tokens
	- Generates pseudo-random authentication codes
- Your phone
	- SMS code to your phone

## Something you are
- Biometric authentication
	- Fingerprint
	- Iris Scan
	- Voice Print
- Usually stores a mathematical representation of your biometric
	- Your actual fingerprint isn't usually saved
- Difficult to change
	- You can change your password
	- You can't change your fingerprint
- Used in very specific situations
	- Not foolproof

## Somewhere you are
- Provide a factor based on your location
	- The transaction only completes if you are in a particular geography
- IP address
	- Not perfect, but can help provide more info
	- Works with IPv4
		- Not so much with IPv6
- Mobile device location services
	- Geolocation to a very specific area
	- Must be in a location that can receive GPS information or near an identified mobile or 802.11 network
	- Still not a perfect identifier of location

## Something you can do
- A personal way of doing things
	- You're Special
- Handwriting analysis
	- Signature comparison
	- Writing technique
- Very similar to biometrics
	- Close to something you are

## Other attributes
- Something you exhibit
	- A unique trait
		- Personal to you
	- Gait Analysis
		- The way you walk
	- Typing analysis
		- The way you hit the enter key too hard
	- Someone you know
		- A social factor
		- It's not what you know
			- It's who you know
		- Web of trust
		- Digital signature

