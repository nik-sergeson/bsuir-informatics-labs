unit Unit2;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;
  type fun=function(x:extended):extended;
  function tabl(a,b:extended;n:integer;f:fun):extended;
implementation
   function tabl(a,b:extended;n:integer;f:fun):extended;
   var x,y,h,s:extended;
   i:integer;
   begin
   h:=(b-a)/n;  s:=0;
   for i:=1 to n+1 do begin
   x:=a+h*(i-0.5);
   y:=f(x);
   s:=s+h*y;
   end;
   result:=s; end;
   end.
