unit Unit2;
interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ComCtrls, StdCtrls, Buttons, ExtCtrls,  Clipbrd,
  TeEngine, Series, TeeProcs, Chart;

type
fun=function(x:extended):extended;
procedure tabl(f:fun;xn,xk,e:extended;m:word;mem1:tmemo);
procedure graf(f:fun;xn,xk,e:extended;m:word;chart1:TChart);
procedure graf2(f,n:fun;xn,xk,e:extended;m:word;chart1:TChart);
implementation
procedure tabl;
var h,x,y:extended;
i:integer; begin
h:=(xk-xn)/m; x:=xn;
for i:=1 to m+1 do begin
y:=f(x);
mem1.lines.add(floattostr(y)+'      '+floattostr(x));
x:=x+h; end; end;
procedure graf;
var h,x,y:extended;
i:integer; begin
h:=(xk-xn)/m; x:=xn;
for i:=1 to m+1 do begin
y:=f(x);
Chart1.SeriesList[0].AddXY(x,y);
x:=x+h; end; end;
procedure graf2;
var h,x,y,z:extended;
i:integer; begin
h:=(xk-xn)/m; x:=xn;
for i:=1 to m+1 do begin
y:=f(x); z:=n(x);
 Chart1.SeriesList[0].AddXY(x,y);
 Chart1.SeriesList[1].AddXY(x,z);
x:=x+h; end; end;
end.
