- Overwriting a buffer of memory
	- Spills over into other memory areas
- Developers need to perform bounds checking
	- The attackers spend a lot of time looking for openings
- Not a simple exploit
	- Takes time to avoid crashing things
	- Takes time to make it do what you want
- A really useful buffer overflow is repeatable
	- Which means that a system can be compromised
![](../Images/028%20-%20Buffer%20overflow-1.png)
- Nothing has been set for Variable A
	- If vulnerable, you can try to overflow area A
![](../Images/028%20-%20Buffer%20overflow-2.png)
- There's potential that if you overflow area "B", you can potentially crash the system or Gain elevated access

