unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ExtCtrls, StdCtrls, Buttons;
 var colrback:tcolor;
 x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,d:integer;
type  tviz=class(tobject)
      canvas:tcanvas;
      colorline:tcolor;
      x,y,r,d:integer;
      procedure ris; virtual; abstract;
      procedure draw(bl:boolean);
      procedure show;
      procedure hide;
      procedure moveto(dx,dy,dr:integer);
      end;
      trect=class(tviz)
      x1,y1,x2,y2,fmax,machta,fmin,nos:integer;
      constructor create (x0,y0,r0,d0:integer;colorline0:tcolor; canvas0:tcanvas);
      procedure ris; override;
           procedure flag(dh,ddx:integer);
           procedure flagd(dh,ddx:integer);
                      end;
     tnak=class(tviz)
    x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6:integer;
     constructor create (x0,y0,r0,d0:integer;colorline0:tcolor; canvas0:tcanvas);
       procedure ris;  override;
      end;

implementation
procedure tviz.draw(bl:boolean);
begin
with canvas do begin
if bl then begin
pen.color:=colorline;
brush.color:=colorline end
else begin
pen.color:=colrback;
brush.color:=colrback; end;
ris;
end; end;
 procedure tviz.show;
begin
draw(true); end;
procedure tviz.hide;
begin
draw(false);
end;
procedure tviz.moveto;
begin
hide;
x:=x+dx; r:=r+dr;
 y:=y+dy; d:=d+dr;
show; end;
constructor trect.create;
begin
colorline:=colorLine0;
canvas:=canvas0;
x:=x0;y:=y0; d:=d0; r:=r0;
end;
Procedure Trect.Ris;
Begin
        x1:=x-r;  x2:=x+r;  y1:=y-d;  y2:=y+d;
        with canvas do begin
    Canvas.rectangle(x1,y1,x2,y2);
    nos:=round(x1+2.1*17*r/14);
    canvas.Polygon([point(x2,y2),point(round(x1+2.1*17*r/14),round(y1-0.6*d)),
    point(round(x2-11*r/14),round(y1-0.6*d)),point(round(x1+14.48*r/14),y1)]);
    canvas.Brush.Color:=clwhite;
    canvas.Ellipse(round(x2-0.3*r),y1,x2,y2-d);
    canvas.Ellipse(round(x2-0.8*r),y1,round(x2-0.5*r),y2-d);
    moveto(round(x1+14.48*r/14),y1);
    canvas.lineto(round(x1+14.48*r/14),y1-3*d);
    machta:=(y1-3*d);
        lineto(round(x1),round(y1));
      end;  end;
  constructor tnak.create;
begin
colorline:=colorLine0;
canvas:=canvas0;
x:=x0;y:=y0; d:=d0; r:=r0;
end;
    procedure tnak.ris;
    begin
        x1:=round(x-2*r);  x2:=x-3*r;  y1:=round(y-1.5*d);  y2:=y-3*d;
    x3:=x+3*r; y3:=y-3*d; x4:=round(x+2*r); y4:=round(y-1.5*d); x5:=round(x+2*r); y5:=round(y+1.5*d);
  x6:=round(x-2*r); y6:=round(y+1.5*d);     canvas.polygon([point(x1,y1),point(x2,y2),
    point(x3,y3),point(x4,y4),point(x5,y5),point(x6,y6)]);
        end;
        procedure trect.flag(dh,ddx:integer);
        var df,rf:extended;
           begin
          canvas.Pen.Color:=clblack;
                df:=d/4; rf:=r/4;
       fmax:=round((y1-0.8*d)-df)-dh;
       fmin:=(round(y1-0.6*d)-round((round(y1-0.6*d)-round(y1-0.8*d-df))/1));
      canvas.polygon([point(round(x1+14.48*r/14)+1+ddx,round(y1-0.6*d)-dh),
      point(round((x1+14.48*r/14)+1.5*rf)+1+ddx,round(y1-0.6*d)-dh),
      point(round((x1+14.48*r/14)+rf)+1+ddx,(round(y1-0.6*d)-round((round(y1-0.6*d)-round(y1-0.8*d-df))/2))-dh),
      point(round((x1+14.48*r/14)+1.5*rf)+1+ddx,round((y1-0.8*d)-df)-dh),
      point(round((x1+14.48*r/14))+1+ddx,round((y1-0.8*d)-df)-dh)]);
       end;
       procedure trect.flagd(dh,ddx:integer);
        var df,rf:extended;
           begin
           canvas.Pen.Color:=clwhite;
      df:=d/4; rf:=r/4;
        canvas.polygon([point(round(x1+14.48*r/14)+1+ddx,round(y1-0.6*d)-dh),
      point(round((x1+14.48*r/14)+1.5*rf)+1+ddx,round(y1-0.6*d)-dh),
      point(round((x1+14.48*r/14)+rf)+1+ddx,(round(y1-0.6*d)-round((round(y1-0.6*d)-round(y1-0.8*d-df))/2))-dh),
      point(round((x1+14.48*r/14)+1.5*rf)+1+ddx,round((y1-0.8*d)-df)-dh),
      point(round((x1+14.48*r/14))+1+ddx,round((y1-0.8*d)-df)-dh)]);
       end;



       end.
