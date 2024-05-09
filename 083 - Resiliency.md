## Non-persistence
- The cloud is always in motion
	- Application instances are constantly built and torn down
- Snapshots can capture the current configuration and data
	- Preserve the complete state of a device, or just the configuration
- Revert to known state
	- Fall back to a previous snapshot
- Rollback to known configuration
	- Don't modify the data, but use a previous configuration
- Live boot media
	- Run the operating system from removable media
		- Very portable
## High availability
- Redundancy doesn't always mean always available
	- May need to be powered on manually
- HA (High availability)
	- Always on
	- Always available
- May include many different components working together
	- Active/Active can provide scalability advantages
- Higher availability almost always means higher costs
	- There's always another contingency you could add
		- Upgraded power
		- High-quality server components
		- Etc...
## Order of restoration
- Application-specific
	- Certain components may need to be restored first
	- Databases should be restored before the application
- Backup-specific
	- Incremental backups restore the full backup, then all subsequent incremental backups
	- Differential backups restore the full backup, then the last differential backup
## Diversity
- Technologies
	- A zero-day OS vulnerability can cause significant outages
	- Multiple security devices
- Vendors
	- A single vendor can become a disadvantage
	- No options during annual renewals
	- A bad support team may not be able to resolve problems in a timely manner
- Cryptographic
	- All cryptography is temporary
	- Diverse certificate authorities can provide additional protection
- Controls
	- Administrative controls
	- Physical controls
	- Technical controls
	- Combine them together
	- Defense in depth

