#include <tins/tins.h>
#include <iostream>

using std::cout;
using std::endl;

using namespace Tins;

PacketSender sender;

bool callback(const PDU& pdu) {
    EthernetII eth = pdu.rfind_pdu<EthernetII>();
    IP ip = eth.rfind_pdu<IP>();
    UDP udp = ip.rfind_pdu<UDP>();
    DNS dns = udp.rfind_pdu<RawPDU>().to<DNS>();

    // Is it a DNS query?
    if (dns.type() == DNS::QUERY) {
        // Let's see if there's any query for an "A" record.
        for (const auto& query : dns.queries()) {
            if (query.query_type() == DNS::A) {
                // Here's one! Let's add an answer.
                dns.add_answer(
                    DNS::resource(
                        query.dname(), 
                        "127.0.0.1",
                        DNS::A, 
                        query.query_class(), 
                        // 777 is just a random TTL
                        777
                    )
                );
            }
        }
        // Have we added some answers?
        if (dns.answers_count() > 0) {
            // It's a response now
            dns.type(DNS::RESPONSE);
            // Recursion is available(just in case)
            dns.recursion_available(1);
            // Build our packet
            auto pkt = EthernetII(eth.src_addr(), eth.dst_addr()) /
                       IP(ip.src_addr(), ip.dst_addr()) /
                       UDP(udp.sport(), udp.dport()) /
                       dns;
            // Send it!
            sender.send(pkt);
        }
    }
    return true;
}

int main(int argc, char* argv[]) {
    if(argc != 2) {
        cout << "Usage: " <<* argv << " <interface>" << endl;
        return 1;
    }
    // Sniff on the provided interface in promiscuos mode
    SnifferConfiguration config;
    config.set_promisc_mode(true);
    // Use immediate mode so we get the packets as fast as we can
    config.set_immediate_mode(true);
    // Only capture udp packets sent to port 53
    config.set_filter("udp and dst port 53");
    Sniffer sniffer(argv[1], config);
    
    // All packets will be sent through the provided interface
    sender.default_interface(argv[1]);
    
    // Start the capture
    sniffer.sniff_loop(callback);
}
