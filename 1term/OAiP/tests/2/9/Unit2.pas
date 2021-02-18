unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs;
type
rec=record
num:integer;
fio:string;
end;
tsel=^sel;
sel=record
inf:rec;
a:tsel;
end;
tspis=class(tobject)
sp,sp1,spk:tsel;
procedure addk(inf:rec);
procedure read(var inf:rec);
constructor create;
procedure sort(tp:tspis);
end;
implementation
constructor tspis.create;
begin
inherited create;
sp:=nil;
spk:=nil;
end;
procedure tspis.addk;
begin
     New(sp);
     sp^.A:=Nil;
     sp^.Inf:=inf;
	 if sp1=Nil then begin		
	                 spk:=sp; sp1:=sp; 
		           end
                else
	 begin spk^.A:=sp;  spk:=sp; end;
  end;
procedure tspis.read;
begin
inf:=sp1^.inf;
sp:=sp1;
sp1:=sp1^.a;
  if sp1=Nil then spk:=Nil;
dispose(sp);
end;
procedure tspis.sort;
procedure divi(tp:tspis;var tq,tr:tspis);
var c:rec;
b:integer;
begin
tr:=tspis.create;
tq:=tspis.create;
b:=-1;
while tp.sp1<>nil do begin
b:=-b;
tp.read(c);
if b>0 then tr.addk(c)
else tq.addk(c);
end; end;
procedure slip(var tp,tq,tr:tspis);
var c:rec;
begin
while (tq.sp1<>nil) and (tr.sp1<>nil) do
if tq.sp1.inf.num<tr.sp1.inf.num then
begin
tq.read(c);  tp.addk(c); end
else begin
tr.read(c);  tp.addk(c);
end;
while (tq.sp1<>nil) do begin
tq.read(c); tp.addk(c); end;
while (tr.sp1<>nil) do begin
tr.read(c); tp.addk(c); end;
end;
var tq,tr:tspis;
begin
if tp.sp1<>tp.spk then begin
divi(tp,tq,tr);
sort(tq);
sort(tr);
slip(tp,tq,tr);
end; end;
end.
