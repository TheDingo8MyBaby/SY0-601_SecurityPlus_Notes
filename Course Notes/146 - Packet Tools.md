## Wireshark
- Graphical packet analyzer
	- Get into the details
- Gathers frames on the network
	- Or in the air
	- Sometimes built into the device
- View traffic patterns
	- Identify unknown traffic
	- Verify packet filtering and security controls
- Extensive decodes
	- View the application traffic
![](../Images/240606-1%202.png)
## tcpdump
- Capture packets form the command line
	- Display packets on the screen
	- Write packets to a file
![](../Images/240606-2%201.png)
```
sudo tcpdump
```
![](../Images/240606-3%201.png)
## Tcpreplay
- A suite of packet replay utilities
	- Replay and edit packet captures
	- Open source
- Test security devices
	- Check IPS signatures and firewalls rules
- Test and tune IP Flow/NetFlow devices
	- Send hundreds of thousands of traffic flows per second
- Evaluate the performance of security devices
	- Test throughput and flows per second

