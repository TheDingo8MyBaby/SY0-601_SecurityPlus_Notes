- Useful information is transmitted over the network
	- A crafty hacker will take advantage of this
- Need access to the raw network data
	- Network tap, ARP poisoning, Malware on the victim computer
- The gathered information may help the attacker
	- Replay the data to appear as someone else
- This is not an on-path attack
	- The actual replay doesn't require the original workstation

## Pass the hash
![](Images/Pasted%20image%2020231202031448.png)![](Images/Pasted%20image%2020231202031459.png)- Avoid this type of replay attack with a salt or encryption
	- Use a session ID with the password hash to create a unique authentication hash each time

## Browser cookies and session IDs
- Cookies
	- Information stored on your computer by the browser
- Used for tracking, personalization, session management
	- Not executable, not generally a security risk
		- Unless someone gets access to them
- Could be considered a privacy risk
	- Lots of personal data in there
- Session IDs are often stored in the cookie
	- Maintains sessions across multiple browser sessions

## Session hijacking (Sidejacking)
![](Images/Pasted%20image%2020231202031803.png)- This is why SSL / TLS is important

## Header manipulation
- Information gathering
	- Wireshark, Kismet
- Exploits
	- Cross-site scripting
		- Use the server to send the session ID to the attacker
- Modify headers
	- Tamper, Firesheep, Scapy
- Modify cookies
	- Cookies Manager+ (Firefox add-on)

## Prevent session hijacking
- Encrypt end-to-end
	- They can't capture your session ID if they can't see it
	- Additional load on the web server (HTTPS)
	- Firefox extension: HTTPS Everywhere, Force-TLS
	- Many sites are now HTTPS-only
- Encrypt end-to-somewhere
	- At least avoid capture over a local wireless network
	- Still in-the-clear for part of the journey
	- Personal VPN (OpenVPN, VyprVPN, etc...)
