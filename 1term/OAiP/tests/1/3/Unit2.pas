unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;
  type
   fun=function(x:extended):extended;
   procedure tabl(f:fun;a,b:extended;n:integer;me:tmemo;var file1:textfile);
implementation
   procedure tabl;
   var
   h,x,y:extended;
   j:integer;
   begin
   h:=(b-a)/n;
   x:=a;
   for j:=1 to n+1 do begin
   y:=f(x);
   write(file1,y,'   ',x);
   me.Lines.Add('x='+floattostr(x)+'y='+floattostr(y));
   x:=x+h;
    end;
   end;
end.
