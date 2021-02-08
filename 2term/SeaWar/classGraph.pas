unit classGraph;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs,classField, StdCtrls, ExtCtrls,classBrain,classShip;
  type
  Tgraph=class(tobject)
    FieldTop,FieldBottom,FieldLeft,FieldRight,SqrS,CurX,CurY,CurSize:Integer;
    Right:boolean;
    memo:Tmemo;
    procedure DrawField(image1:Timage;Nship:integer);
    procedure RdrShape(shape1,shape2:Tshape;image1:timage);
    function PlaceShip(FielS:integer;Image1:Timage;Field:Tfield):boolean;
    procedure DisShape(shape1,shape2,shape3,shape4:Tshape);
    procedure EnebShape(shape1,shape2,shape3,shape4:Tshape);
    procedure Hit(x,y:integer; image:Timage);
    procedure Beside(x,y:integer; image:Timage);
    function Strike(Fiels:integer;Field:Tfield;image:Timage):boolean;
    procedure CpuStrike(Brain:Tbrain;Fiels:integer;Field:Tfield;image:Timage);
    procedure IsKilled(x,y:integer; Image:Timage);
    constructor create;
  end;

implementation

constructor tgraph.create;
var
i:integer;
begin
FieldTop:=30;
FieldBottom:=291;
FieldLeft:=30;
FieldRight:=291;
SqrS:=25;
Right:=true;
CurSize:=4;
end;

procedure tgraph.DrawField;
var i,cur,count:integer;
ch:char;
s:string;
begin
image1.Transparent:=true;
with Image1.Canvas do begin
        image1.Picture.Bitmap.TransparentColor:=clnavy ;
        pen.color:=clnavy;
        brush.Color:=clbtnface;
        rectangle(0,0,image1.Width,image1.Height);
        pen.color:=clblack;
        brush.Color:=claqua;
        Pen.width:=1;
        rectangle(FieldLeft,FieldTop,FieldRight,FieldBottom);
        cur:=FieldLeft;
        for i:=1 to Nship-1 do begin
                cur:=cur +SqrS+1;
                Moveto(Cur,FieldTop);
                Lineto(Cur,FieldBottom);
        end;
        cur:=FieldTop;
        for i:=1 to Nship-1 do begin
                cur:=cur +SqrS+1;
                Moveto(FieldLeft,Cur);
                Lineto(FieldRight,Cur);
        end;
        cur:=Sqrs+12;
        ch:='a';
        font.Size:=18;
        brush.Color:=clbtnface;
        for i:=1 to Nship do begin
                s:=ch;
                TextOut(Cur,FieldLeft-Sqrs-5,s);
                inc(ch);
                cur:=cur +SqrS+1;
        end;
        cur:=FieldTop-1;
        count:=1;
        brush.Color:=clbtnface;
        for i:=1 to Nship do begin
                TextOut(0,cur,inttostr(count));
                inc(count);
                cur:=cur +SqrS+1;
        end;
end;
end;

procedure tgraph.RdrShape;
var CurSX,CurSY:integer;
begin
if(Right=true) then begin
if((CurX>=FieldLeft+Image1.Left) and (CurX+(CurSize-1)*(Sqrs+1)+2<=Image1.Left+FieldRight) and (CurY>=FieldTop+Image1.Top) and (CurY+2<=FieldBottom+Image1.Top)) then
        begin
        CurSx:=(CurX-image1.Left-FieldLeft) div (Sqrs+1);
        CurSy:=(Cury-Image1.Top-FieldTop) div (Sqrs+1);
        shape2.Left:=image1.Left+FieldLeft+(CurSx)*(Sqrs+1);
        shape2.Top:=image1.Top+FieldTop+(CurSy)*(Sqrs+1);
        if(shape1.Visible=true) then
                shape2.Visible:=true
        else
                shape2.Visible:=false;
        end
else
        shape2.Visible:=false;
end
else
if((CurX>=FieldLeft+Image1.Left) and (CurX+2<=Image1.Left+FieldRight) and (CurY>=FieldTop+Image1.Top) and (CurY+(CurSize-1)*(Sqrs+1)+2<=FieldBottom+Image1.Top)) then
        begin
        CurSx:=(CurX-image1.Left-FieldLeft) div (Sqrs+1);
        CurSy:=(Cury-Image1.Top-FieldTop) div (Sqrs+1);
        shape2.Left:=image1.Left+FieldLeft+(CurSx)*(Sqrs+1);
        shape2.Top:=image1.Top+FieldTop+(CurSy)*(Sqrs+1);
        if(shape1.Visible=true) then
                shape2.Visible:=true
        else
                shape2.Visible:=false;
        end
else
        shape2.Visible:=false;
shape1.Left:=Curx;
shape1.top:=Cury;
end;

function tgraph.PlaceShip(FielS:integer;Image1:Timage;Field:Tfield):boolean;
var i,CurSX,CurSY:integer;
begin
CurSx:=(CurX-image1.Left-FieldLeft) div (Sqrs+1);
CurSy:=(Cury-Image1.Top-FieldTop) div (Sqrs+1);
if(Right=true) then begin
if((Cursx+CurSize<=FielS)and (CurSX>=0) and (CurSY>=0) and (Cursy<FielS)) then begin
   if(Field.AddShip(CurSx,CurSy,CurSize,Right)=true) then begin
        result:=true;
        with Image1.Canvas do begin
         pen.Width:=1;
         Brush.Color:=clblue;
         for i:=0 to CurSize-1 do
            rectangle(FieldLeft+CurSx*(Sqrs+1)+i*(Sqrs+1),FieldTop+CurSy*(Sqrs+1),FieldLeft+1+CurSx*(Sqrs+1)+(i+1)*(Sqrs+1),FieldTop+1+CurSy*(Sqrs+1)+(Sqrs+1));
       end;
    end
    else
        result:=false;
