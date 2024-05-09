## Code Injection
- Code Injection
	- Adding your own information into a data stream
- Enabled because of bad programming
	- The application should properly handle input and output
- So many different data types
	- HTML, SQL, XML, LDAP, etc...

## SQL Injection
- SQL - Structured Query Language
	- The most common relational database management system language
- SQL Injection
	- Modifying SQLL requests
	- Your application shouldn't really allow this

## WebGoat - SQL Injection
![](Images/Pasted%20image%2020231202030357.png)
- The field doesn't validate information within the Input Box
![](Images/Pasted%20image%2020231202030448.png)
- `' OR '1'='1` Is a very common SQL Injection
	- 3SL99A' OR '1'=1
		- Means that if number or 1=1 is true, then show

## XML injection and LDAP injection
- XML - Extensible Markup Language
	- A set of rules for data transfer and storage
- XML injection
	- Modifying XML requests - a good application will validate
- LDAP - Lightweight Directory Access Protocol
	- Created by the telephone companies
	- Now used by almost everyone
- LDAP injection
	- Modifying LDAP requests to manipulate application results

## DLL injection
- Dynamic-Link Library
	- A Windows library containing code and data
	- Many applications can use this library
- Inject a DLL and have an application run a program
	- Runs as part of the target process

