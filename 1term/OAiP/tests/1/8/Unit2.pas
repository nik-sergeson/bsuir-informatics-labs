unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ComCtrls, StdCtrls, Buttons, ExtCtrls,  Clipbrd,
  TeEngine, Series, TeeProcs, Chart;
   type
  complex=record
  re,im:extended; end;
  type f=function(o:extended):complex;
procedure tabl(a,b:extended;n:integer;comp:f; Chart1: TChart);

implementation
   procedure tabl;
   var x1,h:extended;
   y1:complex;
   i:integer; begin
   Chart1.serieslist[0].clear;
   chart1.serieslist[1].clear;
   begin
   h:=(b-a)/n;
   x1:=a;
   for i:=1 to n+1 do begin
   y1:=comp(x1);
   chart1.serieslist[0].addxy(x1,y1.re);
    chart1.serieslist[1].addxy(x1,y1.Im);
   x1:=x1+h;
   end;
   end; end;
end.
