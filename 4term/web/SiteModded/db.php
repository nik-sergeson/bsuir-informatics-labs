<?php

$dbhost = "localhost"; 
$dbusername = "root"; 
$dbpass = "";
$dbname = "mydb"; 
$dbconnect = mysql_connect ($dbhost, $dbusername, $dbpass);
mysql_set_charset('utf8',$dbconnect);
mysql_select_db($dbname);
?>