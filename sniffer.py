import socket
import struct
import textwrap

DATA_TAB_3 = '\t\t\t'

#main function in order to listening to the traffic
def main():
	conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

	while True:
		raw_data, addr = conn.recvfrom(65536)
		dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
		print("\nEthernet Frame:")
		print(f"Destination: {dest_mac}, Source: {src_mac}, Protocol: {eth_proto}")

		# 8 for IPV4
		if eth_proto == 8:
			(version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
			print("	"+"IPV4 Packet: ")
			print(f"			Version:{version}, Header length: {header_length}, TTL: {ttl}")
			print(f"			Protocol: {proto},  Source{src},  Target:{target}")	

			if proto == 1:
				icmp_type, code, checksum, data = icmp_packet(data)
				print(f"	ICMP packet: ")
				print(f"		Type: {icmp_type}, Code: {code}, Checksum: {checksum}")
				print(f"		Data: ")
				print(format_multi_line(DATA_TAB_3,data))		


# unpacking the ethernet frame
def ethernet_frame(data):
	dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
	return get_mac_addr(dest_mac),get_mac_addr(src_mac),socket.htons(proto),data[14:]

# return properly format MAC address
def get_mac_addr(bytes_addr):
	bytes_str = map('{:02x}'.format,bytes_addr)
	return ':'.join(bytes_str).upper()


def ipv4_packet(data):
	version_header_length = data[0]
	version = version_header_length >> 4
	header_length = (version_header_length & 15) * 4
	ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s',data[:20])
	return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length]

# Returns properly formatted IPV4 addresses
def ipv4(addr):
	return '.'.join(map(str,addr))

# Unpacks ICMP packet
def icmp_packet(data):
	icmp_type, code, checksum = struct.unpack('! B B H',data[:4])
	return icmp_type, code, checksum, data[4:]


#Unpacks UDP semgents
def udp_segment(data):
	src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])

def format_multi_line(prefix, string, size=80):
	size = len(prefix)
	if isinstance(string, bytes):
		string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
		if size % 2: 
			size = 1
	return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

# Unpacks TCP segments
def tcp_segment(data):
	(src_port, dest_port, sequence, acknoledgement, offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
	offset = (offset_reserved_flags >> 12) * 4
	flag_urg = (offset_reserved_flags & 32) >> 5
	flag_ack = (offset_reserved_flags & 16) >> 5
	flag_psh = (offset_reserved_flags & 8) >> 5
	flag_rst = (offset_reserved_flags & 4) >> 5
	flag_syn = (offset_reserved_flags & 2) >> 5
	flag_fin = offset_reserved_flags & 1
	return src_port, dest_port, sequence, acknoledgement, offset_reserved_flags,flag_urg,flag_ack,flag_psh,flag_rst,flag_syn, flag_fin, data[offset:]



main()	

