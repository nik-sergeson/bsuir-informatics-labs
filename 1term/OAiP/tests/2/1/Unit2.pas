unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ExtCtrls, StdCtrls, Buttons;

type
tviz=class(tobject)
lcolor:tcolor;
x,y,z:integer;
canvas:tcanvas;
procedure draw; virtual; abstract;
procedure moveto(dx,dy,dz:integer);
procedure show;
procedure hide;
procedure ris;
end;
tris=class(tviz)
procedure draw; override;
constructor create(x0,y0,z0:integer;canvas0:tcanvas);
end;
implementation
procedure tviz.moveto;
begin
hide;
x:=x+dx; y:=y+dy; z:=z+dz;
show;
end;
procedure tviz.show;
begin
lcolor:=clblack;
ris;
end;
procedure tviz.hide;
begin
lcolor:=clwhite;
ris;
end;
procedure tviz.ris;
begin
canvas.Pen.color:=lcolor;
draw;
end;
constructor tris.create;
begin
canvas:=canvas0; x:=x0; y:=y0; z:=z0;
end;
procedure tris.draw;
begin
canvas.Rectangle(x+50,y+50,x-50,y-50);
canvas.Ellipse(x+50,y+50,x-50,y-50);
end;
end.
