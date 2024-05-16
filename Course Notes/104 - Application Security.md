## Secure coding concepts
- A balance between time and quality
	- Programming with security in mind is often secondary
- Testing, testing, testing
	- The Quality Assurance (QA) process
- Vulnerabilities will eventually be found
	- And exploited
## Input validation
- What is the expected input?
	- Validate actual vs. expected
- Document all input methods
	- Forms
	- Fields
	- File Type
- Check and correct all input (normalization)
	- A zip code should be only `X` characters long with a letter in the `X` column
	- Fix any data with improper input
- The fuzzers will find what you missed
	- Don't give them an opening
## Dynamic analysis (fuzzing)
- Send random input to an application
	- Fault-injecting
	- Robustness testing
	- Syntax testing
	- Negative testing
- Looking for something out of the ordinary
	- Application crash
	- Server error
	- Exception
- 1988 Class Project at the University of Wisconsin
	- `Operating System utility Program Reliability`
		- Professor Barton Miller
	- The Fuzz Generator
## Fuzzing engines and frameworks
- Many different fuzzing options
	- Platform specific
	- Language specific
	- Etc...
- Very time and processor resource heavy
	- Many, many different iterations to try
	- Many fuzzing engines use high-probability tests
- Carnegie Mellon Computer Emergency Response Team (CER)
	- CERT Basic Fuzzing Framework (BFF)
		- https://professormesser.link/bff
## Secure cookies
- Cookies
	- Information stored on your computer by the browser
- Used for tracking, personalization, session management
	- Not executable
	- Not generally a security risk
		- Unless someone gets access to them
- Secure cookies have a Secure attribute set
	- Browser will only send it over HTTPS
- Sensitive information should not be saved in a cookie
	- This isn't designed to be secure storage
## HTTP Secure Headers
- An additional layer of security
	- Add these to the web server configuration
	- You can't fix every bad application
- Enforce HTTPS communication
	- Ensure encrypted communication
- Only allow:
		- Scripts
		- Stylesheets
		- Images
	- Prevent XSS attacks
- Prevent data from loading into an inline frame (iframe)
	- Also helps to prevent XSS attacks
## Code signing
- An application is deployed
	- Users run application executable or scripts
- So many security questions
	- Has the application been modified in any way?
	- Can you confirm that the application was written by a specific developer?
- The application code can be digitally signed by the developer
	- Asymmetric encryption
	- A trusted CA signs the developer's public key
	- Developers sign the code with their private key
	- For internal apps, use your own CA
## Allow list / Deny list
- Any application can be dangerous
	- Vulnerabilities
	- Trojan horses
	- Malware
- Security policy can control app execution
	- Allow list
	- Deny/Block list
- Allow list
	- Nothing runs unless it's approved
	- Very restrictive
- Deny list
	- Nothing on the "bad list" can be executed
		- Anti-virus
		- Anti-malware
## Examples of allow and deny lists
- Decisions are made in the operating system
	- Often built-in  to the operating system management
- Application hash
	- Only allows applications with this unique identifier
- Certificate
	- Allow digitally signed apps from certain publishers
- Path
	- Only run applications in these folders
- Network zone
	- The apps can only run from this network zone
## Static code analyzers
- Static Application Security Testing (SAST)
	- Help to identify security flaws
- Many security vulnerabilities found easily
	- Buffer overflows
	- Database injections
	- Etc...
- Not everything can be identified through analysis
		- Authentication security
		- Insecure cryptography
		- Etc...
	- Don't reply on automation for everything
- Still have to verify each finding
	- False positives are an issue
## Static code analyzer output

![](../Images/240515-1%201.png)

