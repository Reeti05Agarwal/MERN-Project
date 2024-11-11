# bandit


## Level 0

ssh -p 2220 bandit0@bandit.labs.overthewire.org

password: bandit0

## Level 0 -> 1

ls -al
cat readme
>>> password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

## Level 1-> 2

ssh -p 2220 bandit1@bandit.labs.overthewire.org
password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

ls -al
cat < - 
>>> 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

## Level 2 -> 3

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

ls -al
cat 'spaces in this filename'
>>> MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

## Level 3 -> 4

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

ls -al
cat inhere
la -al
cat '...Hiding-From-You'
>>> 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

## Level 4 -> 5

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

ls -al
cat inhere
la -al
cat -- -file*
//The -- ensures that cat treats -file* as filenames even if they start with a -, which is often used to indicate options.

>>> 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

## Level 5 -> 6

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

ls -al
cd inhere
ls -alR
find . -type f ! -executable -size 1033c
>>> ./maybehere07/.file2
cd maybehere07
cat .file2
>>> HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

## Level 6 -> 7

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

ls -al
find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null
>>> /var/lib/dpkg/info/bandit7.password
cat /var/lib/dpkg/info/bandit7.password
>>> morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

## Level 7 -> 8

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

ls -al
grep millionth data.txt
>>> dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

## Level 8 -> 9

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

ls -al
head -n 10 data.txt
cat data.txt | sort | uniq -u
>>> 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

## Level 9 -> 10

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

ls -al
cat data.txt
strings data.txt | grep =====
>>> FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

## Level 10 -> 11

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

ls -al
cat data.txt
>>> VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
cat data.txt | base64 -d
>>> dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

## Level 11 -> 12

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

la -al
cat data.txt
>>> Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4
https://www.dcode.fr/caesar-cipher
>>> The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

## Level 12 -> 13

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

ls -al
cat data.txt
// the file is in hexadecimal format
mkdir /tmp/hexdump
cd /tmp/hexdump
cp /home/bandit12/data.txt .
xxd -r data.txt > hex
file hex
mv hex hex.gz
gunzip hex.gz
file hex
mv hex hex.bz2
bunzip2 hex.bz2
file hex
mv hex hex.gz
gunzip hex.gz
file hex
tar -xf hex
file data5.bin
tar -xf data5.bin
file data6.bin
mv data6.bin data6.bin.bz2
bunzip2 data6.bin.bz2
file data6.bin
tar -xf data6.bin
file data8.bin
mv data8.bin data8.bin.gz
cat data8.bin
>>> wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw


## Level 13 -> 14

ssh -p 2220 bandit2@bandit.labs.overthewire.org
password: wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

