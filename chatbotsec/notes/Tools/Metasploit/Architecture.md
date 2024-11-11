 ![[Pasted image 20241007182835.png]]

# File System

- Its installed in `/usr/share/metasploit-framework` directory
![[Pasted image 20241007183011.png]]


## Data
It contains editable files used by Metasploit to store binaries required for certain exploits, wordlists, images, and more.

```
msf6 > ls /usr/share/metasploit-framework/data/
[*] exec: ls /usr/share/metasploit-framework/data/

README.md               ipwn                    rocketmq_versions_list.json
SqlClrPayload           isight.bundle           shellcode
auxiliary               jtr                     snmp
capture_config.yaml     kafka_ui_versions.json  sounds
eicar.com               lab                     templates
eicar.txt               logos                   unirpc-errors.yaml
emailer_config.yaml     markdown_doc            utilities
evasion                 meterpreter             vncdll.x64.dll
exchange_versions.json  mime.yml                vncdll.x86.dll
exploits                msfcrawler              webcam
f5-mcp-objects.txt      passivex                wmap
flash_detector          php                     wordlists
headers                 post                    ysoserial_payloads.json

```


## Documentation
Contains the doc for framework
```
msf6 > ls /usr/share/metasploit-framework/documentation/
[*] exec: ls /usr/share/metasploit-framework/documentation/

CODE_OF_CONDUCT.md  README.md            cli        developers_guide.pdf.gz
CONTRIBUTING.md.gz  changelog.Debian.gz  copyright  modules
```
## Lib

Contains the meat of the framework code base

```
msf6 > ls /usr/share/metasploit-framework/lib
[*] exec: ls /usr/share/metasploit-framework/lib

README.md      expect.rb   msf_autoload.rb  postgres         rbmysql.rb  rubocop  tasks
anemone        metasploit  msfdb_helpers    postgres_msf.rb  rex         snmp     telephony
anemone.rb     msf         msfenv.rb        rabal            rex.rb      snmp.rb  telephony.rb
enumerable.rb  msf.rb      net              rbmysql          robots.rb   sqlmap   windows_console_color_support.rb

```


## Modules
Contains actual Modules for exploits, auxiliary and post modules, payloads, encoders and nop generators

```
msf6 > ls /usr/share/metasploit-framework/modules
[*] exec: ls /usr/share/metasploit-framework/modules

README.md  auxiliary  encoders  evasion  exploits  nops  payloads  post

```

## Plugins

Contains plugins

```
msf6 > ls /usr/share/metasploit-framework/plugins
[*] exec: ls /usr/share/metasploit-framework/plugins

README.md          besecure.rb        ffautoregen.rb  msgrpc.rb    request.rb           socket_logger.rb  token_hunter.rb
aggregator.rb      capture.rb         ips_filter.rb   nessus.rb    rssfeed.rb           sounds.rb         wiki.rb
alias.rb           db_credcollect.rb  lab.rb          nexpose.rb   sample.rb            sqlmap.rb         wmap.rb
auto_add_route.rb  db_tracker.rb      libnotify.rb    openvas.rb   session_notifier.rb  thread.rb
beholder.rb        event_tester.rb    msfd.rb         pcap_log.rb  session_tagger.rb    token_adduser.rb

```


## Scripts
Contains meterpreter and other scripts

```
msf6 > ls /usr/share/metasploit-framework/scripts
[*] exec: ls /usr/share/metasploit-framework/scripts

README.md  meterpreter  resource  shell
```

## Tools

Has various useful cmd utilities

```
msf6 > ls /usr/share/metasploit-framework/tools
[*] exec: ls /usr/share/metasploit-framework/tools

README.md  automation  context  dev  docs  exploit  hardware  memdump  modules  password  payloads  recon  smb_file_server.rb
```


## Rex

- Basic lib for most tasks
- Handles sockets, protocols, text transformations, and others
- SSL, SMB, HTTP, XOR, Base64, Unicode


## Msf::Core

- Provides basic API
- Defines metasploit framework
## Msf::Base

