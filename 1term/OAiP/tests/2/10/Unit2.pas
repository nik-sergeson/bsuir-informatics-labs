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
function av(str:string):extended;
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

function stack.av(str:string):extended;
var ch,ch1,ch2,chr:char;
op1,op2,rez:extended;
i:integer;
begin
chr:=succ('z');
for i:=1 to length(str) do begin
ch:=str[i];
if not (ch in ['/','*','-','+','^']) then
add(ch)
else begin
read(ch2); read(ch1);
op1:=a[ch1]; op2:=a[ch2];
case ch of
'/':rez:=op1/op2;
'*':rez:=op1*op2;
'-':rez:=op1-op2;
'+':rez:=op1+op2;
'^':rez:=power(op1,op2);
end;
a[chr]:=rez; add(chr); inc(chr);
end; end;
result:=rez;
end;
end.
