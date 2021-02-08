<?php
    session_start();
	
	$login = $_POST['login'];
	$password=$_POST['password'];
	
    $login = stripslashes($login);
    $login = htmlspecialchars($login);
	$password = stripslashes($password);
    $password = htmlspecialchars($password);
	
    $login = trim($login);	
    $password = trim($password);
	
	$password_part_crypt = md5("pass".$password);
	$password_full_crypt = md5($password_part_crypt."word");
	
    include ("db.php");
 
	$result = mysql_query("SELECT * FROM users WHERE login='$login'");
    $myrow = mysql_fetch_array($result);
    if (empty($myrow))
    {
		$_SESSION['info_msg'] = "Пользователь с таким логином и паролем не обнаружен.";
			header("Location: lab1.authorization.php");
			exit();
    }
    else {
		if ($myrow['password'] == $password_full_crypt) {
			$_SESSION['login'] = $myrow['login']; 
			$_SESSION['id'] = $myrow['id'];			
			header("Location: lab1.main.php");
			exit();
		}
		else {
			$_SESSION['info_msg'] = "Неверный пароль.";
			header("Location: lab1.authorization.php");
			exit();
		}
    }
?>