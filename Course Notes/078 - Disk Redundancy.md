## Redundancy
- Duplicate parts of the system
	- If a part fails, the redundant part can be used
- Maintain uptime
	- The organization continues to function
- No hardware failure
	- Servers keep running
- No software failure
	- Services always available
- No system failure
	- Network performing optimally

## Geographic dispersal
- Bad things can happen in a local area
	- Hurricanes
	- Tornadoes
	- Flooding
- Disperse technologies to different geographies
	- Use multiple data centers
	- In different locations
- Data centers might be part of the normal operations
	- East Cost & West Coast operations centers
- May be part of a disaster recovery center
	- If Florida gets hit, fire up the Denver data center

## Disk redundancy
- Multipath I/O (Input/Output)
	- Especially useful for network-based storage subsystems
	- Multiple Fiber Channel interfaces with multiple switches
- RAID
	- Redundant Array of Independent Disks
- Multiple drives create redundancy
	- Many different designs and implementations

## RAID
- RAID 0
	- Striping without parity
		- High Performance
		- No Fault Tolerance
- RAID 1
	- Mirroring
		- Duplicates data for fault tolerance
		- Requires twice the disk space
- RAID 5
	- Striping with parity
		- Fault tolerant
		- Only requires an additional disk for redundancy
- RAID Pairs: 
	- Multiple RAID types
		- 0+1
		- 1+0
		- 5+1
		- Etc...
	- Combine RAID methods to increase redundancy

