## SSL stripping / HTTP downgrade
- Combine an on-path attack with a downgrade attack
	- Difficult to implement, but big returns for the attacker
- Attacker must sit in the middle of the conversation
	- Must modify data between the victim and web server
	- Proxy server, ARP spoofing, rogue Wi-Fi hotspot, Etc...
- Victim does not see any significant problem
	- Except the browser page isn't encrypted
	- Strips the S away from HTTPS
- This is a client and server problem
	- Works on SSL and TLS

## SSL and TLS
![](Images/Pasted%20image%2020231202035818.png)- SSL (Secure Sockets Layer) 2.0
	- Deprecated in 2011
- SSL 3.0
	- Vulnerable to the PODDLE attack
	- Deprecated in June 2015
- Transport Layer Security (TLS) 1.0
	- Upgrade to SSL 3.0, and a name change from SSL to TLS
	- Can downgrade to SSL 3.0
- TLS 1.1
	- Deprecated in January 2020 by modern browsers
- TLS 1.2 and TLS 1.3
	- The latest standars

## SSL stripping
![](Images/Pasted%20image%2020231202040027.png)![](Images/Pasted%20image%2020231202040237.png)