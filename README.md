
# Yoko_Dip_Switches_Addressing
Simple console DIP-switches addressing helper for Yokogawa (r) Centum VP (r), ProSafe-RS (r) stations.


Example:

Set address to DIP.
Domain number (1-31) --> 01
Station number (1-64) --> 32

	==========================
	|Domain address:		1
	==========================
	|  off  |  on  |
	----------------------
	1|  *   |      |parity
	2|  *   |      |off
	3|  *   |      |off
	4|  *   |      |16
	5|  *   |      |8
	6|  *   |      |4
	7|  *   |      |2
	8|      |   *  |1
	==========================
	|Station address:	32  
	==========================
	|  off  |  on  |
	----------------------
	1|  *   |      |parity
	2|  *   |      |64
	3|      |   *  |32
	4|  *   |      |16
	5|  *   |      |8
	6|  *   |      |4
	7|  *   |      |2
	8|  *   |      |1
	======================
	
Get address from DIP.
Please input DIP switches configuration as string (domain number: 10000011...).
DOMAIN --> 10000011
STATION --> 10000011

	=========================
	|Domain address:		3
	=========================
	|Station address:		3  
	=========================
