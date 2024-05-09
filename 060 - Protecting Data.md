- A primary job task
	- An organization is out of business without data
- Data is everywhere
	- On a storage drive
	- On the network
	- In a CPU
- Protecting the data
	- Encryption
	- Security Policies
- Data permissions
	- Not everyone has the same access

## Data Sovereignty
- Data that resides in a country is subject to the laws of that country
	- Legal Monitoring
	- Court Orders
	- Etc...
- Laws may prohibit where data is stored
	- GDPR (General Data Protection Regulation)
		- Data collected on EU citizens must be stored in the EU
	- A complex mesh of technology and legalities
- Where is your data stored?
	- Your compliance laws may prohibit moving data out of the country

## Data Masking
- Data Obfuscation
	- Hide some of the original data
		- Only showing last 4 digits of the credit card
- Protects PII
	- And other sensitive data
- May only be hidden from view
	- The data may still be intact in storage
	- Control the view based on permissions
- Many different techniques
	- Substituting
	- Shuffling
	- Encrypting
	- Masking Out
	- Etc...

## Data Encryption
- Encode information into unreadable data
	- Original information is plaintext
		- Encrypted form is ciphertext
- This is a two-way street
	- Convert between one and the other
	- If you have the proper key
- Confusion
	- The encrypted data is drastically different than the plaintext

![](Images/Pasted%20image%2020240320205716.png)

## Diffusion
- Change one character of the input, and may characters change of the output

![](Images/Pasted%20image%2020240320205859.png)

## Data at-rest
- The data is on a storage device
	- Hard drive
	- SSD
	- Flash Drive
	- Etc...
- Encrypt the data
	- Whole disk encryption
	- Database encryption
	- File-or Folder-Level Encryption
- Apply permissions
	- Access control lists
	- Only authorized users can access the data

## Data in-transit
- Data transmitted over the network
	- Also called data in-motion
- Not much protection as it travels
	- Switches
	- Routers
	- Devices
- Network-based protection
	- Firewall
	- IPS
- Provide transport encryption
	- TLS (Transport Layer Security)
	- IPsec (Internet Protocol Security)

## Data in-use
- Data is actively processing in memory
	- System RAM
	- CPU registers and cache
- The data is almost always decrypted
	- Otherwise, you couldn't do anything with it
- The attackers can pick the decrypted information out of RAM
	- A very attractive option
- Target Corp. Breach  -  November 2013
	- 110 Million Credit Cards
	- Data in-transit encryption and data at-rest encryption
		- Attackers picked the credit card numbers out of the Point-Of-Sale RAM

## Tokenization
- Replace sensitive data with a non-sensitive placeholder
	- SSN: 266-12-1112
		- Becomes: 691-61-8539
- Common with credit card processing
	- Use a temporary token during payment
	- An attacker capturing the card number can't use them later
- This IS NOT encryption or Hashing
	- The original data and token aren't mathematically related
	- No encryption overhead

![](Images/Pasted%20image%2020240320211145.png)

## Information Rights Management (IRM)
- Control how data is used
	- Microsoft Office Documents
	- Email Messages
	- PDFS
- Restrict data access to unauthorize persons
	- Prevent copy and paste
	- Control screenshots
	- Manage printing
	- Restrict editing
- Each user has thier own set of rights
	- Attackers have limited options

