#!/usr/bin/bash

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365


#Generating a 4096 bit RSA private key
#............................++
#.........................................................................................#.........................................................................................#.........................................................................................#.......................................................................++
#writing new private key to 'key.pem'
#Enter PEM pass phrase:
#Verifying - Enter PEM pass phrase:
#Verify failure
#Enter PEM pass phrase:
#Verifying - Enter PEM pass phrase:
#——
#You are about to be asked to enter information that will be incorporated
#into your certificate request.
#What you are about to enter is what is called a Distinguished Name or a DN.
#There are quite a few fields but you can leave some blank
#For some fields there will be a default value,
#If you enter '.', the field will be left blank.
#——
#Country Name (2 letter code) [AU]:RU    
#State or Province Name (full name) [Some-State]:Moscow Region
#Locality Name (eg, city) []:Moscow
#Organization Name (eg, company) [Internet Widgits Pty Ltd]:ayrapetov inc.
#Organizational Unit Name (eg, section) []:development dept.
#Common Name (e.g. server FQDN or YOUR name) []:Artem
#Email Address []:ayeaye.post@gmail.com
