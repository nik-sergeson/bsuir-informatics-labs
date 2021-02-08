<?php
    session_start();
?>
<html>
	<head>
		<title>Мунк Эдвард</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="Stylesheet" href="lab1.style.css" type="text/css" /> 
	</head>
	
	<body>
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
		<h2>Интересные факты</h2>
		<ol>

						
		</ol>
		<div class="pictures">
		<h2>Картины</h2>
		<table>
			<tr>
				<td><p>Крик 1893, Музей Мунка, Осло</p></td>
				<td class="picture"><img src="munch03.jpg" alt="Крик" title="Крик"></td>
			</tr>
			<tr>
				<td><p>Вампир 1897, Национальная галерея, Осло</p></td>
				<td class="picture"><img src="munch04.jpg" alt="Вампир" title="Вампир"></td>
			</tr>
			<tr>
				<td><p>Звездная ночь 1893, Музей Поля Гетти</p></td>
				<td class="picture"><img src="munch15.jpg" alt="Звездная ночь" title="Звездная ночь"></td>
			</tr>
			<tr>
				<td><p>Автопортрет с бутылкой вина 1906, Музей Мунка, Осло</p></td>
				<td class="picture"><img src="munch16.jpg" alt="Автопортрет с бутылкой вина" title="Автопортрет с бутылкой вина"></td>
			</tr>
		</table>
		</div>
	</body>
</html>