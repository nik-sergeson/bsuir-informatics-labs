<?php
    session_start();
	
	$login = $_POST['login'];
	$password=$_POST['fpassw'];
	$email=$_POST['email'];
	$answer=$_POST['answer'];
	
    $login = stripslashes($login);
    $login = htmlspecialchars($login);	
    $answer = stripslashes($answer);
    $answer = htmlspecialchars($answer);
	$password = stripslashes($password);
    $password = htmlspecialchars($password);
	$email = stripslashes($email);
    $email = htmlspecialchars($email);		
    $login = trim($login);	
    $password = trim($password);	
	$password = md5(md5("pass".$password)."word");	
    include ("db.php"); 
	$result = mysql_query("SELECT * FROM users WHERE login='$login'");
    $myrow = mysql_fetch_array($result);
    if (!empty($myrow))
    {
			$_SESSION['info_msg'] = "Извините, введённый вами логин уже зарегистрирован.";
			header("Location: lab1.registration.php");
			exit();
    }
    else {
		if($answer=='a1'){
			$result2 = mysql_query ("INSERT INTO users (login, password, email, drawer) VALUES('$login','$password','$email','Эдвард Мунк')");
		}
		else{
			$result2 = mysql_query ("INSERT INTO users (login, password, email, drawer) VALUES('$login','$password','$email','Винсент ван Гог')");
		}
		if ($result2=='TRUE') {
			$_SESSION['login'] = $login; 			
			header("Location: lab1.main.php");
			exit();
		} 
		else {
			$_SESSION['info_msg'] = "Неизвестная ошибка. Попробуйте зарегистривроваться позже.";
			header("Location: lab1.registration.php");
			exit();
		}
    }
?>