#!/usr/bin/env python3

from urllib import response
import requests
import json
# url for creating user accounts with sandbox 
sanbox_url = "https://rmguk--fullsandbo.my.salesforce.com/"
uname = "joshua.musiyarira@rmguk.com.fullsandbo"
pwd = "6Z4d_ZGL&6D*#@va"
# create outlook rule on email that sends the verification code to my inbox 
verification_code = ""

response = requests.get(sanbox_url)

status_code = response.status_code

if status_code == 200:
    print('Success!')
else:
    print(f"Error code: {status_code}")