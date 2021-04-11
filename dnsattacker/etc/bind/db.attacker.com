$TTL   60000
@               IN      SOA     dnsattacker.attacker.com.    root.dnsattacker.attacker.com. (
                        2006031201 ; serial
                        28800 ; refresh
                        14400 ; retry
                        3600000 ; expire
                        0 ; negative cache ttl
                        )

@        		 IN      NS      dnsattacker.attacker.com.
dnsattacker.attacker.com. IN	A 192.168.0.150

attacker  IN      A       192.168.0.151
