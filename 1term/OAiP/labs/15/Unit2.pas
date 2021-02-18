unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;
type
tsel=^sel;
sel=record
dig:integer;
a:tsel;
end;
tstr=^str;
str=record
s:string;
a:tstr;
end;
stack=class(tobject)
sp1,sp:tsel;
ssp1,ssp:tstr;
ssp1n,sspn:tstr;
key,p,lp,dim:integer;
procedure add(i:integer);
procedure read(var i:integer);
procedure print(l:tlistbox);
procedure readafter(var i:integer;l:integer);
procedure addafter(i,l:integer);
constructor create;
procedure finda(i:integer; var sp2:tsel);
procedure lfind(l:tlistbox;var sp2:tsel);
procedure bubl;
procedure bubls;
procedure del;
procedure str(list:tlistbox);
procedure strsort(list:tlistbox);
end;
implementation
constructor stack.create;
begin
inherited create;
sp1:=nil;
end;
procedure stack.add;
begin
new (sp);
sp^.dig:=i;
sp^.a:=sp1;
sp1:=sp;
end;
procedure stack.read;
begin
i:=sp1^.dig;
sp:=sp1;
sp1:=sp1^.a;
dispose(sp);
end;
procedure stack.print;
var i:integer;
begin
sp:=sp1;
for i:=1 to dim do begin
l.Items.Add(inttostr(sp^.dig));
sp:=sp^.a;
end;end;
procedure stack.finda;
var k:integer;
begin
k:=1;sp:=sp1;
while k<i do begin
sp2:=sp^.a;
inc(k); sp:=sp^.a;
end; end;
procedure stack.addafter;
var spi:tsel;
begin
new(sp);
finda(l,spi);
sp^.dig:=i;
sp^.a:=spi^.a;
spi^.a:=sp;
end;
procedure stack.readafter;
var spi:tsel;
begin
finda(l,spi);
sp:=spi^.a;
i:=sp^.dig;
spi^.a:=sp^.a;
dispose(sp);
end;
procedure stack.lfind;
begin
if sp1^.a<>nil then begin
sp2:=sp1;
while (sp2^.dig<>key)and (sp2^.a<>nil)do begin
sp2:=sp2^.a;
end; end;
if sp2^.dig=key then l.Items.Add('find')
 end;
procedure stack.bubl;
procedure change(var sp:tsel);
var i:integer;
begin
i:=sp^.dig;
sp^.dig:=sp^.a^.dig;
sp^.a^.dig:=i
end;
var spt:tsel;
begin
spt:=nil;
repeat
sp:=sp1;
while (sp^.a<>spt) do begin
if sp^.dig>sp^.a^.dig then change(sp);
sp:=sp^.a;
end;
spt:=sp;
until sp1^.a=sp;
end;
 procedure stack.del;
 begin
if sp1<>nil then
repeat
 sp:=sp1;
 sp1:=sp1^.a;
 dispose(sp);
 until sp1^.a=nil
 end;
procedure stack.str;
var m,i,l,g,w:integer;
begin
if p<>0 then begin
for m:=1 to p do begin
ssp:=ssp1;
ssp1:=ssp1^.a;
dispose(ssp); end; end;
ssp1:=nil;
list.Clear;
p:=random(8)+2;
for i:=1 to p do begin
new(ssp);
w:=random(8)+2;
for g:=1 to w do begin
l:=random(100)+20;
ssp^.s:=ssp^.s+inttostr(l); end;
ssp^.a:=ssp1;
ssp1:=ssp;
list.Items.Add(ssp^.s)
end;
end;
procedure stack.bubls;
procedure change(var sspn:tstr);
var i:string;
begin
i:=sspn^.s;
sspn^.s:=sspn^.a^.s;
sspn^.a^.s:=i
end;
var spt:tstr;
begin
spt:=nil;
repeat
sspn:=ssp1n;
while (sspn^.a<>spt) do begin
if length(sspn^.s)>length(sspn^.a^.s) then change(sspn);
sspn:=sspn^.a;
end;
spt:=sspn;
until ssp1n^.a=sspn;
end;
procedure stack.strsort;
var i,m:integer;
e:string;
begin
if lp<>0 then
if sp1<>nil then
repeat
 sspn:=ssp1n;
 ssp1n:=ssp1n^.a;
 dispose(sspn);
 until ssp1n^.a=nil;
ssp1n:=nil; ssp:=ssp1;
for i:=1 to p do begin
new(sspn);
sspn^.a:=ssp1n;
ssp1n:=sspn;
sspn^.s:=ssp^.s;
ssp:=ssp^.a;
end;
bubls;
list.Clear;
sspn:=ssp1n;
while (sspn<>nil) do begin
list.Items.Add((sspn^.s));
sspn:=sspn^.a;
end;
lp:=p;
end;
end.
