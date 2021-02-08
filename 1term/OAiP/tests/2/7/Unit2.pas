unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs;
type
rec=record
wes:integer;
cost:integer;
end;
mas=array[1..10] of rec;
solv=class(tobject)
a:mas;
wmax,cmax,wc,oct,n,wt,ct:integer;
s,opts:set of byte;
procedure mves;
end;
implementation
procedure solv.mves;
function find:integer;
var j,min:integer;
begin
min:=wmax;
for j:=1 to n do
if not (j in s) and (a[j].wes<min) then begin
min:=a[j].wes;
find:=j;
end;end;
var i,l:integer;
begin
i:=find;
l:=1;
while (wt+a[i].wes<=wmax) and (l<=n) do begin
wt:=wt+a[i].wes;  cmax:=cmax+a[i].cost; include(s,i);
i:=find; inc(l);
end;
end;
end.
