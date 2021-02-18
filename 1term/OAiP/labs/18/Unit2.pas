unit Unit2;

interface

uses  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ComCtrls, StdCtrls, Buttons, Grids;

type
tinf=record
fio:string;
num:integer;
end;
ttree=^tree;
tree=record
inf:tinf;
a1,a2:ttree;
end;
solv=class(tobject)
proot,p,q,v,w:Ttree;
n:integer;
bl:boolean;
a:array[1..100] of tinf;
constructor create;
procedure wrt1;
procedure add(inf:tinf);
procedure blns(n:integer);
procedure del(i:integer);
procedure view;
procedure Delete(p:ttree);
procedure left;
end;
implementation
uses unit1;
constructor solv.create;
begin
inherited create;
proot:=nil;
end;
//////////////////////////
procedure solv.wrt1;
procedure wr(p:ttree);
begin
if p<>nil then begin
Form1.Memo1.Lines.Add(p^.Inf.fio+IntToStr(p^.Inf.num));
wr(p^.a1);
wr(p^.a2);
end; end;
begin
p:=proot; wr(p);
end;
/////////////////////////
procedure solv.add;
var bl:boolean;
begin
new(w);
w^.inf:=inf;
w^.a1:=nil;
w^.a2:=nil;
if proot= nil
then proot:=w
else begin
p:=proot;
repeat
q:=p;
bl:=inf.num<p^.inf.num;
if bl then p:=p^.a1
else p:=p^.a2;
until p=nil;
if bl then q^.a1:=w
else q^.a2:=w;
end; end;
////////////////////////
procedure solv.blns;
procedure bls(i,j:integer);
var m:integer;
begin
if i<=j then
begin
m:=(i+j) div 2;
add(a[m]);
bls(i,m-1);
bls(m+1,j);
end;    end;
begin
 proot:=Nil;
  BLs(1,n);
end;
/////////////////////////////////
procedure solv.del;
begin
p:=proot;
while (p<>nil) and (p^.inf.num<>i) do begin
q:=p;
if p^.inf.num>i then p:=p^.a1
else  p:=p^.a2; end;
if (p<>nil) then begin
if p=proot then   begin
new(q);
q^.a1:=p; end;
if (p^.a1=nil) and (p^.a2=nil) then
if q^.a1=p then q^.a1:=nil
else q^.a2:=nil
else if p^.a1=nil then
if q^.a1=p then q^.a1:=p^.a2
else q^.a2:=p^.a2
else
 if p^.A2=Nil then
if q^.a1=p then q^.a1:=p^.a1
else q^.a2:=p^.a1
else
		        begin
		          w:=p^.A1;
              if w^.A2=Nil then
                w^.A2:=p^.A2
		          else
 begin
			            Repeat
                    v:=w;
                    w:=w^.A2;
			            Until w^.A2=Nil;
			            v^.A2:=w^.A1;
			            w^.A1:=p^.A1;
			            w^.A2:=p^.A2;
			          end;
		          if q^.A1=P then
                q^.A1:=w
					    else
                q^.A2:=w;
		        end;
	    if p=proot then
        begin
          proot:=q^.A1;
          Dispose(q);
        end;
	    Dispose(p);
    end;
end;
///////////////////////////8///
procedure solv.view;
var kl:integer;
      procedure VW(p:ttree;Var kl:Integer);
      begin
      if  p<>Nil then
        with Form1.TreeView1.Items do
          begin
            if kl=-1 then
              AddFirst(Nil, p^.Inf.fio+' '+IntToStr(p^.Inf.num))
            else
              AddChildFirst(Form1.TreeView1.Items[kl],
            p^.Inf.fio+' '+IntToStr(p^.Inf.num));
            Inc(kl);
            VW(p^.A1,kl);
            VW(p^.A2,kl);
            Dec(kl);
          end;
      end;
begin
  Form1.TreeView1.Items.Clear;
  p:=proot;
    kl:=-1;
  VW(p,kl);
  Form1.TreeView1.FullExpand;
  bl:=true;
end;
////////////////////////////
procedure solv.delete;
begin
bl:=false;
  if p=nil then
    Exit;
  Delete(p^.A1);
  Delete(p^.A2);
  Dispose(p);
  proot:=Nil;
  end;
  /////////////////////////
  procedure solv.left;
  var h:integer;
  begin
  p:=proot^.a1;
  while (p^.a2<>nil) do begin
  q:=p;
   p:=p^.a2;
  h:=p^.inf.num; end;
  q^.a2:=nil;
  end;

end.
