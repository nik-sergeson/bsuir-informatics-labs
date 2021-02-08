unit Unit2;

    interface
  uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs,math;
  type
  tstack=^stack;
  stack=record
  inf:char;
  a:tstack;
  end;
  sstack=class(tobject)
  sp,sp1:tstack;
  zn:array['a'..'я']of extended;
  procedure add1(i:char);
  procedure read1(var i:char);
  function av(strp:string):extended;
  procedure obr(var strpi,strp:string);
  end;
  var str:string;
  sck:sstack;
implementation
  procedure sstack.add1;
  begin
  new(sp);
  sp^.inf:=i;
  sp^.a:=sp1;
  sp1:=sp;
  end;

  procedure sstack.read1;
  begin
  i:=sp1^.inf;
  sp:=sp1;
  sp1:=sp1^.a;
  dispose(sp);
  end;
  function sstack.av(strp:string):extended;
  var chr,ch,ch1,ch2:char;
  i:integer;
  op1,op2,rez:extended;
  begin
  sck:=sstack.create;
  chr:=succ('z');
  for i:=1 to length(strp) do begin
  ch:=strp[i];
  if not (ch in ['*','/','+','-','^']) then
  sck.add1(ch)
  else begin
  sck.read1(ch2); sck.read1(ch1);
  op1:=zn[ch1];  op2:=zn[ch2];
  case ch of
  '+':rez:=op1+op2;
  '-':rez:=op1-op2;
  '*':rez:=op1*op2;
  '/':rez:=op1/op2;
  '^':rez:=power(op1,op2);
  end;
  zn[chr]:=rez;
       sck.Add1(chr); Inc(chr);
  end; end;
  result:=rez; sck.Free;
  end;

  procedure sstack.obr;
  function prior(ch:char):integer;
    begin
	   case ch of
		'(',')':prior:=0;
		'+','-':prior:=1;
		'*','/':prior:=2;
		    '^':prior:=3;
	   end;
  end;
 var i,pr:integer;
 ch,ch1:char;
   begin
   sck:=sstack.Create;
   for i:=1 to length(strpi) do begin
   ch:=strpi[i];
     if not (ch in['+','-','*','/','(',')','^'])
	   then	strp:=strp+ch
     else
   if sck.sp1=nil then
   sck.add1(ch)
   else
   if ch='(' then
   sck.add1(ch)
   else
   if ch=')' then  begin
   sck.read1(ch);
   while ch<>'(' do  begin
   strp:=strp+ch;
   sck.read1(ch);
   end;
   end
   else begin
   pr:=prior(ch);
   While (sck.sp1<>nil) and (pr<= prior(sck.sp1.Inf)) do begin
   sck.read1(ch1);
   strp:=strp+ch1; end;
   sck.add1(ch);
   end;   end;
   While sck.sp1<>nil do begin sck.Read1(ch);
 strp:=strp+ch end;
    end;

end.
