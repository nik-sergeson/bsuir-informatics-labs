unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, ExtCtrls;
    type
  tteam=record
  FIO:string[40];
  str:string[40];
  tm:string[40];
  num:integer  ;
  age:integer ; //key
  rst:extended;
  ves:extended ;  end;
   tfile=file of tteam;

  bd=class(tobject)
  dim,ind:integer;
  key:integer;
  team:array[1..50] of tteam;
  procedure incfile(i:integer;bl:boolean;memo1:tmemo;var fz:tfile;edit1,edit2,edit3,edit4,edit5,edit6,edit7:tedit);
  procedure readfile(var fz:tfile;memo1:tmemo;bl:boolean);
  procedure mastofile(var ft:textfile);
  procedure linesearch(memo1:tmemo);
  procedure slsearch(l,r:integer);
  procedure qs(l,r:integer);
  procedure dsearch(memo1:tmemo);
  procedure del;
  procedure age(memo1:tmemo);

  end;

implementation
  procedure bd.incfile;
  begin
  dim:=i;
 with team[i] do begin
fio:=edit1.Text;
str:=edit2.Text;
tm:=edit3.Text;
num:=strtoint(edit4.Text);
age:=strtoint(edit5.Text);
rst:=strtofloat(edit6.Text);
ves:=strtofloat(edit7.Text);
if bl then begin
memo1.Lines.Add(inttostr(i)+' игрок');
memo1.Lines.Add('фио '+fio);
memo1.Lines.Add('страна '+str);
memo1.Lines.Add('команда '+tm);
memo1.Lines.Add('номер '+inttostr(num));
memo1.Lines.Add('возраст '+inttostr(age));
memo1.Lines.Add('рост '+floattostr(rst));
memo1.Lines.Add('вес '+floattostr(ves)); end; end;
write(fz,team[i]);
edit1.Clear;
edit2.Clear;
edit3.Clear;
edit4.Clear;
edit5.Clear;
edit6.Clear;
edit7.Clear;
end;
////////////////////////////////////////
procedure bd.readfile;
var nzap:integer;
begin
nzap:=0;
while not eof(fz) do begin
nzap:=nzap+1;
read(fz,team[nzap]);
if bl then begin
memo1.Lines.Add('----------------------------');
memo1.Lines.Add('фио '+team[nzap].fio);
memo1.Lines.Add('страна '+team[nzap].str);
memo1.Lines.Add('команда '+team[nzap].tm);
memo1.Lines.Add('номер '+inttostr(team[nzap].num));
memo1.Lines.Add('возраст '+inttostr(team[nzap].age));
memo1.Lines.Add('рост '+floattostr(team[nzap].rst));
memo1.Lines.Add('вес '+floattostr(team[nzap].ves)); end;
end;
dim:=nzap;
end;
procedure bd.mastofile;
var i:integer;
begin
for i:=1 to dim do
 with team[i] do  Writeln(Ft,i:4,'. ',fio,str,tm,num,age,rst,ves);

         CloseFile(Ft);
         end;
//////////////////////////////////
procedure bd.linesearch;
var i:integer;
begin
for i:=1 to dim do
if team[i].age=key then
with team[i] do begin
memo1.Lines.Add('фио '+fio);
memo1.Lines.Add('страна '+str);
memo1.Lines.Add('команда '+tm);
memo1.Lines.Add('номер '+inttostr(num));
memo1.Lines.Add('возраст '+inttostr(age));
memo1.Lines.Add('рост '+floattostr(rst));
memo1.Lines.Add('вес '+floattostr(ves));
end; end;
///////////////////////////////////////
procedure bd.slsearch;
procedure sliv(l,r,m:integer);
var i,j,k:integer;
c:array[1..100] of tteam;
begin
k:=1; i:=m+1; j:=l;
while (i<=r) and (j<=m) do
if team[i].age<team[l].age
then begin c[k]:=team[i]; inc(k); inc(i); end
else begin c[k]:=team[j]; inc(j); inc(k); end;
while (i<=r) do begin
c[k]:=team[i]; inc(k); inc(i); end;
while (j<=m) do begin
c[k]:=team[j]; inc(j); inc(k); end;
k:=0;	for i:=L to R do
		begin Inc(k); team[i]:=c[k] end; end;
var m:integer;
   begin
if l<>r then begin
m:=(l+r)div 2;
slsearch(l,m);
slsearch(m+1,r);
sliv(l,r,m);
end;  end;
/////////////////////////////////////////

 /////////////////////////////////
procedure bd.dsearch;
var i,j:integer;
function drob(l,r:integer):integer;
var m:integer;
begin
if r<=l then drob:=r
else begin
m:=(l+r) div 2;
if team[m].age<key then drob:=drob(m+1,r)
else drob:=drob(l,m);
end; end;
begin
j:=1;
while j<=dim do begin
i:=drob(j,dim);  j:=i+1;
if team[i].age=key then
with team[i] do begin
memo1.Lines.Add('----------------------------');
memo1.Lines.Add('фио '+fio);
memo1.Lines.Add('страна '+str);
memo1.Lines.Add('команда '+tm);
memo1.Lines.Add('номер '+inttostr(num));
memo1.Lines.Add('возраст '+inttostr(age));
memo1.Lines.Add('рост '+floattostr(rst));
memo1.Lines.Add('вес '+floattostr(ves)); end;
end; end;
////////////////////////////////
procedure bd.del;
var n,l,i:integer;
begin
i:=0;
for n:=1 to dim do
if team[n].age=key then begin
inc(i);
for l:=n to dim-1 do
team[l]:=team[l+1]; end;
dim:=dim-i;
end;
//////////////////////////////////
procedure bd.qs;
var v:tteam;
i,j,x,m:word;
begin
m:=(l+r)div 2;
i:=l;j:=r; x:=team[m].age;
while i<=j do
  begin
while team[i].age<x do i:=i+1;
while team[j].age>x do  j:=j-1;
if i<=j then begin
v:=team[i]; team[i]:=team[j];
team[j]:=v;
i:=i+1; j:=j-1;
 end;
end;
 if l<j then qs(l, j);
    if i<r then qs(i, r);
 end;
 //////////////////////////////////////
procedure bd.age;
var i,j,m,l,n,g,sum:integer;
s:tteam; max,sr:extended;
str:string;
begin
for i:=1 to dim-1 do begin
m:=i;
for j:=i+1 to dim do
if team[j].tm<team[i].tm then m:=j;
s:=team[i];
team[i]:=team[m];
team[m]:=s;
end;
sr:=0; n:=1; sum:=team[1].age;  max:=team[1].age;
for g:=1 to dim do
if team[g].age> max then
max:=team[g].age;
for l:=2 to dim do
if team[l].tm=team[l-1].tm then begin
inc(n); sum:=sum+team[l].age; end
else begin
sr:=sum/n; n:=1; sum:=team[l].age;
if sr<max then  begin str:=team[l-1].tm; max:=sr; end;
end;
memo1.lines.add('самая молодая команда-'+str+'с возрастом'+floattostr(max));
end;

end.

