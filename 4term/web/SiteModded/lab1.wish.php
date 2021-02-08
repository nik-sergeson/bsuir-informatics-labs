<?php
    session_start();
	if (!isset($_SESSION['login'])) {
		header("Location: lab1.main.php");
	exit();		
	}
?>
<html>
	<head>
		<link rel="stylesheet" href="lab1.style.css" type="text/css" >
		<title>Отправить пожелание</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	</head>
	<body>
	<div>
	<div class="userbar">
		<?php
		if (!empty($_SESSION['login'])) {
			echo ("Вы вошли как: ");
			?>
			<a href="lab1.office.php"><?php echo($_SESSION['login']); ?>
			<a href="exit.php">(Выход)</a>
			<?php
		}
		else{
		?>
		<ul class="regbutt">
			<li><a href="lab1.registration.php">Регистрация</a></li>
			<li><a href="lab1.authorization.php">Вход</a></li>
		</ul>
		<?php
		}
		?>
	</div>
	<ul class="menu">
		<li><a href="lab1.main.php">Главная</a></li>
		<li><a href="lab1.munch.php">Мунк Эдвард</a></li>
		<li><a href="lab1.vangogh.php">Ван Гог</a></li>
		<li><a href="lab1.artists.php">Хужожники</a></li>
		<?php
			if (!empty($_SESSION['login'])) {?>
			<li><a href="lab1.wish.php">Пожелания</a></li>
			<?php
			}
		?>
	</ul>
		<?php if (!empty($_SESSION['info_msg'])) {														
			echo ($_SESSION['info_msg']);
			unset($_SESSION['info_msg']);
			}
		?>	
	</div>
	<div>
		 <form name="Wish" action="sendwish.php" method="post">
			<p><b>Введите ваш отзыв:</b></p>
			<p><textarea name="userwish" rows="5" cols="45" name="text"></textarea></p>
		<p><input type="submit" value="Отправить"></p>
  </form>

	</div>
</html>