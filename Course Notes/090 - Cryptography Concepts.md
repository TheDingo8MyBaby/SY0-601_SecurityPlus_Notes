## Cryptography
- Greek: "Kryptos"
	- Hidden
	- Secret
- Confidentiality
	- It's a secret
- Authentication and access control
	- I know it's you
- Non-repudiation
	- You said it.  You can't deny it
## Cryptography terms
- Plaintext
	- An unencrypted message (in the clear)
- Ciphertext
	- An encrypted message
- Cipher
	- The algorithm used to encrypt and/or decrypt
- Cryptanalysis
	- The art of cracking encryption
	- Researchers are constantly trying to find weaknesses in ciphers
		- A mathematically flawed cipher is bad for everyone
## Cryptographic Keys
- Keys
	- Add the key to the cypher to encrypt
	- Larger keys are generally more secure
- Some encryption methods use one key
	- Some use more than one key
	- Every method is a bit different
## Give weak keys a workout
- A weak key is a weak key
	- By itself, it's not very secure
- Make a weak key stronger by performing multiple processes
	- Hash a password
		- Hash the hash of the password
	- Key stretching
		- Key strengthening
- Brute force attacks would require reversing each of those hashes
	- The attacker has to spend much more time
		- Even though the key is small
## Key stretching libraries
- Already built for your application
	- No additional programming involved
- bcrypt
	- Generates hashes from passwords
	- An extension to the UNIX crypt library
	- Uses Blowfish cipher to perform multiple rounds of hashing
- Password-Based Key Derivation Function 2 (PBKDF2)
	- Part of RSA public key cryptography standards
		- PKCS #5, RFC 2898
## Lightweight cryptography
- Powerful cryptography has traditionally required strength
	- A powerful CPU and lots of time
- Internet of Things (IoT) devices have limited power
	- Both watts and CPU
- New standards are being created
	- National Institute of Standards and Technology (NIST) leading the effort
	- Provide powerful encryption
	- Include integrity features
	- Keep costs low
## Homomorphic encryption (HE)
- Encrypted data is difficult to work with
	- Decrypt the data
	- Perform a function
	- Encrypt the answer
- Homomorphic encryption
	- Perform calculations of data while it's encrypted
	- Perform the work directly on the encrypted data
	- The decrypted data can only be viewed with the private key
- Many advantages
	- Securely store data in the cloud
	- Perform research on data without viewing the data

