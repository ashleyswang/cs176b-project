from netfilterqueue import NetfilterQueue
import struct
import textwrap
import numpy as np
from dns import reversename, resolver
import subprocess
from scapy.all import *

def lookup_domain(ip_addr):
    name = reversename.from_address(ip_addr)
    try:
        domain = str(resolver.query(name,"PTR")[0]).strip('.')
        return domain
    except:
        return None

def is_ad(ip_addr): 
    #domains = np.load("domains.npy")
    domain = lookup_domain(ip_addr)
    print("\tIP:", ip_addr, "DOMAIN:", domain)
    #if (domain is None): return False
    #else: return (domain in domains)

'''
def get_ip(pkt):
    data = pkt.get_payload()
    print(data)
    print(pkt.get_mark())
    dest_mac, src_mac, ether_proto = struct.unpack('! 6s 6s H', data[:14])
    data = data[:14]
    # IPv4 packet
    if ether_proto == 49320:
        ttl, proto, src, dest = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
        src_ip = '.'.join(map(str, src))
        dest_ip = '.'.join(map(str, dest))
        return src_ip, dest_ip
    return None, None
'''   
     
def print_and_accept(pkt):
    print(pkt)
    packet = IP(pkt.get_payload())
    print(packet.dst, packet.src)
    #is_ad(packet.src)
    #is_ad(packet.dst)
    '''
    if(is_ad(src_ip) or is_ad(dest_ip)):    
        pkt.drop()
        print('DROPPED PACKET\tSOURCE:', src_ip, '\tDEST', dest_ip)
    else:
        pkt.accept()

    '''
    pkt.accept()

if __name__ == '__main__':
    # add rule to ip table
    subprocess.call("iptables -I INPUT -d 192.168.0.0/24 -j NFQUEUE --queue-num 1", shell=True)

    nfqueue = NetfilterQueue()
    nfqueue.bind(1, print_and_accept)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        print('')
        nfqueue.unbind()
        subprocess.call("iptables -F", shell=True)

    nfqueue.unbind()

    # remove rule from ip table
    subprocess.call("iptables -F", shell=True)

