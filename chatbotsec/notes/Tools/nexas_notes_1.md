

# networking
port 0 is invalid

the ip address is on network interface card

Static and dynamic ip address
static ip addresses are thoughs that remain stegnant even after the networking is changes. its on your hardware.
dynamic ip address changes as you change the network

the main router wifi is turned off, only internet is on. 
WPA to protect the routers.

tcp -> connection oriented protocol
udp -> connection less protocol

## Port

ftp -> 20 (udp) and 21 (tcp)
ftp ip_address



smtp -> 25

## tools

### nmap
nmap  -sn ip/subnet
netdiscover

### ssh
ssh ip username password

### telnet
remotely connect to the machine with ip address

# active directory
Active Directory (AD) is a directory service developed by Microsoft for Windows domain networks. It provides a centralized and standardized way to manage and authenticate network resources, users, and policies. 
Its using ethernet cable. the admin computer is connected to the other computers through switch. the admin is downloading the windows in other pc by using ethernet using active directory. 

# VLAN


# Reconnaisance
- ports
- ip address
- Domain Name
- Network Topology
- Social Media
- Public Records
- services
- version {headers}
- OS Versions
- cookies
- token id from github
- Database info and version
- ISP
- Phone Numbers
- Metadata
- XML {like html but newer version}
- every website is having a robots.txt which will give some info about it {without it, the website is illigal}

## Password Directory
- /etc/passwd

# traceroute

```bash
traceroute google.com
```
## output:
traceroute to google.com (142.250.70.46), 30 hops max, 60 byte packets
 1  192.168.99.148 (192.168.99.148)  3.850 ms  3.825 ms  4.864 ms
 2  * * *
 3  255.0.0.1 (255.0.0.1)  32.918 ms  43.890 ms  32.884 ms
 4  255.0.0.2 (255.0.0.2)  43.856 ms  43.837 ms  42.422 ms
 5  * * *
 6  255.0.0.4 (255.0.0.4)  40.588 ms  181.212 ms  39.514 ms
 7  172.26.102.35 (172.26.102.35)  181.121 ms 172.26.102.34 (172.26.102.34)  181.107 ms 172.26.102.35 (172.26.102.35)  181.086 ms
 8  192.168.92.160 (192.168.92.160)  181.068 ms 192.168.92.162 (192.168.92.162)  180.373 ms  178.972 ms
 9  * * *
10  * * *
11  173.194.121.8 (173.194.121.8)  119.376 ms  119.337 ms 74.125.51.166 (74.125.51.166)  119.304 ms
12  * 192.178.84.191 (192.178.84.191)  294.112 ms *
13  192.178.86.243 (192.178.86.243)  294.059 ms 216.239.46.136 (216.239.46.136)  60.380 ms 72.14.239.246 (72.14.239.246)  60.327 ms
14  pnbomb-aa-in-f14.1e100.net (142.250.70.46)  60.284 ms 192.178.86.243 (192.178.86.243)  60.534 ms pnbomb-aa-in-f14.1e100.net (142.250.70.46)  60.493 ms

## info to take: 

The output of the `traceroute` command you provided shows the path that packets take from your machine to `google.com` (IP address 142.250.70.46). Here's a breakdown of the key information you can extract:

### 1. **Local Network and ISP Information**
   - **Hop 1**: `192.168.99.148` – This is your local router or gateway. The IP address is private (within the 192.168.x.x range), indicating that you are on a private network behind a router.

### 2. **Routing and Connectivity Information**
   - **Hops 2 and 5**: `* * *` – These hops timed out, which means that the traceroute could not get a response from these routers. This could be due to firewalls or routers configured not to respond to traceroute requests.
   - **Hops 3 and 4**: `255.0.0.1` and `255.0.0.2` – These are also private IP addresses and might represent a local network or intermediary devices within the private network. Note that the use of IP addresses in the 255.x.x.x range is non-standard for regular routing and might indicate a misconfiguration or placeholder addresses.
   - **Hop 7**: `172.26.102.35` – This IP address belongs to a private IP range (172.16.0.0 – 172.31.255.255). It might be a router or device within a private network or a network segment.
   - **Hop 8**: `192.168.92.160` – Another private IP address indicating the internal network.

### 3. **Public Network Path**
   - **Hop 11**: `173.194.121.8` – This is an IP address assigned to a Google server, showing that packets are reaching Google's network.
   - **Hop 12**: `192.178.84.191` – Another IP within a private or less commonly used range, possibly an internal Google network address.
   - **Hop 13**: `192.178.86.243` and `216.239.46.136` – These are also within Google's network.
   - **Final Destination (Hop 14)**: `pnbomb-aa-in-f14.1e100.net` – The hostname resolves to the IP address `142.250.70.46`, which is the Google server you are trying to reach. This confirms that packets eventually arrive at Google's server.

### 4. **Latency Information**
   - **Latency Times**: The times in milliseconds (e.g., `3.850 ms`, `32.918 ms`) represent the round-trip time for packets to reach each hop and return. This helps in understanding the network delay at each point.

### Summary
- **Local Network**: Your packets start from a local network and pass through several hops with some private addresses, indicating internal or intermediary network devices.
- **Public Network**: Eventually, the packets reach Google's infrastructure, showing that the connection to Google is successful and identifying the path taken.
- **Timeouts**: The timeouts (`* * *`) at certain hops could be due to routers not responding to traceroute requests, which is not uncommon.

This information can help in diagnosing network issues, understanding the route taken by packets, and identifying potential bottlenecks or areas where network configurations might be affecting connectivity.


# Scanning Tools
- go buster


