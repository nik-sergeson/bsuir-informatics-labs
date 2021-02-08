var
	X:array [1..100] of integer;
	Y:array [1..10] of integer;
	i,j:integer;
begin 
	writeln('Enter 100 elements');
	for i:=1 to 100 do
		readln(Y[i]);
	j:=1;
	for i:=1 to 100 do begin
		if j>10 then
			break;
		if X[i]>15 then  begin
			Y[j]:=i;
			j:=j+1;
		end;
	end;
	if(Y[10]=0) then 
		writeln('Таких значений больше нет');
	else if(Y[1]=0) then
		writeln('Таких значений нет');
	else begin
		for i=1 to 10 do
			writeln(i,' ',X[i]);
	end;
end.