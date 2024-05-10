## File backups
- The archive attribute (archive bit)
	- Set when a files is modified
- Full
	- Everything
		- You'll want this one first
- Incremental
	- All files changed since the last incremental backup
- Differential
	- All files changed since the last full backup
## Incremental backup
- A full backup is taken first
- Subsequent backups contain data changed since the last full backup and last incremental backup
	- These are usually smaller than the full backup
- A restoration requires the full backup and all of the incremental backups

![](Images/Pasted%20image%2020240501194539.png)- A full backup is taken first
- Subsequent backups contain data changed since the last full backup
	- These usually grow larger as data is changed
- A restoration requires the full backup and the last differential backup

![](Images/Pasted%20image%2020240501194728.png)
![](Images/Pasted%20image%2020240501194809.png)- Magnetic tape
	- Sequential storage
	- 100GB to multiple terabytes per cartridge
	- Easy to ship and store
- Disk
	- Faster than magnetic tape
	- Deduplicate and compress
- Copy
	- A useful strategy
	- May not include versioning
	- May need to keep offsite
## NAS vs. SAN
- Network Attached Storage (NAS)
	- Connect to a shared storage device across the network
	- File-level access
- Storage Area Network (SAN)
	- Looks and feels like a local storage device
		- Block-level access
	- Very efficient reading and writing
- Requires a lot of bandwidth
	- May use an isolated network and high-speed network technologies
## Other backups
- Cloud
	- Backup to a remote device in the cloud
	- Support many devices
	- May be limited by bandwidth
- Image
	- Capture an exact replica of everything on a storage drive
	- Restore everything on a partition
		- Including operating system files and user documents
## Backup locations
- Offline backup
	- Backup to local devices
	- Fast and secure
	- Must be protected and maintained
	- Often requires offsite storage for disaster recovery
- Online backup
	- Remote network-connected third-party
	- Encrypted
	- Accessible from anywhere
	- Speed is limited by network bandwidth

