## Hashes
- Represent data as a short string of text
	- A message digest
		- A fingerprint
- One-way trip
	- Impossible to recover the original message from the digest
	- Used to store passwords / confidentiality
- Verify a downloaded document is the same as the original
	- Integrity
- Can be a digital signature
	- Authentication
	- Non-repudiation
	- Integrity
- Will not have a collision (hopefully)
	- Different messages will not have the same hash
## A hash example
- SHA256 hash
	- 256 bits / 64 hexadecimal characters
- My name is Professor Messer.
	- SHA256 hash:
		- `19da9a2e26f3bff67f0522f962851c42542b8659333ac53397c8d65aa7a3f871`
- My name is Professor Messer!
	- SHA256 hash:
		- `54381cae1eea10892d81c8688d06d1928b4ee8495061a792864f83092b033aea`
## Collision
- Hash functions
	- Take an input of any size
	- Create a fixed size string
	- Message digest / checksum
- The hash should be unique
	- Different inputs should never create the same hash
		- If they do, it's a collision
- MD5 has a collision problem
	- Found in 1996
	- Don't use MD5
![](Images/Pasted%20image%2020240509194705.png)## Practical hashing
- Verify a downloaded file
	- Hashes may be provided on the download site
	- Compare the downloaded file hash with the posted hash value
![](Images/Pasted%20image%2020240509194806.png)- Password storage
	- Instead of storing the password, store a salted hash
	- Compare hashes during the authentication process
	- Nobody ever knows your actual password
## Adding some salt
- Salt
	- Random data added to a password when hashing
- Every user gets their own random salt
	- The salt is commonly stored with the password
- Rainbow tables won't work with salted hashes
	- Additional random value added to the original password
- This slows things down for the brute force process
	- It doesn't completely stop the reverse engineering
## Salting the hash
- Each user gets a different random hash
	- The same password creates a different hash
![](Images/Pasted%20image%2020240509195638.png)## Digital signatures
- Prove the message was not changed
	- Integrity
- Prove the source of the message
	- Authentication
- Make sure the signature isn't fake
	- Non-repudiation
- Sign with the private key
	- The message doesn't need to be encrypted
	- Nobody else can sign this
- Verify with the public key
	- Any change in the message will invalidate the signature
## Creating a digital signature
![](Images/Pasted%20image%2020240509195914.png)## Verifying a digital signature
![](Images/Pasted%20image%2020240509200018.png)
