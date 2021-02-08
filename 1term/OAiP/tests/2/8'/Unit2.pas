unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, Grids;
  type
  rec=record
  num:integer;
  fio:integer;
  end;
  tmas=array[1..1] of rec;
  pmas=^tmas;
  solv=class(tobject)
  a,a1:pmas;
  n1,mt:integer;
  procedure addlast(elem:rec);
  procedure read1(var elem:rec);
  procedure update(str:TStringGrid);
  constructor create;
  end;
implementation
  constructor solv.create;
  begin
  mt:=sizeof(rec);
  n1:=0;
  end;
  procedure solv.addlast;
  var i:integer;
  begin
  getmem(a1,(n1+1)*mt);
  n1:=n1+1;
  a1[n1]:=elem;
  if a<>nil then begin
  for i:=1 to n1-1 do
  a1[i]:=a[i];
  freemem(a,(n1-1)*mt); end;
  a:=a1;
  end;
  procedure solv.read1;
  var i:integer;
  begin
  getmem(a1,(n1-1)*mt);
  n1:=n1-1;
  elem:=a[1];
  for i:=1 to n1 do
  a1[i]:=a[i+1];
  freemem(a,(n1+1)*mt);
  a:=a1;
  end;
  procedure solv.update;
  var i:integer;
  begin
  str.rowcount:=n1+1;
  str.colcount:=2;
  for i:=1 to n1 do begin
  str.cells[0,i]:=inttostr(a[i].num);
  str.cells[1,i]:=inttostr(a[i].fio);
  end; end;

  end.
