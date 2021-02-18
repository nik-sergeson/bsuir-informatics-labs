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
procedure add(c:tinf);
procedure write;
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
procedure solv.write;
procedure wrt(p:tsel;i:integer);
begin
if p<>nil then begin
wrt(p^.a1,i+1);
form1.stringgrid2.cells[i,0]:=inttostr(p^.inf.num);
wrt(p^.a2,i+1);
end;
end;
begin
p:=proot;
wrt(p,0);
end;
end.
 