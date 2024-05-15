## Finding the balance
- Low power devices
	- Mobile devices, portable systems
	- Smaller symmetric key sizes
	- Use elliptic curve cryptography (ECC) for asymmetric encryption
- Low latency
	- Fast computation time
	- Symmetric encryption, smaller key sizes
- High resiliency
	- Larger key sizes
	- Encryption algorithm quality
	- Hashing provides data integrity
## Use cases
- Confidentiality
	- Secrecy and privacy
	- Encryption
		- File-Level
		- Drive-Level
		- Email
		- Etc...
- Integrity
	- Prevent modification of data
	- Validate the contents with hashes
		- File downloads
		- Password storage
- Obfuscation
	- Modern malware
	- Encrypted data hides the active malware code
	- Decryption occurs during execution
## Use cases
- Authentication
	- Password hashing
	- Protect the original password
	- Add salt to randomize the stored password hash
- Non-Repudiation
	- Confirm the authenticity of data
	- Digital signature provides both integrity and non-repudiation

