- What if your network was really secure?
	- You didn't even plug in that USB key from the parking lot
- The bad guys can't get in
	- Not responding to phising emails
	- Not opening any email attachments
- Have the mountain come to you
	- Go where the mountain hangs out
	- The watering hole
	- This requires a bit of research

## Executing the watering hole attack
- Determine which website the victim group uses
	- Educated guess - Local coffee or sandwich shop
	- Industry-related sites
- Infect one of these third-party sites
	- Site vulnerability
	- Email attachments
- Infect all visitors
	- But you're just looking for specific victims

## Because that's where the money is
- January 2017
- Polish Financial Supervision Authority, National Banking and Stock Commission of Mexico, State-Owned bank in uruguay
	- The watering hole was sufficiently poisoned
- Vising the site would download malicious JavaScript files
	- But only to IP addresses matching banks and other financial institutions
- Did the attack work?
	- We still don't know

## Watching the watering hole
- Defense-in-depth
	- Layered defense
	- It's never one thing
- Firewalls and IPS
	- Stop the network traffic before things get bad
- Anti-Virus / Anti-malware signature updates
	- The Polish Financial Supervision Authority attack code was recognized and stopped by generic signature in Symantec's Anti Virus
