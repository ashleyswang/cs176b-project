import socket
import struct
import textwrap

# Get ethernet frame from packet
def ethernet_frame(data):
	dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
	return mac_addr(dest_mac), mac_addr(src_mac), socket.htons(proto), data[:14]

# Get readable mac address (AA:BB:CC:DD:EE:FF)
def mac_addr(byte_addr):
	byte_str = map('{:02x}'.format, byte_addr)
	return ':'.join(byte_str).upper()

# Get IPv4 frame from packet
def ipv4_packet(data):
	version_header_len = data[0]
	version = version_header_len >> 4
	header_length = (version_header_len & 15) * 4
	ttl, proto, src, dest = struct.unpack('! 8x 8 8 2x 4s 4s', data[:20])
	return version, header_length, ttl, proto, ipv4(src), ipv4(dest), data[header_length:]

# Get readable IPv4 address (X.X.X.X)
def ipv4(addr):
	return '.'.join(map(str, addr))

def main():
	# For LINUX OS
	conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
	# For MAC OS
	# conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(3))

	while(1):
		raw_data, addr = conn.recvfrom(65536)
		dest_mac, src_mac, ether_proto, data = ethernet_frame(raw_data)
		print('\nEthernet Frame: \nDestination: {} \tSource: {} \tProtocol: {}'\
			.format(dest_mac, src_mac, ether_proto))

main()
