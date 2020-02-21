import socket
import struct
import textwrap

# Unpack ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return mac_addr(dest_mac), mac_addr(src_mac), socket.htons(proto), data[:14]

# Get readable mac address (AA:BB:CC:DD:EE:FF)
def mac_addr(byte_addr):
    byte_str = map('{:02x}'.format, byte_addr)
    return ':'.join(byte_str).upper()

# Unpack IPv4 frame
def ipv4_packet(data):
    version_header_len = data[0]
    version = version_header_len >> 4
    header_length = (version_header_len & 15) * 4
    ttl, proto, src, dest = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(dest), data[header_length:]

# Get readable IPv4 address (X.X.X.X)
def ipv4_addr(addr):
    return '.'.join(map(str, addr))

# Unpack ICMP packet
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

# Unpack TCP segment
def tcp_seg(data):
    src_port, dest_port, seq, ack, offset_reserved_flags = \
        struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    return src_port, dest_port, seq, ack, flag_urg, flag_ack, flag_psh, flag_rst,\
        flag_syn, flag_fin, data[offset:]

# Unpack UDP segment
def udp_seg(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, size, data[8:]

# String constants for formatting
TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t   '
DATA_TAB_2 = '\t\t   '
DATA_TAB_3 = '\t\t\t   '
DATA_TAB_4 = '\t\t\t\t   '

# Formats the output line
def format_output_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size-= 1
            return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

def main():
    # For LINUX OS
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    # For MAC OS
    # conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(3))

    while(1):
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, ether_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame: \n\tDestination: {} \tSource: {} \tProtocol: {}'\
            .format(dest_mac, src_mac, ether_proto))

        # IPv4
        if ether_proto == 8:
            (version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
            print(TAB_1 + "IPV4 Packet:")
            print(TAB_2 + 'Version: {}, Header Length: {}, TTL: {}'.format(version, header_length, ttl))
            print(TAB_3 + 'protocol: {}, Source: {}, Target: {}'.format(proto, src, target))

            # ICMP
            if proto == 1:
                icmp_type, code, checksum, data = icmp_packet(data)
                print(TAB_1 + 'ICMP Packet:')
                print(TAB_2 + 'Type: {}, Code: {}, Checksum: {},'.format(icmp_type, code, checksum))
                print(TAB_2 + 'ICMP Data:')
                print(format_output_line(DATA_TAB_3, data))

            # TCP
            elif proto == 6:
                src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, \
                    flag_syn, flag_fin = struct.unpack('! H H L L H H H H H H', raw_data[:24])
                print(TAB_1 + 'TCP Segment:')
                print(TAB_2 + 'Source Port: {}, Destination Port: {}'.format(src_port, dest_port))
                print(TAB_2 + 'Sequence: {}, Acknowledgment: {}'.format(sequence, acknowledgment))
                print(TAB_2 + 'Flags:')
                print(TAB_3 + 'URG: {}, ACK: {}, PSH: {}'.format(flag_urg, flag_ack, flag_psh))
                print(TAB_3 + 'RST: {}, SYN: {}, FIN:{}'.format(flag_rst, flag_syn, flag_fin))

                if len(data) > 0:
                    # HTTP
                    if src_port == 80 or dest_port == 80:
                        print(TAB_2 + 'HTTP Data:')
                        try:
                            http = HTTP(data)
                            http_info = str(http.data).split('\n')
                            for line in http_info:
                                print(DATA_TAB_3 + str(line))
                        except:
                            print(format_output_line(DATA_TAB_3, data))
                    else:
                        print(TAB_2 + 'TCP Data:')
                        print(format_output_line(DATA_TAB_3, data))
            # UDP
            elif proto == 17:
                src_port, dest_port, length, data = udp_seg(data)
                print(TAB_1 + 'UDP Segment:')
                print(TAB_2 + 'Source Port: {}, Destination Port: {}, Length: {}'.format(src_port, \
                    dest_port, length))

            # Other IPv4
            else:
                print(TAB_1 + 'Other IPv4 Data:')
                print(format_output_line(DATA_TAB_2, data))

        else:
            print('Ethernet Data:')
            print(format_output_line(DATA_TAB_1, data))


main()
