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
procedure vg(i,wt,oct:integer);
end;
implementation
procedure solv.vg;
var j,k,oct1,wt1:integer;
begin
wt1:=wt+a[i].wes;
if (wt1<=wmax) then begin
include(opts,i);
if i<n then vg(i+1,wt1,oct)
else
if oct>cmax then begin s:=opts; cmax:=oct; end;
exclude(opts,i); end;
oct1:=oct-a[i].cost;
if oct1>cmax then
if i<n then
vg(i+1,wt,oct1)
else begin
s:=opts; cmax:=oct1;
end;
end;
end.
