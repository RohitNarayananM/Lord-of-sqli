# Goblin

----------------

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
  $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("goblin");
  highlight_file(__FILE__); 
?>
```

Here we have one parameter no.``` if($result['id'] == 'admin') solve("goblin"); ``` We have to get the value 'Admin' as result.

If we give `no=1` we get a result as `Hello guest` and if we give `no=2` we don't get any result. If we put `no=2 or 1` we get a result. Also `no=2 or n=1` gives us the result.

To get admin we can put`no=2 or no=2` which will select the id from the second column which have the value admin.
