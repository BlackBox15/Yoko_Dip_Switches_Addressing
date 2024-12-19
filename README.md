
# YokoDIPAddressing
Simple DIP-switches addressing helper for Yokogawa stations.


Example:

Domain address: 01
Station address: 32
IP address: 192.168.01.32

	======================
	|Domain address:   01
	======================
	|  off  |  on  |
	----------------------
	1|  *   |      |parity
	2|  *   |      |off
	3|  *   |      |off
	4|  *   |      |16
	5|  *   |      |8
	6|  *   |      |4
	7|  *   |      |2
	8|  *   |      |1
	______________________
	|Station address: 32  
	======================
	|  off  |  on  |
	----------------------
	1|  *   |      |parity
	2|  *   |      |64
	3|  *   |      |32
	4|  *   |      |16
	5|  *   |      |8
	6|  *   |      |4
	7|  *   |      |2
	8|  *   |      |1
	======================
