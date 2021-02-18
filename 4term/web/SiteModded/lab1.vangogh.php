<?php
    session_start();
?>
<html>
	<head>
		<title>Винсент Ван Гог</title>
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
				<td><p>Лодки в Сен-Мари, 1888 Музей ван Гога, Амстердам</p></td>
				<td class="picture"><img src="van_gogh01.jpg" alt="Лодки в Сен-Мари" title="Лодки в Сен-Мари"></td>
			</tr>
			<tr>
				<td><p>Ирисы, 1890 Музей ван Гога, Амстердам</p></td>
				<td class="picture"><img src="van_gogh02.jpg" alt="Ирисы" title="Ирисы"></td>
			</tr>
			<tr>
				<td><p>Подсолнухи, 1888 Новая Пинакотека, Мюнхен</p></td>
				<td class="picture"><img src="van_gogh03.jpg" alt="Подсолнухи" title="Подсолнухи"></td>
			</tr>
			<tr>
				<td><p>Мост де л'Англуа, 1888 Частное собрание, Берлин</p></td>
				<td class="picture"><img src="van_gogh9.jpg" alt="Мост де л'Англуа" title="Мост де л'Англуа"></td>
			</tr>
		</table>
		</div>
	</body>
</html>