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
