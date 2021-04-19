# TOPOLOGY
![](https://github.com/lucarighes/netsec_dns_lab/blob/main/TOPO.png)

---

# COMMAND

```bash
sudo kathara lstart #start 
sudo kathara lclean #stop
sudo kathara wipe #delete
sudo kathara list #show instances
tc qdisc add dev eth0 root netem delay 200ms #add a constant delay to interface eth0
tc qdisc show  dev eth0 #display active rules
tc qdisc del dev eth0 root #remove all rules
bash install.sh #install python + scapy
ip.dst == 192.168.0.201 && ip.src == 192.168.0.200 && udp.port == 53 && dns.flags.rcode == 0000 #wireshark filter to sniff only the DNS error-free answers from the recursive server to the client
```

---

# BIND v9 

View cache
```bash
rndc dumpdb -cache
cat /var/cache/bind/named_dump.db
```

Clean cache
```bash
rndc flush
rndc reload
```

---

# NS

```bash
nslookup trusted.website.com --> 192.168.0.101
```
