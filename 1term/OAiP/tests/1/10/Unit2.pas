unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ExtCtrls, StdCtrls;

procedure rec(x1,x2, x3,y1,y2,y3,h:extended; m:timage);

implementation
procedure rec;
var s:string;
x11,x22,x33,s1,p:extended;
begin
with m.Canvas do begin
brush.Color:=clyellow;
rectangle(0,0,m.Width,m.Height);
brush.Color:=clblue;
polygon([point(round(x1/h),m.height-round(y1/h)),point(round(x2/h),m.height
-round(y2/h)),point(round(x3/h),m.height-round(y3/h))]);
try x11:=sqrt(sqr(x1-x2)+sqr(y1-y2));
x22:=sqrt(sqr(x2-x3)+sqr(y2-y3));
x33:=sqrt(sqr(x3-x1)+sqr(y3-y1));
p:=(x11+x22+x33)/2;
s1:=sqrt(p*(p-x11)*(p-x22)*(p-x33));  except showmessage('22'); end;
s:=floattostr(s1);
brush.Color:=clwhite;
textout(0,0,s);
end;end;
end.