end
    else
        result:=false;
end
else
begin
if((Cursx<FielS)and (CurSX>=0) and (CurSY>=0) and (Cursy+CurSize<=FielS)) then begin
   if(Field.AddShip(CurSx,CurSy,CurSize,Right)=true) then begin
        result:=true;
        with Image1.Canvas do begin
         pen.Width:=1;
         Brush.Color:=clblue;
         for i:=0 to CurSize-1 do
            rectangle(FieldLeft+CurSx*(Sqrs+1),FieldTop+CurSy*(Sqrs+1)+i*(Sqrs+1),FieldLeft+1+CurSx*(Sqrs+1)+(Sqrs+1),FieldTop+1+CurSy*(Sqrs+1)+(i+1)*(Sqrs+1));
       end;
    end
    else
        result:=false;
end
    else
        result:=false;
end;
end;

procedure Tgraph.DisShape;
begin
shape1.enabled:=false;
shape2.enabled:=false;
shape3.enabled:=false;
shape4.enabled:=false;
end;

procedure Tgraph.EnebShape;
begin
shape1.enabled:=true;
shape2.enabled:=true;
shape3.enabled:=true;
shape4.enabled:=true;
end;

procedure Tgraph.Hit;
begin
with image.Canvas do begin
        brush.Color:=clyellow;
        rectangle(FieldLeft+x*(Sqrs+1),FieldTop+y*(Sqrs+1),FieldLeft+1+x*(Sqrs+1)+(Sqrs+1),FieldTop+1+y*(Sqrs+1)+(Sqrs+1));
        moveto(FieldLeft+x*(Sqrs+1),FieldTop+y*(Sqrs+1));
        lineto(FieldLeft+1+x*(Sqrs+1)+(Sqrs+1),FieldTop+1+y*(Sqrs+1)+(Sqrs+1));
        moveto(FieldLeft+1+x*(Sqrs+1)+(Sqrs+1),FieldTop+y*(Sqrs+1));
        lineto((FieldLeft+x*(Sqrs+1)),FieldTop+1+y*(Sqrs+1)+(Sqrs+1));
end;
end;

procedure Tgraph.Beside;
begin
with image.canvas do begin
brush.Color:=clblack;
ellipse(FieldLeft+x*(Sqrs+1)+sqrs div 3,FieldTop+y*(Sqrs+1)+sqrs div 3,FieldLeft+1+x*(Sqrs+1)+(Sqrs+1)-sqrs div 3,FieldTop+1+y*(Sqrs+1)+(Sqrs+1)-sqrs div 3);
end;
end;

function Tgraph.Strike(Fiels:integer;Field:Tfield;image:Timage):boolean;
var i,Health,CurSX,CurSY:integer;
begin
inc(Field.Move);
CurSx:=(CurX-image.Left-FieldLeft) div (Sqrs+1);
CurSy:=(Cury-Image.Top-FieldTop) div (Sqrs+1);
if((Cursx+CurSize<=FielS)and (CurSX>=0) and (CurSY>=0) and (Cursy<FielS)) then begin
        if(Field.ifstriked(Cursx,cursy)=false) then begin
                Field.StrikeTable[CurSx,CurSy]:=true;
                if(Field.Strike(Cursx,CurSy)=false) then begin
                        Beside(Cursx,CurSy,Image);
                        result:=false;
                        end
                else begin
                        Health:=field.GetHealth(Cursx,CurSy);
                        if(Health>0) then
                                Hit(CurSx,CurSy,Image)
                        else begin
                                dec(field.ShipLeft[field.getsize(cursx,cursy)-1]);
                                for i:=1 to  field.getsize(cursx,cursy) do
                                        IsKilled(field.GetShipX(CurSx,CurSy,i),field.GetShipY(CurSx,CurSy,i),image);
                        if(field.MaxShip=0) then
                        result:=false;
                        end;
                        result:=true;
                end;
        end
        else
                result:=true;
end;
end;

procedure Tgraph.CpuStrike;
var res:boolean;
i,Health:integer;
begin
res:=true;
while(res=true) do begin
brain.easy(Fiels);
     if(Field.ifstriked(brain.Curx,brain.Cury)=false) then begin
                Field.StrikeTable[brain.Curx,brain.Cury]:=true;
                if(Field.Strike(brain.Curx,brain.Cury)=false) then begin
                        Beside(brain.Curx,brain.Cury,Image);
                        res:=false;
                        end
                else begin
                        Health:=field.GetHealth(brain.Curx,brain.Cury);
                        if(Health>0) then
                                Hit(brain.Curx,brain.Cury,Image)
                        else begin
                                dec(field.ShipLeft[field.GetHealth(brain.Curx,brain.Cury)-1]);
                                for i:=1 to  field.GetSize(brain.Curx,brain.Cury) do
                                        IsKilled(field.GetShipX(brain.Curx,brain.Cury,i),field.GetShipY(brain.Curx,brain.Cury,i),image);
                        if(field.MaxShip=0) then
                        res:=false;
                        end;
                        res:=true;
                end;
        end
        else
                res:=true;
end;
end;

procedure tgraph.IsKilled;
begin
with image.Canvas do begin
brush.Color:=clred;
rectangle(FieldLeft+x*(Sqrs+1),FieldTop+y*(Sqrs+1),FieldLeft+1+x*(Sqrs+1)+(Sqrs+1),FieldTop+1+y*(Sqrs+1)+(Sqrs+1));
end;
end;
end.
