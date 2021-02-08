unit Unit2;

interface
uses
 Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;
  type
  tsel=^sel;
  sel=record
  dig:integer;
  prev:tsel;
  next:tsel;
  end;
  stack=class(tobject)
  sp,sp1,spk:tsel;
  key,dim:integer;
  procedure add(i:integer);
  constructor create;
  procedure print(list:TListBox);
  procedure read(var i:integer);
  procedure poisk(var spi:tsel);
  procedure readfter(var i:integer);
  procedure addafter(i:integer);
  procedure sortslip(var tp:stack);
  procedure read1(var i:integer);
  procedure addlast(var i:integer);
  procedure solution;
    end;
implementation
 constructor stack.create;
 begin
 Inherited create;
  New(sp1);
  New(spk);
  sp1:=Nil;
  spk:=Nil;
 end;
 procedure stack.add;
 begin
 New(sp);
  sp.dig:=i;
  sp^.next:=Nil;
  sp^.prev:=Nil;
  if sp1=Nil then
    begin
      sp1:=sp;
      spk:=sp;
    end
  else
    begin
      sp^.next:=sp1;
      sp1^.prev:=sp;
      sp1:=sp;
    end; end;
 procedure stack.addlast;
 begin
   New(sp);
  sp.dig:=i;
  sp^.next:=Nil;
  sp^.prev:=Nil;
  if sp1=Nil then
    begin
      sp1:=sp;
      spk:=sp;
    end
  else
    begin
      spk^.next:=sp;
      sp^.prev:=spk;
      spk:=sp;
    end;
    end;
 procedure stack.read;
 begin
 sp:=spk;
 i:=spk^.dig;
 sp1^.prev^.next:=nil;
 spk:=sp1^.prev;
 dispose(sp);
 end;
 procedure stack.print;
 var l:integer;
 begin
 sp:=sp1;
 for l:=1 to dim do begin
 list.items.add(inttostr(sp^.dig));
 sp:=sp^.next;
 end;
 end;
 procedure stack.poisk;
 begin
 sp:=sp1;
 while (sp^.dig<>key) and(sp^.next<>nil) do
 sp:=sp^.next;
 if sp^.dig=key then  spi:=sp;
 end;
 procedure stack.addafter;
 var spp,spi:tsel;
 begin
 poisk(spi);
 new(spp);
 spi^.next:=spp;
  spp^.dig:=i;
 spp^.prev:=spi;
 spp^.next:=spi.next;
 spp^.next^.prev:=spp;
 end;
 procedure stack.readfter;
 var spi:tsel;
 begin
 poisk(spi);

 end;
 procedure stack.read1;
 var b1:boolean;
 begin
   if spk=Nil then
    begin
      ShowMessage('Список пуст');
      b1:=false;
    end
  else
    begin
      b1:=true;
      if spk<>sp1 then
        begin
          sp:=sp1;
          i:=sp^.dig;
          sp^.next^.prev:=Nil;
          sp1:=sp^.next;
          Dispose(sp);
        end
      else
        begin
          sp:=spk;
          i:=spk.dig;
          sp1:=Nil;
          spk:=Nil;
        end;
    end;
 end;
 procedure stack.sortslip;
Procedure Div2sp( var tp,tq,tr:stack);
 var Inf:integer;
    bl:boolean;
begin
  tq:=stack.create;
  tr:=stack.create;
  bl:=true;
  while bl do
    begin
      tp.Read1(Inf);
      tq.AddLast(Inf);
      bl:=(tp.sp1<>Nil);
      if bl then
        begin
          tp.Read1(Inf);
          tr.AddLast(Inf);
          bl:=(tp.sp1<>Nil);
        end;
    end;
       end;
      Procedure Slip(var tq,tr,tp:stack);
 Var i:integer;
 Begin
      While(tq.sp1<>Nil) and (tr.sp1<>Nil) do 
	  if tq.sp1.dig<tr.sp1.dig 
       then begin tq.Read1(i); tp.addlast(i); end
       else begin tr.Read1(i); tp.Addlast(i) end;

   while tq.sp1<>nil do
     begin tq.Read1(i); tp.Addlast(i); end;

   while tr.sp1<>nil do
     begin tr.Read1(i); tp.Addlast(i); end;
 end;
   var tq,tr:stack;
begin
  if tp.sp1<>tp.spk then
    begin
      Div2sp(tp,tq,tr);
      SortSlip(tq);
	    SortSlip(tr);
	    Slip(tq,tr,tp);
    end;
    end;
  procedure stack.solution;
  var f,l:integer;
  ssp:tsel;
  begin
  sp:=sp1;
  while sp^.next<>nil do begin
   if (sp^.dig<0) and (sp^.prev=nil) then begin
  sp^.next^.prev:=nil;
  sp1:=sp^.next;
  dim:=dim-1;
  dispose(sp);
  sp:=sp1;
  end
  else  if (sp^.dig>=0) and (sp^.prev=nil) then
  sp:=sp1^.next;
  if (sp^.dig<0) and (sp^.prev<>nil) then begin
   ssp:=sp^.prev;
   sp^.prev^.next:=sp^.next;
  sp^.next^.prev:=sp^.prev;
  dispose(sp);
  dim:=dim-1;
  sp:=ssp^.next;
   end;
 if (sp^.dig>=0) and (sp^.prev<>nil) then
 sp:=sp^.next;
    end;
   if (sp^.dig<0) then begin
   sp^.prev^.next:=nil;
   dispose(sp);
   dim:=dim-1;
     end;

      end;
end.
