## On-path Network attack
- How can an attacker watch without you knowing
	- Formerly known as a man-in-the-middle
- Redirects your traffic
	- Then passes it on to the destination
	- You never know your traffic was redirected
- ARP poisoning (Address Resolution Protocol)
	- On-path attack on the local IP subnet
	- ARP has no security

## ARP poisoning (spoofing)
![](Images/Pasted%20image%2020231204223848.png)
![](Images/Pasted%20image%2020231204224027.png)

## On-path browser attack
- What if the middleman was on the same computer as the victim?
	- Malware/Trojan does all of the proxy work
	- Formerly known as man-in-the-browser
- Huge advantages for the attackers
	- Relatively easy to proxy encrypted traffic
	- Everything looks normal to the victim
- The malware in your browser waits for you to login to your bank
	- And then cleans you out

