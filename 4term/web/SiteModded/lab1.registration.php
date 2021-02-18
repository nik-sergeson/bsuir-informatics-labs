<?php
    session_start();
?>
<html>
	<head>
		<title>Регистрация нового пользователя</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="Stylesheet" href="lab1.style.css" type="text/css" /> 
	</head>
	<body>
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
	<form name="Guest" onSubmit="provGuest(); return(false);" action="save_user.php" method="post">
	<P> Ввведите имя: 
	<INPUT NAME="login"></p>
	<P> Ввведите пароль:
	<INPUT TYPE="password" NAME="fpassw"></p>
	<P> Повторите пароль:
	<INPUT TYPE="password" NAME="spassw"></p>
	<P> Ввведите адрес электронной почты: 
	<INPUT NAME="email"></p>
	<p>Ваш любимый художник?</p>
	<p><input type="radio" name="answer" value="a1">Эдвард Мунк
	<input type="radio" name="answer" value="a2">Винсент ван Гог</p>
	<p><input type="submit" value="Отправить" name="submit"></p>
	</form>
	<script type="text/javascript">
	function provGuest() {
		obj_form=document.forms.Guest;
		obj_pole_name =obj_form.login;
		obj_pole_fpas =obj_form.fpassw;
		obj_pole_spasw =obj_form.spassw;
		obj_pole_email =obj_form.email;	
		if (obj_pole_name.value==""||obj_pole_email.value==""){ 
			alert ("Все поля должны быть заполнены!"); 
			return;
		}
		txt = obj_pole_email.value;
		if (obj_form.fpassw.value!=obj_form.spassw.value){ 
			alert ("Пароли не совпадают!");
			return;
		}
		if (obj_form.fpassw.value.length<6){ 
			alert ("Слишком короткий пароль!Нужно минимум 6 символов");
			return;
		}
		if (!(/[0-9a-z_]+@[0-9a-z_]+\.[a-z]{2,5}/i.test(obj_pole_email.value))){ 
			alert ("Напишите Ваш E-mail вида name@yandex.ru!");
			return;
		}
		var n=0;   
		var art = document.getElementsByName('answer');
		for (i = 0; i < art.length; i++) {
			if(art[i].checked == true){
				n++;
			}
			
		} 
		if(n==0){
			alert( "Вы не отметили художника" );
			return;
		}
		obj_form.submit();
	}
	</script>
	</body>
</html>