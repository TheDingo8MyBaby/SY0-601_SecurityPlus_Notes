## Plaintext / unencrypted passwords
- Some applications store passwords "in the clear"
	- No encryption. You can read the stored password.
	- This is rare, thankfully
- DO NOT STORE PASSWORDS AS PLAIN TEXT
	- Anyone with access to the password file or database has ever credential
- What to do if your application saves passwords as plaintext.
	- Get a better application

## Hashing a password
- Hashes represent data as a fixed-length string of text
	- A message digest, or "Fingerprint"
- Will not have a collision (Hopefully)
	- Different inputs will not have the same hash
- One-way trip
	- Impossible to recover the original message from the digest
	- A common way to store passwords

## A hashed example
- SHA-256
	- Used in many applications
![](Images/Pasted%20image%2020231127213420.png)
## The password file
- Different across operating systems and applications
	- Different hash algorithms
![](Images/Pasted%20image%2020231127214238.png)
## Spraying attack
- Try to login with an incorrect password
	- Eventually you're locked out
- There are some common passwords
	- https://en.wikipedia.org/wiki/List_of_the_most_commong_passwords
![](Images/Pasted%20image%2020231127214339.png)- Attack an account with the top three (or more) passwords
	- If they don't work, move to the next account
	- No lockouts, no alarms, no alerts

## Brute force
- Try every possible password combination until the a hash is matched
- This might take some time
	- A strong hasing algorithm slows things down
![](Images/Pasted%20image%2020231127214628.png)- Brute force attacks - Online
	- Keep trying the login process
	- Very slow
	- Most accounts will lockout after a number of failed attempts
- Brute force the hash - Offline
	- Obtain the list of users and hashes
	- Calculate a password hash, compare it to a stored has
	- Large computational resource requirement
![](Images/Pasted%20image%2020231127214751.png)
## Dictionary attacks
- Use a dictionary to find common words
	- Passwords are created by humans
- Many common wordlists available on the 'net
	- Some are customized by language or line of work
		- Things like a Medical Dictionary exist for hospital
- The password crackers can substitute letters
	- p&ssw0rd
- This takes time
	- Distributed cracking
	- GPU cracking is common
- Discover passwords for common words
	- This won't discover random character passwords
![[WKoKrOf.png)

## Rainbow tables
- An optimized, pre-built set of hashes
	- Saves time and storage space
	- Doesn't need to contain every hash
	- Contains pre-calculated hash chains
- Remarkable speed increase
	- Especially with longer password lengths
- Need different tables for different hashing methods
	- Windows is different than MySQL

## Adding some salt
- Salt
	- Random data added to a password when hashing
- Every user gets their own random salt
	- The salt is commonly stored with the password
		- If two users share a password, the hash will be different due to Salting
- Rainbow tables wont work with salted hashes
	- Additional random value added to the original password
- This slows things down for the brute force process
	- It doesn't completely stop the reverse engineering
		- It just slows it down

## Salting the hash
- Each user gets a different random hash
	- The same password creates a different hash
![](Images/Pasted%20image%2020231127215345.png)
## When the hashes get out
- January 2019 - Collection #1
	- A collection of email addresses and passwords
	- 12,000+ files and 87 GB of data
- 1,160,253,228 unique emails and passwords
	- A compilation of data breach results
- 772,904,991 unique usernames
	- That's about 773 Million people
- 21,222,975 unique passwords
	- You really need a password manager
- https://haveibeenpwned.com/
	- See if you've been affected by a data breach
		- Trusted and well respected.

