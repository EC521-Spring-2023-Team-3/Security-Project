# Security-Project

This repository explores URL brute force and deauthentication attack vulnerabilities in a Eufy S220 camera. 


**Deauthentication Attack**

The python script uses the scapy module to create the frames and packets to be sent. The user is prompted to enter the mac addresses of the eufy camera and the router along with the interface being used and the router's channel.

## RTMP Folder
**rtmpcheck.py**<br>
Gets Unix Time Stamp and Encodes the serial number with 4 digit hex code into base 64 and gets a rtmp URL. Then uses ffpmeg to check if the stream is live.<br>
**progressbar.py**<br>
Add a dynamic progress bar so i could see the progress of the program.<br>
**faster.py**<br>
Old program did everything one by one. using asyncio to speed thins up by running things in parrallel.<br>
### Other Files
the Pcap file contains network traffic from when a laptop connected to the eufy portal and streamed the webcam video
