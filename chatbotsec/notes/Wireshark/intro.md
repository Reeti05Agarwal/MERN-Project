# Wireshark

*Reconasance*

Wireshark captures the data coming or going through the NICs on its device by using an underlying packet capture library. By default, Wireshark captures on-device data only, but it can capture almost all the data on its LAN if run in promiscuous mode. Currently, Wireshark uses NMAP’s Packet Capture library(called npcap). 
The top pane shows real-time traffic, the middle one shows information about the chosen packet and the bottom pane shows the raw packet data. 
The top pane shows source address(IPv4 or IPv6) destination address, source and destination ports, protocol to which the packet belongs to and additional information about the packet. 

## Packet Capturing
Choose the network interface you want to capture data from


# Packets Filters
Since there are a lot of packets going in and out every second, looking at all of them or searching for one type of packets will be tedious. This is why packet filters are provided. 

## factos

- IP Address
- Port Number
- protocol at capture level/ display level

    host (capture the traffic through a single target)
    net( capture the traffic through a network or sub-network). “net” can be prefixed with “src” or “dst” to indicate whether the data coming from or going to the target host(s).)
    port (capture the traffic through or from a port). “port” can be prefixed with “src” or “dst” to indicate whether the data coming from or going to the target port.
    “and”, “not” and “or” logical connectives.(Used to combine multiple filters together).



tcp.port==80/udp.port==X 
    	shows the tcp/udp traffic at port X.
http.request.uri matches “parameter=value$” 
    	shows packets that are HTTP requests at the application layer level and their URI ends with a parameter with some value.
    The logical connective and or and not work here too.
    
ip.src==192.168.0.0/16 and ip.dst==192.168.0.0/16 
    	will show traffic to and from workstations and servers.

## Plugins

extra pieces of codes that can be embedded into the native Wireshark. Plugins help in analysis by: 

 

    Showing parameter specific statistics and insights.
    Handling capture files and issues related to their formats.
    Collaborating with other tools and frameworks to set up an all-in-one network monitoring solution.
