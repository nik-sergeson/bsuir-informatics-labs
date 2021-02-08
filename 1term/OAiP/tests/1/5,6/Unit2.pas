unit Unit2;
interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls;
  type fun=function(x:extended):extended;
procedure graf(a,b,ymax,ymin:extended;m,n:integer;f:fun;im:timage);


implementation
  procedure graf;
  var x,y,h,hx,hy:extended;
  p,l:integer;
  begin
 with im.Canvas do begin
  try
  h:=(b-a)/n;
  p:=20;
  hy:=(im.Height-2*p)/(ymax-ymin);
  hx:=(im.Width-2*p)/(b-a);
  brush.color:=clwhite;    pen.Color:=clblack;
  rectangle(0,0,im.Width,im.Height);
  rectangle(p,p,im.Width-p,im.Height-p);
  x:=a; y:=f(x);                      except showmessage('here'); end;
  moveto(p,im.Height-(p+round(y*hy)));
  for l:=1 to n do begin
  x:=x+h;  y:=f(x);
  lineto(round(x*hx),im.Height-(p+round(y*hy)));
  end;
  pen.Color:=clwhite;
  rectangle(0,0,im.Width,p-1);
  rectangle(im.Width-p+1,0,im.Width,im.Height);
  end; end;
end.
