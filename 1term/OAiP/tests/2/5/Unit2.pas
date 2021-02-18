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
wmax,cmax,wc,n:integer;
s,opts:set of byte;
procedure pp(i:integer);
end;
implementation
procedure solv.pp;
var j,wt,ct,k:integer;
begin
for j:=0 to 1 do begin
if j=0 then include(opts,i)
else exclude(opts,i);
if i<n then pp(i+1)
else begin
wt:=0; ct:=0;
for k:=1 to n do
if (k in opts) then  begin
wt:=wt+a[k].wes;
ct:=ct+a[k].cost;  end;
if (wt<=wmax) and (ct>cmax) then begin
s:=opts; cmax:=ct; wc:=wt;
end; end; end;  end;
end.
