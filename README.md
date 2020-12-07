# visualdriver

## Arduino PWM Manager
### 000 to 009: Instant Single Light Control

Example Input: 000250 --> Set light 0 to 250

Number of Bytes: 2

Description of Bytes: 
1.  TypeId and LightId
1.  State to set

### 010 to 019: Linear Dimming Light Control

Example Input: 011250030 --> Set light 1 to 250 with a steptime of 30

Number of Bytes: 3

Description of Bytes: 
1.  TypeId and LightId
1.  State to set
1.  Steptime --> Milliseconds per step



## Virtual Environment
### Linux
virtualenv visualdriver
source visualdriver/bin/activate