- Provides friendly API
- Provides simplified API for use in framework


# Modules and Locations

All the custom modules is stored at `¬/.msf4/modules/`


## Exploits

Modules that use payloads.

```
msf6 > ls /usr/share/metasploit-framework/modules/exploits/
[*] exec: ls /usr/share/metasploit-framework/modules/exploits/

aix        bsd     example.py                 example_webapp.rb  hpux   mainframe  openbsd  solaris
android    bsdi    example.rb                 firefox            irix   multi      osx      unix
apple_ios  dialup  example_linux_priv_esc.rb  freebsd            linux  netware    qnx      windows
```
## Auxiliary

It includes port scanners , fuzzers, sniffers and more

```
msf6 > ls /usr/share/metasploit-framework/modules/auxiliary/
[*] exec: ls /usr/share/metasploit-framework/modules/auxiliary/

admin    bnat    cloud    docx  example.py  fileformat  gather  pdf      server   spoof  voip
analyze  client  crawler  dos   example.rb  fuzzers     parser  scanner  sniffer  sqli   vsploit

```
## Payloads, Encoders, Nops

```
msf6 > ls /usr/share/metasploit-framework/modules/payloads/
[*] exec: ls /usr/share/metasploit-framework/modules/payloads/

adapters  singles  stagers  stages

```

```
msf6 > ls /usr/share/metasploit-framework/modules/encoders/                                                                    
[*] exec: ls /usr/share/metasploit-framework/modules/encoders/                                                                 
                                                                                                                               
cmd  generic  mipsbe  mipsle  php  ppc  ruby  sparc  x64  x86
```

```
msf6 > ls /usr/share/metasploit-framework/modules/nops/                                                                
[*] exec: ls /usr/share/metasploit-framework/modules/nops/

aarch64  armle  cmd  mipsbe  php  ppc  sparc  tty  x64  x86
```


## Loading Additional Module Trees

Pass the **-m** option when running msfconsole to load additional modules at runtime:

```
```shellsession
root@kali:~# msfconsole -m ~/secret-modules/
```
```




If you need to load additional modules from with msfconsole, use the **loadpath** command:

```plaintext
msf > loadpath
Usage: loadpath </path/to/modules>

Loads modules from the given directory which should contain subdirectories for
module types, e.g. /path/to/modules/exploits

msf > loadpath /usr/share/metasploit-framework/modules/
Loaded 399 modules:
    399 payloads

```


# Metasploit Object Model


In the Metasploit Framework, all modules are Ruby classes.

- _Modules_ inherit from the type-specific class
- The type-specific class inherits from the Msf::Module class
- There is a shared common API between modules

_Payloads_ are slightly different.

- Payloads are created at runtime from various components
- Glue together stagers with stages


# Mixins and Plugins

## Metasploit Mixins

Mixins are quite simply, the reason why Ruby rocks.

- Mixins _include_ one class into another
- This is both different and similar to inheritance
- Mixins can override a class’ methods

Mixins can add new features and allows modules to have different ‘flavors’.

- Protocol-specific (HTTP, SMB)
- Behaviour-specific (brute force)
- _connect()_ is implemented by the TCP mixin
- _connect()_ is then overloaded by FTP, SMB, and others

Mixins can change behavior.

- The Scanner mixin overloads _run()_
- Scanner changes _run()_ for _run_host()_ and _run_range()_
- It calls these in parallel based on the THREADS setting
- The _BruteForce_ mixin is similar

## Metasploit Plugins

Plugins work directly with the API.

- They manipulate the framework as a whole
- Plugins hook into the event subsystem
- They automate specific tasks that would be tedious to do manually

Plugins only work in the msfconsole.

- Plugins can add new console commands
- They extend the overall Framework functionality
```plaintext
class MyParent
     def woof
          puts “woof!”
     end
end

class MyClass > MyParent
end

object = MyClass.new
object.woof() => “woof!”

================================================================

module MyMixin
     def woof
          puts “hijacked the woof method!”
     end
end

class MyBetterClass > MyClass
     include MyMixin
end
```

