# Network Level Ad Block

### VPN: Configured using OpenVPN
Guide used: https://raspberrytips.com/install-openvpn-raspberry-pi/ <br>
*Note: This guide is outdated and many of the instructions in the guide cannot be followed without additional procedures. For example, the `easyrsa` bashscript has been omitted/relocated in the newest version of OpenVPN and must be replaced in the correct directory.*

The configurations files for the OpenVPN API is located in the `vpn_conf` directory. Note that this only contains information not having to do with the security measures of the VPN (ie. no certificates/keys). 

### DNS: Configured using DNSMasq
Guide used: https://wiki.archlinux.org/index.php/dnsmasq <br>

The configuration files for the DNSMasq server is located in the `dns_conf` directory. This includes both lists for the DNS blacklast that were generated from https://github.com/notracking/hosts-blocklists. The code for the generating the `.conf` file is located in the `dns_blacklist` directory.

### IP Tables Filter
The code used to maintain the rules in the Raspberry Pi's IP tables is located in the `iptable_filter` directory. The code also uses the domain list generated from https://github.com/notracking/hosts-blocklists. 

### VPN Client
The `.ovpn` files needed to connect to our VPN is in the `ovpns` directory. (There is 3 for Ryan to use on multiple devices and 3 for Prof. Almeroth. Please contact us if you need more `.ovpn` files.)

### Old Implementations
Previous implementations of the project can be found in `adblock_packet_filter` (second attempt -- more front to back) and `helper_funcs` (first attempt -- contains more separate pieces of functions). 
