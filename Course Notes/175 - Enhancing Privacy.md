## Tokenization
- Replace sensitive data with a non-sensitive placeholder
	- SSN: 266-12-1112
		- Token: 691-61-8539
- Common with credit card processing
	- Use a temporary token during payment
	- An attacker capturing the card numbers, can't use them later
- This isn't encryption or hasing
	- The original data and token aren't mathematically related
	- No encryption overhead
![](SY0-601_SecurityPlus_Notes/Images/240606-1%2020.png)
## Data minimization
- Minimal data collection
	- Only collect and retain necessary data
- Included in many regulations
	- HIPAA has a "Minimum Necessary" rule
	- GDPR: "Personal data shall be adequate, relevant and not excessive in relation to the purpose or purposes for which they are processed."
- Some information may not be required
	- Do you need a telephone number or address?
- Internal data use should be limited
	- Only access data required for the task
## Data masking
- Data obfuscation
	- Hid some of the original data
- Protects PII
	- And other sensitive data
- May only be hidden from view
	- The data may still be intact in storage
	- Control the view based on permissions
![](../Images/240606-1%2021.png)
- Many different techniques
	- Substituting
	- Shuffling
	- Encrypting
	- Masking Out
	- Etc...
## Anonymization
- Make it impossible to identify individual data from a dataset
	- Allows for data use without privacy concerns
- Many different anonymization techniques
	- Hashing
	- Masking
	- Etc...
- Convert from detailed customer purchase date
	- Remove;
		- Name
		- Address
		- Change Phone number to
			- ###-###-####
	- Keep;
		- Product name
		- Quantity
		- Total
		- Sale date
- Anonymization cannot be reversed
	- No way to associate the date to a user
## Pseudo-anonymization
- Pseudonymization
	- Replace personal information with pseudonyms
	- Often used to maintain statistical relationships
- May be reversible
	- Hide the personal data for daily use;
		- In case of breach
	- Convert it back for other processes
- Random replacement
	- James Messer
		- Jack O'Neill
			- Sam Carter
				- Daniel Jackson
- Consistent replacements
	- James Messer is always converted to `George Hammond`

