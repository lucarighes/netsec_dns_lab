$TTL   60000
@               IN      SOA     dnscom.com.    root.dnscom.com. (
                        2006031201 ; serial
                        28800 ; refresh
                        14400 ; retry
                        3600000 ; expire
                        0 ; negative cache ttl
                        )
@                   IN      NS      dnscom.com.
dnscom.com.         IN      A       192.168.0.10

website.com.             IN      NS      dnswebsite.website.com.
dnswebsite.website.com.  IN      A       192.168.0.100
