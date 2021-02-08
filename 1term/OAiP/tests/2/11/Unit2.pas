unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls,math;

type
tsel=^sel;
sel=record
ch:char;
a:tsel;
end;
stack=class(tobject)
sp,sp1:tsel;
a:array['a'..'я'] of extended;
procedure add(i:char);
procedure read(var i:char);
procedure obr(str:string;var stri:string);
constructor create;
end;
implementation
constructor stack.create;
begin
inherited create;
sp1:=nil;
end;

procedure stack.add;
begin
new(sp);
sp^.ch:=i;
sp^.a:=sp1;
sp1:=sp;
end;

procedure stack.read;
begin
i:=sp1^.ch;
sp:=sp1;
sp1:=sp1^.a;
dispose(sp);
end;

procedure stack.obr;
function prior(ch:char):integer;
begin
case ch of
'(',')':prior:=0;
'+','-':prior:=1;
'*','/':prior:=2;
'^':prior:=4;
end; end;
var i,pr:integer;
ch,ch1:char;
begin
stri:='';
for i:=1 to length(str) do begin
ch:=str[i];
if not (ch in ['/','*','-','+','^']) then
stri:=stri+ch
else
if sp1=nil then
add(ch)
else if ch='(' then
add(ch)
else if ch=')' then begin
read(ch1);
while ch1<>'(' do begin
stri:=stri+ch1;
read(ch1); end; end
else begin
pr:=prior(ch);
while (sp1<>nil) and (pr<=prior(sp1^.ch)) do begin
read(ch1);
stri:=stri+ch1;
end;
add(ch)
end; end;
while sp1<>nil do begin
read(ch1);
stri:=stri+ch1;
end; end;
end.
