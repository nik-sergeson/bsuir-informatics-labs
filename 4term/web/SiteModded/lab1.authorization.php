<?php
    session_start();
?>
<html>
	<head>
		<title>Вход на сайт</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="Stylesheet" href="lab1.style.css" type="text/css" /> 
	</head>
	<body>
	<ul class="regbutt">
			<li><a href="lab1.registration.php">Регистрация</a></li>
	</ul>
	<ul class="menu">
		<li><a href="lab1.main.php">Главная</a></li>
		<li><a href="lab1.munch.php">Мунк Эдвард</a></li>
		<li><a href="lab1.vangogh.php">Ван Гог </a></li>
	</ul>
	<div>
		<?php if (!empty($_SESSION['info_msg'])) {														
			echo ($_SESSION['info_msg']);
			unset($_SESSION['info_msg']);
			}
		?>	
	</div>
	<div class="userbar">
		<?php
		if (!empty($_SESSION['login'])) {
			echo ("Вы вошли как: ");
			?>
			<a href="lab1.office.php"><?php echo($_SESSION['login']); ?>
			<a href="exit.php">(Выход)</a>
			<?php
		}
		?>
	</div>
	<form name="Auth" onSubmit="authGuest(); return(false);" action="auth.php" method="post">
	<P> Ввведите имя: 
	<INPUT NAME="login"></p>
	<P> Ввведите пароль:
	<INPUT TYPE="password" NAME="password"></p>
	<p><input type="submit" value="Войти" name="submit"></p>
	</form>
	<script type="text/javascript">
	function authGuest() {
		obj_form=document.forms.Auth;
		obj_pole_name =obj_form.login;
		obj_pole_fpas =obj_form.password;
		if (obj_pole_name.value==""||obj_pole_fpas.value==""){ 
			alert ("Все поля должны быть заполнены!"); 
			return;
		}
		obj_form.submit();
	}
	</script>
	</body>
</html>