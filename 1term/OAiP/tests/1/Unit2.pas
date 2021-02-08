unit unit2;

interface
uses stdctrls, sysutils;
type
fun=function(x:extended):extended;
procedure tabl(f,o:fun;xn,xk,e:extended;m:integer;mem1:tmemo);
procedure tabl1(f:fun;xn,xk,e:extended;m:integer;mem1:tmemo);
implementation
procedure tabl;
var x,y,h,l,g:extended; i,toc:integer;
begin
x:=xn;
h:=(xk-xn)/m;
toc:=0;
l:=e;
while (l<1) do begin
l:=l*10;
toc:=toc+1; end;
for i:=1 to m+1 do begin
y:=f(x); g:=o(x);
mem1.lines.add('x='+floattostr(x)+'   y='+
floattostrf(y,fffixed,8,toc)+'   n='+
floattostr(g));
x:=x+h;
end;
end;
procedure tabl1;
var x,y,h,l,g:extended; i,toc:integer;
begin
x:=xn;
h:=(xk-xn)/m;
toc:=0;
l:=e;
while (l<1) do begin
l:=l*10;
toc:=toc+1; end;
for i:=1 to m+1 do begin
y:=f(x);
mem1.lines.add('x='+floattostr(x)+'   y='+
floattostrf(y,fffixed,8,toc));
x:=x+h;
end;
end;
end.