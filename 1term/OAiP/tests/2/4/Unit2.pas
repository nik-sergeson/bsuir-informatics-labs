unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs;
  type
  rec=record
  fio:integer;
  num:integer;
  end;
  mas=array[1..10] of rec;
  solv=class(tobject)
  a:mas;
  procedure sort(l,r:integer);
  end;
implementation
 procedure solv.sort;
 var i,j,m:integer;
 rc:rec;
 begin
 i:=l; j:=r; m:=(l+r) div 2;
while i<=j do begin
 while a[i].fio<a[m].fio do inc(i);
 while a[j].fio>a[m].fio do dec(j);
 if i<=j then begin
 rc:=a[i];
 a[i]:=a[j];
 a[j]:=rc;  inc(i); dec(j);
 end;
end;
 if l<j then sort(l,j);
 if i<r then sort (i,r);
 end;

end.
