- You've encrypted data and sent it to another person
	- Is it really secure?
	- How do you know?
- The bad guy doesn't have the combination (the key)
	- So they break the safe (the cryptography)
- Finding ways to undo the security
	- There are many potential cryptographic shortcomings
	- The problem is often the implementation

## Birthday attack
- In a classroom of 23 students, what is the chance of two students sharing a birthday?
	- About 50%
		- For a class of 30, the chance is about 70%
- In the digital world, this is a hash collision
	- A hash collision is the same has value for two different plaintexts
	- Find a collision through brute force
- The attacker will generate multiple versions of plaintext to match the hashes
	- Protect yourself with a large hash output size

## Collisions
- Hash digests are supposed to be unique
	- Different input data should never create the same hash
- MD5 hash
	- Message Digest Algorithm 5
		- First published in April 1992
		- Collisions identified in 1996
- December 2008: Researchers created CA certificate that appeared legitimate when MD5 is checked
	- Built other certificates that appeared to be legit and issued by RapidSSL
![](Images/Pasted%20image%2020231127223108.png)
![](Images/Pasted%20image%2020231127223218.png)
## Downgrade attack
- Instead of using perfectly good encryption, use something that's not so great
	- Force the systems to downgrade their security
- 2014 - TLS vulnerability
	- POODLE (Padding Oracle On Downgraded Legacy Encryption)
		- On-path attack
		- Forces clients to fallback to SSL 3.0
			- SSL 3.0 has significant cryptographic vulnerabilities
	- Because of POODLE, modern browsers won't fallback to SSL 3.0

