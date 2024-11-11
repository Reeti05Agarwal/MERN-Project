
# WebDecode

inscept the about page
use cyberchef

# IntroToBurp

Open burpsuite
open browser from burpsuite
paste the website tehre and fill the form
after filling form -> turn on the intercept, and click on register
the burpsuite will intercept the request the website to sending to the server. 
read it and then formward it to the server
then it will ask for authentification, just type anything and intercept the submit
in the last line will show what you types 


# Verify

sha256sum files/*
sha256sum files/* | grep "467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02"
>>> files/c6c8b911
decrypt.sh files/c6c8b911
>>> picoCTF{trust_but_verify_c6c8b911}

# canyousee

unzip image.jpg
exiftool image.jpg
echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fZGVjYTA2ZmJ9Cg==" | base64 -d   
>>> picoCTF{ME74D47A_HIDD3N_deca06fb}

# hideme

xxd flag.png
strings flag.png
binwalk -e flag.png

#  SQLi Lite

username: anything
password: ' OR 1--

# SQL Direct

select * from public.flags;

# hide and seek
