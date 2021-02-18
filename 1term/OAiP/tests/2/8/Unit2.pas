unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, Grids;
type
  tsel=^sel;
  rec=record
  num:integer;
  fio:string;
  end;
  sel=record
  inf:rec;
  a:tsel;
  end;
  solv=class(tobject)
  sp,sp1:tsel;
  dim:integer;
  procedure add(inf:rec);
  procedure read(var inf:rec);
  procedure sort;
  constructor create;
  end;
implementation
constructor solv.create;
begin
inherited create;
new(sp1);
sp1^.a:=nil;
end;
procedure solv.add;
begin
new(sp);
sp^.inf:=inf;
sp^.a:=sp1^.a;
sp1^.a:=sp;
end;
 procedure solv.read;
 begin
 inf:=sp1^.a^.inf;
 sp:=sp1^.a;
 sp1^.a:=sp1^.a^.a;
 dispose(sp);
 end;
 procedure solv.sort;
 procedure rev(spi:tsel);
 var sp:tsel;
 begin
 sp:=spi^.a^.a;
 sp^.a:=spi^.a;
 spi^.a^.a:=sp^.a;
 spi^.a:=sp;
 end;
 var spt:tsel;
 begin
 spt:=nil;
 repeat
 sp:=sp1^.a;
 while (sp^.a^.a<>spt) do begin
 if sp^.a^.inf.num>sp^.a^.a^.inf.num then rev(sp);
 sp:=sp^.a; end;
 spt:=sp^.a;
 until sp1^.a^.a=spt;
 end;
end.
