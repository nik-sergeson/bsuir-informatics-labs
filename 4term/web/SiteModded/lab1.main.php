<?php
    session_start();
?>

<html>
  <head>
    <title>Экспрессионизм в живописи</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="Description" content="Сайт посвященный экспрессионизму в живописи<">
	<link rel="Stylesheet" href="lab1.style.css" type="text/css" /> 
	<script type="text/javascript" src="script.js"></script>
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
<div id="wrapper">
	<div id="container">
		<div class="sliderbutton" id="slideleft" onclick="slideshow.move(-1)"></div>
		<div id="slider">
			<ul>
				<li class="sliderpic"><img src="slider/02.jpg" width="500" height="300" /></li>
				<li class="sliderpic"><img src="slider/03.jpg" width="500" height="300" /></li>
				<li class="sliderpic"><img src="slider/04.jpg" width="500" height="300" /></li>
				<li class="sliderpic"><img src="slider/05.jpg" width="500" height="300" /></li>
				<li class="sliderpic"><img src="slider/06.jpg" width="500" height="300" /></li>
				<li class="sliderpic"><img src="slider/08.jpg" width="500" height="300" /></li>
				<li class="sliderpic"><img src="slider/09.jpg" width="500" height="300"/></li>
			</ul>
		</div>
		<div class="sliderbutton" id="slideright" onclick="slideshow.move(1)"></div>
		<ul id="pagination" class="pagination">
			<li onclick="slideshow.pos(0)"></li>
			<li onclick="slideshow.pos(1)"></li>
			<li onclick="slideshow.pos(2)"></li>
			<li onclick="slideshow.pos(3)"></li>
			<li onclick="slideshow.pos(4)"></li>
			<li onclick="slideshow.pos(5)"></li>
			<li onclick="slideshow.pos(6)"></li>
		</ul>
	</div>
</div>
<script type="text/javascript">
var slideshow=new TINY.slider.slide('slideshow',{
	id:'slider',
	auto:4,
	resume:false,
	vertical:false,
	navid:'pagination',
	activeclass:'current',
	position:0,
	rewind:false,
	elastic:true,
	left:'slideleft',
	right:'slideright'
});
</script>
	<h2>Экспрессионизм в живописи</h2>
		
	</body>
</html>
