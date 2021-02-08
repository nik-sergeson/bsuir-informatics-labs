unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs;
type
rec=record
i:integer;
n:integer;
end;
tmas=array[1..10] of rec;
solv=class(tobject)
key,ans:integer;
mas:tmas;
procedure psk(var mas:tmas;l,r:integer);
end;
implementation
procedure solv.psk;
var m:integer;
begin
if r<=l then ans:=r
else  begin
m:=(l+r) div 2;
if mas[m].i<key then psk(mas,m+1,r)
else psk(mas,l,m);
end;
end;
end.
