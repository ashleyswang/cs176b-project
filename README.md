
# Network Level Ad Block

### VPN: Configured using OpenVPN
Guide used: https://raspberrytips.com/install-openvpn-raspberry-pi/ <br>
*Note: This guide is outdated and many of the instructions in the guide cannot be followed without additional procedures. For example, the `easyrsa` bashscript has been omitted/relocated in the newest version of OpenVPN and must be replaced in the correct directory.*

The configurations files for the OpenVPN API is not currently in the Github repository, but will be added later on. 

### Advertisement Detection
The packet sniffer programs are located in the `sniffers` folder. `firewall.py` and `sniffer.py` are identical programs with different lines commented out. `sniffer2.py` is a tested packet sniffing code (that we did not write) that we used primarily for debugging. Using the sniffers, we can extract the destination IP address.

All files for the implementation of the advertisement detection are in the folders labeled `get_domains_v*`. There are currently two versions of the script that provides this functionality. The version we intend on using is `get_domains_v2`.  The curated lists `hostnames.txt` and `adblock.txt` were taken from the repository https://github.com/notracking/hosts-blocklists. 

Libraries used: 
DNS Python: [http://www.dnspython.org/](http://www.dnspython.org/)
Socket: [https://docs.python.org/3/library/socket.html](https://docs.python.org/3/library/socket.html)
Numpy: [https://numpy.org/](https://numpy.org/)

### Packet Filter 
Packet filtering implementation is located in the directory `packet_filter`. The current version of the program drops all packets, however we will add the conditional statements soon. 

Libraries used: 
Python Netfilter Queue: [https://pypi.org/project/NetfilterQueue/](https://pypi.org/project/NetfilterQueue/)

