unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs;
  type
tinf=record
fio:string;
num:integer;
end;
tsel=^sel;
sel=record
inf:tinf;
a:tsel;
end;
ar=array[0..1] of tsel;
pa=^ar;
hesh=class(tobject)
sp,sp1:tsel;
m,n:integer;
h:pa;
procedure add(c:tinf);
function read(c:integer):tinf;
constructor create(m0:integer);
end;
implementation
constructor hesh.create;
var i:integer;
begin
inherited create;
getmem(h,4*m0);
m:=m0; n:=0;
for i:=0 to m-1 do
h[i]:=nil;
end;
procedure hesh.add;
var i:integer;
begin
i:=c.num mod m;
new(sp);
sp^.inf:=c;
sp^.a:=h[i];
h[i]:=sp;
inc(n);
end;
function hesh.read(c:integer):tinf;
var i:integer;
begin
i:=c mod m;
sp:=h[i];
while (sp<>nil) and (sp^.inf.num<>c) do begin
sp:=sp^.a; end;
if sp<>nil then result:=sp^.inf;
end;

end.
 