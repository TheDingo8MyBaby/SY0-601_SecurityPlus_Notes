## Development to production
- Your programming team has been working on a new application
	- How will you deploy it safely and reliably?
- Patch Tuesday
	- Test and Deploy
		- Wednesday?
		- Thursday?
		- Friday?
- Manage the process
	- Safely move from a non-production phase to full production

## Sandboxing
- Isolated testing environment
	- No connection to the real world or production system
	- A technological safe space
- Use during the development process
	- Try some code
	- Break some code
		- Nobody gets hurt
- Incremental development
	- Helps build the application

## Building the application
- Development
	- Secure environment
	- Writing code
	- Developers test in their sandboxes
- Test
	- Still in the development stage
	- All of the pieces are put together
		- Does it work?
	- Functional Tests

## Verifying the application
- Quality Assurance (QA)
	- Verifies features are working as expected
	- Validates new functionality
	- Verifies old errors don't reappear
- Staging
	- Almost ready to roll it out
	- Works and feels exactly like the production environment
	- Working with a copy of production data
	- Run performance tests
	- Test usability and features

## Using the application
- Production
	- Applicatio is live
	- Rolled out to the user community
- A challenging step
	- Impacts the users
- Logistical Challengeds
	- New servers
	- New software
	- Restart or interrupt of service

## Secure baselines
- The security of an application environment should be well defined
	- All application instances must follow this baseline
		- Firewall settings
		- Patch levels
		- OS file versions
	- May require constant updates
- Integrity measurements check for the secure baseline
	- These should be performed often
	- Check against well-documented baselines
	- Failure requires an immediate correction

