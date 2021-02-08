var
	ina:array[1..10] of integer;
    outa:array[0..10] of integer;
	i,pos,temp:integer;
begin
	{устанавка начального значения счетчика цикла}
	i:=1;
	{ввода значений элементов массива}
	while i<=10 do begin
		read(ina[i]);
		outa[i]:=ina[i];
		i:=i+1;
	end;
    outa[0]:=outa[10];
	{устанавка начального значения счетчика цикла}
	i:=10;
	{цикл перемещения послденего элемента в позицию, где он не нарушает упорядоченность массива}
	while outa[i]<outa[i-1] do begin
		temp:=outa[i];
		outa[i]:=outa[i-1];
		outa[i-1]:=temp;
		i:=i-1;
	end;
	pos:=i;
	{устанавка начального значения счетчика цикла}
	i:=1;
	{вывод значений на экран}
	while i<=10 do begin
		write(ina[i],' ');
		i:=i+1;
	end;
	writeln();
	{устанавка начального значения счетчика цикла}
	i:=1;
	{вывод значений на экран}
	while i<=10 do begin
		write(outa[i],' ');
		i:=i+1;
	end;
	writeln();
	{вывод позиции перемещенного элемента}
	writeln(pos);
	read();
	end.
