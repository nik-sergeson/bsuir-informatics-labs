unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls;
  procedure ris(x,y,r,h:extended;im:timage);
implementation
  procedure ris;
  var px,py,pr:extended;
  x1,y1:integer;
  begin
  with im.Canvas do begin
  x1:=im.Width div 2; y1:=im.Height div 2;
  px:=x/h; py:=y/h; pr:=r/h;
  brush.Color:=clgreen;
  rectangle(0,0,im.Width,im.Height);
  brush.Color:=clred; pen.Color:=clred;
  ellipse(round(x1-pr),im.Height-round(y1+pr),round(x1+pr),im.Height-(round(y1-pr)));
  ellipse(round(px-4),round(py-4),round(px+4),round(py+4));
  end; end;
  end.
