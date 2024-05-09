- Pentest
	- Simulate an attack
- Similar to vulnerability scanning
	- Except we actually try to exploit the vulnerabilities
- Often a compliance mandate
	- Regular penetration testing by a 3rd-party
- National Institute of Standards and Technology Technical Guide to Information Security Testing and Assessment
	- https://professormesser.link/800115 (PDF)

## Rules of Engagement
- An important document
	- Defines purpose and scope
	- Makes everyone aware of the test parameters
- Type of testing and schedule
	- On-site physical breach
	- Internal Test
	- External Test
		- Could be during Normal working hours
		- Could be after 6pm Only
		- Etc...
- The rules
	- IP address ranges
	- Emergency contacts
	- How to handle sensitive information
	- In-Scope and Out-Of-Scope devices or applications

## Working knowledge
- How much do you know about the test?
	- Many different approaches
- Unknown environment
	- The Pentester knows nothing about the systems under attack
		- "Blind" Test
- Known environment
	- Full Disclosure
- Partially known envioronment
	- A mix of known and unknown
	- Focus on certain systems or applications

## Exploiting vulnerabilities
- Try to break into the system
	- BE CAREFUL;
		- This can cause a denial of service or loss of data
	- Buffer Overflows can cause instability
	- Gain privilege escalation
- You may need to try many different vulnerability types
	- Password brute-force
	- Social engineering
	- Database injections
	- Buffer overflows
- You'll only be sure you're vulnerable if you can bypass security
	- If you can get through, the attackers can get through

## The process
- Initial exploitation
	- Get into the network
- Lateral movement
	- Move from system to system
	- The inside of the network is relatively unprotected
- Persistence
	- Once you're there, you need to make sure there's a way back in
		- Set up a backdoor
		- Build user accounts
		- Change or Verify default passwords
- The pivot
	- Gain access to systems that would normally not be accessible
	- Use a vulnerable system as a proxy or relay

## Pentest Aftermath
- Cleanup
	- Leave the network in its original state
	- Remove any binaries or temporary files
	- Remove any backdoors
	- Delete user accounts created during the test
- Bug Bounty
	- A reward for discovering vulnerabilities
		- Earn money for hacking a system
	- Document the vulnerability to earn cash

