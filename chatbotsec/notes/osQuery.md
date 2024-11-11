OS Query
# OS Query

$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04 LTS
Release:        22.04
Codename:       jammy

$ uname -r
5.15.0-78-generic

$ uname -a
Linux yourhostname 5.15.0-78-generic #84~22.04.1-Ubuntu SMP Fri Jul 28 17:54:59 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

$ cat /etc/os-release
NAME="Ubuntu"
VERSION="22.04 LTS (Jammy Jellyfish)"
ID=ubuntu
ID_LIKE=debian
...

$ lscpu
Architecture:        x86_64
CPU(s):              4
Model name:          Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz
...

$ free -h
              total        used        free      shared  buff/cache   available
Mem:           7.7Gi       2.3Gi       3.8Gi       167Mi       1.6Gi       5.1Gi
Swap:          2.0Gi          0B       2.0Gi

$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       30G  15G   14G  53% /

$ lshw
...
