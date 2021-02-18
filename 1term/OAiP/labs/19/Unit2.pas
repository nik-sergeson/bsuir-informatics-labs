unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, Grids;

type
tinf=record
fio:string;
num:integer;
end;

tsel=^sel;
sel=record
inf:tinf;
a:tsel;
end;
mas=array[0..1] of tsel;
pmas=^mas;
hesh=class(tobject)
n,m:integer;
h:pmas;
sp,sp1:tsel;
procedure add(inf:tinf);
constructor create(m0:integer);
Destructor Free(var sgrid:Tstringgrid);
function read(key:integer):tinf;
function Readd(key:integer):tinf;
procedure print(me:tmemo);
procedure solv(me:tmemo);
end;
implementation
constructor hesh.create;
var i:integer;
begin
inherited create;
m:=m0; n:=0;
getmem(h,m*4);
for i:=0 to m-1 do
h[i]:=nil;
end;
Destructor Hesh.Free;
var i,j:word;
     begin j:=0;
        for i:=0 to M-1 do begin
            While H[i]<>Nil do
                     begin Inc(j);
                           sp:=H[i];
    SGrid.Cells[0,j]:=sp^.inf.Fio;
    SGrid.Cells[1,j]:=IntToStr(sp^.inf.num);
                           H[i]:= H[i]^.A;
                           dispose(sp);
				end;
                            end;
      FreeMem(H,4*M); n:=0;
      Inherited Free;
    end;

procedure hesh.add;
var i:integer;
begin
i:=inf.num mod m;
new(sp); inc(n);
sp^.inf:=inf;
sp^.a:=h[i];
h[i]:=sp;
end;
function hesh.read(key:integer):tinf;
var i:integer;
begin
i:=key mod m;
sp:=h[i];
while(sp<>nil) and (sp^.inf.num<>key) do
sp:=sp^.a;
if sp<>nil then result:=sp^.inf;
end;

function hesh.Readd(key:integer):tinf;
   var i:integer;
     begin
      i:=key mod m;
      sp:=H[i]; 
 if sp=Nil then ShowMessage('ключ не найден')
           else 
 begin
    if sp^.inf.num=key
    then begin Result:=sp^.inf;
     H[i]:=H[i].A; dispose(sp); Dec(n); end
    else 
 Begin
 While (sp.A<>Nil) and (sp.A.inf.num<>key)
    do  sp:=sp^.A;
      if sp.A<>Nil then begin
                         Result:=sp.A.inf;
                         sp1:=sp.A; 
                         sp.A:=sp.A.A;
                         dispose(sp1); Dec(n);
                       end
      else ShowMessage('ключ не найден');
end;
End;
end;
procedure hesh.print;
var i:integer;
s:string;
begin
me.Clear;
for i:=0 to m-1 do begin
sp:=h[i]; s:='';
while sp<>nil do begin
s:=s+' '+sp^.inf.fio;
sp:=sp^.a;
end;
me.Lines.Add(s);
end;
end;
procedure hesh.solv;
var i,cnt:integer;
sred:extended;
begin
sred:=0; cnt:=0;
for i:=0 to m-1 do begin
sp:=h[i];
while sp<>nil do  begin
sred:=sred+sp^.inf.num;
sp:=sp^.a; end; end;
sred:=sred/n;
for i:=0 to m-1 do begin
sp:=h[i];
while sp<>nil do  begin
if sp^.inf.num>sred then inc(cnt);
sp:=sp^.a;
end;    end;
me.Lines.Add(inttostr(cnt));
end;
end.
