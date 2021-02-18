<?php
    session_start();
	unset($_SESSION['login']);
	unset($_SESSION['id']);

	header("Location: lab1.main.php");
	exit;
?>