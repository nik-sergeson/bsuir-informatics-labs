unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, Grids;
type
tinf=record
fio:string;
num:integer;
end;
tsel=^sel;
sel=record
inf:tinf;
a1,a2:tsel;
end;
solv=class(tobject)
proot,w,sp,p:tsel;
a:array[0..10] of tinf;
procedure add(c:tinf);
procedure blns(i,j:integer);
procedure poisk;
constructor create;
end;
implementation
uses unit1;
constructor solv.create;
begin
inherited create;
proot:=nil;
end;
procedure solv.add;
var bl:boolean;
begin
new(sp);
sp^.inf:=c;
sp^.a1:=nil;
sp^.a2:=nil;
if proot=nil
then proot:=sp
else begin
p:=proot;
repeat
w:=p;
bl:=c.num<p^.inf.num;
if bl
then p:=p^.a1
else p:=p^.a2;
until p=nil;
if bl then w^.a1:=sp
else w^.a2:=sp;
end; end;
procedure solv.blns;
var m:integer;
begin
if i<=j then begin
m:=(i+j) div 2;
add(a[m]);
blns(i,m-1);
blns(m+1,j);
end;end;
procedure solv.poisk;
begin
p:=proot;
while (p^.a1<>nil)  do begin
p:=p^.a1
end;
form1.memo1.Lines.Add(inttostr(p^.inf.num)+'    '+p^.inf.fio);
end;
end.
 