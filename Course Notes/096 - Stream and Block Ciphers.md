## Stream ciphers
- Encryption is done one bit or byte at a time
	- High speed, low hardware complexity
- Used with symmetric encryption
	- Not commonly used with asymmetric encryption
- The starting state should never be the same twice
	- Key is often combined with an initialization vector (IV)
## Block ciphers
- Encrypt fixed-length groups
	- Often 64-bit or 128-bit blocks
	- Pad added to short blocks
	- Each block is encrypted or decrypted independently
- Symmetric encryption
	- Similar to stream ciphers
- Block cipher modes of operation
	- Avoid patterns in the encryption
	- Many different modes to choose from
## Block cipher mode of operation
- Encrypt one fixed-length group of bits at a time
	- A block
- Mode of operation
	- Defines the method of encryption
	- Many provide a method of authentication
- The block size is a fixed size
	- Not all data matches the block size perfectly
	- Split your plaintext into smaller blocks
	- Some modes require padding before encrypting
## ECB (Electronic Codebook)
- The simplest encryption mode
	- Too simple for most use cases
- Each block is encrypted with the same key
	- Identical plaintext blocks create identical ciphertext blocks
## CBC (Cipher Block Chaining)
- A popular mode of operation
	- Relatively easy to implement
- Each plaintext block is XORed (Exclusive/Or) with the previous ciphertext block
	- Adds additional randomization
	- Use an initialization vector for the first block
![](../Images/240514-1%203.png)
![](../Images/240514-1%204.png)
## CTR (Counter)
- Block cipher mode / acts like a stream cipher
	- Encrypts successive values of a "Counter"
- Plaintext can be any size, since it's par of the XOR
	- IE:)  8 Bits at a time (Streaming) instead of a 128-bit block
![](../Images/240514-2%201.png)
## GCM (Galois/Counter Mode)
- Encryption with authentication
	- Authentication is part of the block mode
	- Combines Counter Mode with Galois authentication
- Minimum latency, minimum operation overhead
	- Very efficient encryption and authentication
- Commonly used in packetized data
	- Network traffic security (Wireless, IPsec)
		- SSH
		- TLS

