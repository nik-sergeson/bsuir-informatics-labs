unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Grids;
   Type
      Mas=array[1..1] of integer;
    pmas=^mas;
procedure del(var a:pmas;var n,n1:integer);

implementation
procedure del;
var k,i,j:integer;
begin
k:=0;
for i:=1 to n do
if odd(a[i]) then begin
inc(k);
a[k]:=a[i];
end;
n1:=k;
end;
end.
