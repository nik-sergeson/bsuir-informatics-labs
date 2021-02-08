unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs;
type
rec=record
name:integer;
num:integer;
end;
mas=array[1..20] of rec;
tsolv=class(tobject)
a:mas;
procedure sort(l,r:integer);
end;
implementation
procedure tsolv.sort;
procedure sortslip(l,r,m:integer);
var i,k,j:integer;
c:mas;
begin
i:=l; j:=m+1; k:=1;
while (i<=m) and (j<=r) do
if a[i].name<a[j].name then
begin c[k]:=a[i]; inc(k); inc(i); end
else begin  c[k]:=a[j]; inc(k); inc(j); end;
while (i<=m) do begin
c[k]:=a[i]; inc(k); inc(i); end;
while (j<=r) do begin
c[k]:=a[j]; inc(k); inc(j); end;
k:=0;
for i:=l to r do begin
inc(k);
a[i]:=c[k];
end;
end;
var m:integer;
begin
if l<>r then begin
m:=(l+r) div 2;
sort(l,m);
sort(m+1,r);
sortslip(l,r,m);
end;
end;
end.
