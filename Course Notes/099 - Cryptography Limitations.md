## Finding balance
- Cryptography isn't a perfect solution
	- It can have significant limitations
- Not all implementations are the same
	- Different platforms
	- Different cryptographic options
- Cryptography can't fix bad technique
	- Hashing easily guessed passwords without a salt
- Every situation is different
	- Do your homework
## Limitation
- Speed
	- Cryptography adds overhead
	- A system needs CPU
		- CPU Needs power
	- More involved encryption increases the load
- Size
	- Typical block ciphers don't increase the size of encrypted data
	- AES block size is 128 bits/16 bytes
	- Encrypting 8 bytes would potentially double the storage size
## 