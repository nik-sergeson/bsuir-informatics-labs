<?php
    session_start();
?>
<html>
	<head>
		<link rel="stylesheet" href="lab1.style.css" type="text/css" >
		<title>Художники-экспрессионисты</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<script type="text/javascript" src="script.js"></script>
		<script src="jquery-1.11.1.js" type="text/javascript"></script>
		<script src="LoadData.js" type="text/javascript"></script>
	</head>
	<body>
	<h2 align="center"><a>Художники-экспрессионисты</a></h2>
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
		<table class="itemtableheader">
			<tr>
				<td class="itemid">ID</td>
				<td class="itemname">Имя</td>
				<td class="itemy">Произведения</td>
			</tr>
		</table>
	</div>
	<div id="dyntable"></div>
	</body>
</html>