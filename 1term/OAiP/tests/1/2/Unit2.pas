unit Unit2;

interface
 uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls,math;
  function fun(x:integer):integer;
implementation
   function fun;
   var
   m,ost:integer;
   begin
   m:=0;
   while x>0 do begin
     ost:=x mod 10;
     m:=m*10+ost;
     x:=x div 10;
       result:=m;
       end;  end;
       end.
