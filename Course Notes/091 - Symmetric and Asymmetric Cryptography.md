## Symmetric encryption
- A single, shared key
	- Encrypt with the key
	- Decrypt with the same key
	- If it gets out, you'll need another key
- Secret key algorithm
	- A shared secret
- Doesn't scale very well
	- Can be challenging to distribute
- Very fast to use
	- Less overhead than asymmetric encryption
	- Often combined asymmetric encryption
## Asymmetric encryption
- Public key cryptography
	- Two (or more) mathematically related keys
- Private key
	- Keep this private
- Public Key
	- Anyone can see this key
		- Give it away
- The private key is the only key that can decrypt data encrypted with the public key
	- You can't derive the private key from the public key
## The key pair
- Asymmetric encryption
	- Public Key Cryptography
- Key generation
	- Build both the public and private key at the same time
	- Lots of randomization
	- Large prime numbers
	- Lots and lots of math
- Everyone can have the public key
	- Only Alice has the private key
## Asymmetric encryption
![[../Images/240509-6.png]]
## Symmetric key from asymmetric keys
- Use public and private key cryptography to create a symmetric key
	- Math is powerful
![[../Images/240509-7.png]]
## Elliptic curve cryptography (ECC)
- Asymmetric encryption
	- Need large integers composed of two or more large prime factors
- Instead of numbers, use curves!
	- Uses smaller keys than non-ECC asymmetric encryption
	- Smaller storage and transmission requirements
	- Perfect for mobile devices

