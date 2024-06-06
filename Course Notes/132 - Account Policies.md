- Control access to an account
	- It's more than just username and password
	- Determine what policies are best for an organization
- The authentication process
	- Password policies
	- Authentication factor policies
	- Other considerations
- Permissions after login
	- Another line of defense
## Perform routine audits
- Is everything following the policy?
	- You have to police yourself
- It's amazing how quickly things can change
	- Make sure the routine is scheduled
- Certain actions can be automatically identified
	- Consider a tool for log analysis
## Auditing
- Permission auditing
	- Does everyone have the correct permissions?
	- Some Administrators don't need to be there
	- Scheduled recertification
- Usage auditing
	- How are your resources used?
	- Are your systems and applications secure?
## Password complexity and length
- Make your password strong
	- Resist guessing or brute-force attack
- Increase password entropy
	- No single words
	- No obvious passwords
		- What's the name of your dog?
	- Mix Upper and Lower case
	- Use special characters
		- Don't replace a `o with a 0`
			- or
		- `t with a 7`
- Stronger passwords at least 8 characters
	- Consider a phrase or set of words
- Prevent password reuse
	- System remembers password history
		- Requires unique passwords
## Account lockout and disablement
- Too many incorrect passwords will cause a lockout
	- Prevents online brute force attacks
	- This should be normal for most user accounts
	- This can cause big issues for service accounts
		- You might want this
- Disabling accounts
	- Part of the normal change process
	- You don't want to delete accounts
		- At least not initially
		- May contain important decryption keys
## Location-based policies
- Network location
	- Identify based on IP subnet
	- Can be difficult with mobile devices
- Geolocation
	- Determine a user's location
		- GPS
			- Mobile Devices, Very Accurate
		- 802.11 Wireless
			- Less accurate
		- IP Address
			- Not very accurate
- Geofencing
	- Automatically allow or restrict access when the user is in a particular location
	- Don't allow this app to run unless you're near the office
## Location-based policies
- Geotagging
	- Add location metadata to a document or file
		- Latitude and longitude
		- Distance
		- Time Stamps
- Location-based access rules
	- Your IP address is associated with an IP block in Russia
		- We don't have an office in Russia
			- You were in Colorado Springs an hour ago
				- Permission NOT Granted
- Time-based access rules
	- Nobody needs to access the lab at 3AM

