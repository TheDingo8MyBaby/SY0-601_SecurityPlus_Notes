## Proxies
- Sits between the users and the external network
- Receives the user requests and sends the request on their behalf (The Proxy)
- Useful for caching information
	- Access control
	- URL filtering
	- Content scanning
- Applications may need to know how to use the proxy (Explicit)
- Some proxies are invisibly (Transparent)
## Application proxies
- One of the simplest `"Proxies"`is NAT
	- A network-level proxy
- Most proxies in use are application proxies
	- The proxy understands the way the application works
- A proxy may only known one application
	- HTTP
- Many proxies are multipurpose proxies
	- HTTP
	- HTTPS
	- FTP
	- Etc...
## Forward proxy
- An `"Internal Proxy"`
	- Commonly used to protect and control user access to the internet
![](../Images/240522-1%205.png)
## Reverse proxy
- Inbound traffic from the Internet to your internal service
![](../Images/240522-1%206.png)
## Open proxy
- A third-party, uncontrolled proxy
	- Can be significant security concern
	- Often used to circumvent existing security controls
![](../Images/240522-1%207.png)

