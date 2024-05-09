## Cross-site requests
- Cross-site requests are common and legitimate
	- You visit ProfessorMesser.com
	- Your browser loads text from the ProfessorMesser.com server
	- Your browser loads a video from YouTube
	- Your browser loads pictures from Instagram
- HTML on ProfessorMesser.com directs requests form your browser
	- This is normal an expected
	- Most of these are unauthenticated requests

## The client and the server
- Website pages consist of client-side code and server-side code
	- Many moving parts
- Client side
	- Renders the page on the screen
	- HTML, JavaScript
- Server side
	- Performs requests from the client
	- HTML, PHP
		- BackEnd Processes
	- Transfer money from one account to another
	- Post a video on YouTube

## Cross-site request forgery
- One-click attack, session riding
	- XSRF, CSRF (sea surf)
- Takes advantage of the trust that a web application has for the user
	- The web site trusts your browser
	- Requests are made without your consent or your knowledge
	- Attacker posts a Facebook status on your account
- Significant web application development oversight
	- The application should have anti-forgery techniques added
	- Usually a cryptographic token to prevent a forgery

## Cross-site request forgery (Example)
![](Images/Pasted%20image%2020231202032901.png)

## Server-side request forgery (SSRF)
- Attacker finds a vulnerable web application
	- Sends requests to a web server
	- Web server performs the request on behalf of the attacker
- Caused by bad programming
	- Never trust the user input
	- Server should validate the input and the responses
	- These are rare, but can be critical vulnerabilities

## Server-side request forgery (SSRF) {Example}
![](Images/Pasted%20image%2020231202033145.png)

## Capital One SSRF breach - March 2019
- Attacker is able to execute commands on the Capital One website
	- This is normally stopped by a WAF (Web Application Firewall)
	- The WAF was misconfigured
- Attacker obtained security credentials for the WAF role
- WAF-Role account listed the buckets on Amazon S3
- Attacker retrieved the data from the Amazon buckets
- Credit card application data form 2005 through 2019
	- 106 million names, address, phone, email, DoB
	- 140,000 Social Security numbers, 80,00 bank account numbers

