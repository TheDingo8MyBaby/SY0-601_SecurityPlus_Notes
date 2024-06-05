## curl
- Client URL
	- Retrieve data using a URL
	- Uniform Resource Locator
		- Web pages
		- FTP
		- Emails
		- Databases
		- Etc...
- Grab the raw data
	- Search
	- Parse
	- Automate
```
curl www.professmermesser.com
```
![](../Images/240604-1%2012.png)
```
curl https://www.professormessor.com
```
![](../Images/240604-2%203.png)
## IP scanners
- Search a network for IP addresses
	- Locate active devices
	- Avoid doing work on an IP address that isn't there
- Many different techniques
	- ARP
		- If on the local subnet
	- ICMP requests
		- Ping
	- TCP ACK
	- ICMP timestamp requests
- A response means more recon can be done
	- Keep gathering information
		- Nmap
		- hping
		- Etc...
## hping
- TCP/IP packet assembler/analyzer
	- A ping that can send almost anything
- Ping a device
	- ICMP, TCP, UDP
		- `hping3 --destport 80 10.1.10.1`
- Send crafted frames
	- Modify all;
		- IP
		- TCP
		- UDP
		- ICMP values
		- Etc...
- A powerful tool
	- It's easy to accidentally flood and DoS
		- BE CAREFUL!
## hping example
```
sudo hping3 10.1.10.1
```
![](../../240604-1.png)
```
sudo hping3 --scan 80-443 -S 10.1.10.1 -V 
```
![](../../240604-2.png)
