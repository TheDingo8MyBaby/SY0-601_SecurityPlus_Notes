- XSS (Cross-site scripting)
	- Cascading Style Sheets (CSS)
		- This is something else entirely
- Originally called cross-site because of browser security flaws
	- Information from one site could be shared with another
- One of the most common web application development errors
	- Takes advantage of the trust a user has for a site
	- Complex and varied
- Malware that uses JavaScript
	- Do you allow scripts?

## Non-persistent (reflected) XSS attack
- Web site allows scripts to run in user input
	- Search box is a common source
- Attacker emails a link that takes advantage of this vulnerability
	- Runs a script that sends credentials/session IDs/cookies to the attacker
- Script embedded in URL executes in the victim's browser
	- As if it came from the server
- Attacker uses credentials/session IDs/cookies to steal victim's information without their knowledge
	- Very sneaky

## WebGoat
![](Images/Pasted%20image%2020231202025243.png)
- You would put a JavaScript at the end of the Credit Card Number field, to create a fake dialog box / alert
![](Images/Pasted%20image%2020231202025350.png)
	- The Script will show Session Information / Cookie data / Etc...
![](Images/Pasted%20image%2020231202025452.png)
- The data is then sent to to attacker

## Persistent (stored) XSS attack
- Attacker posts a message to a social network
	- Includes the malicious payload
- It's now "persistent"
	- Everyone gets the payload
- No specific target
	- All viewers to the page
- For social networking, this can spread quickly
	- Everyone who views the message can have it posted to their page
		- Where someone else can view it and propagate it further...

## Hacking a Subaru
- June 2017, Aaron Guzman
	- Security researcher
- When authenticating with Subaru, users get a token
	- This token never expires (This is BAD)
- A valid token allowed any service request
	- Even adding your email address to someone else's account
		- Now you have full access to someone else's car
- Web front-end included an XSS vulnerability
	- A user clicks a malicious link, and you have their token

## Protecting against XSS
- Be careful when clicking untrusted links
	- Never blindly click in your email inbox. Never
- Consider disabling JavaScript
	- Or control with an extension
	- This offers limited protection
- Keep your browser and applications updated
	- Avoid the nasty browser vulnerabilities
- Validate input
	- Don't allow users to add their own scripts to an input field

