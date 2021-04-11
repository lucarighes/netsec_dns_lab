# TOPOLOGY

dnsroot 192.166.0.1  
dnscom 192.168.0.10

dnswebsite 192.168.0.100  
website 192.168.0.101

dnsclient 192.168.0.200  
client 192.168.0.201

---

# COMMAND

```bash
sudo kathara lstart #start 
sudo kathara lclean #stop
sudo kathara wipe #delete
sudo kathara list #show instances
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
nslookup website.com
```
