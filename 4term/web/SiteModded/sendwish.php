<?php
    session_start();
	
	$wish = $_POST['userwish'];
	$login=$_SESSION['login'];
	
    $wish = stripslashes($wish);
    $wish = htmlspecialchars($wish);

    include ("db.php"); 

	$result2 = mysql_query ("INSERT INTO wishes (login, wish) VALUES('$login','$wish')");
		if ($result2=='TRUE') {		
			$_SESSION['info_msg'] = "Пожелание принято";
			header("Location: lab1.wish.php");
			exit();
		} 
		else {
			$_SESSION['info_msg'] = "Неизвестная ошибка. Попробуйте позже.";
			header("Location: lab1.wish.php");
			exit();
		}
 
?>