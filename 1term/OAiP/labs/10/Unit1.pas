unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ExtCtrls, StdCtrls, Buttons;

type
  TForm1 = class(TForm)
    Image1: TImage;
    BitBtn1: TBitBtn;
    BitBtn2: TBitBtn;
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    Button5: TButton;
    Button6: TButton;
    Button7: TButton;
    procedure BitBtn1Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
    procedure Button6Click(Sender: TObject);
    procedure Button7Click(Sender: TObject);
    procedure BitBtn2Click(Sender: TObject);
     private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;


implementation

{$R *.dfm}
uses unit2;
var rect:trect;
nak:tnak;
okno:timage;
x0,y0,r0,d0,pxm,pym,i,l:integer;
bll:boolean;
procedure TForm1.BitBtn1Click(Sender: TObject);
begin
okno:=form1.image1;
colrBack:=clWhite;
pxm:=okno.clientwidth;
pym:=okno.clientheight;
with okno.canvas do begin
 pen.color:=colrBack;
   brush.color:=colrBack;
   Rectangle(0,0,image1.width,image1.height);
   x0:=pxm div 2;
  y0:=pym div 2;
  r0:=50;
  d0:=30;
    rect:=Trect.Create(x0,y0,2*r0,d0,clBlack,okno.Canvas);
        rect.show;
   end;
    end;
procedure TForm1.Button1Click(Sender: TObject);
begin
while rect.nos+4<okno.Width do begin
rect.moveto(3,0,0);
okno.Update;
sleep(10); end;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  nak:=tnak.Create(rect.x1+2*r0,2*d0,2*r0,d0,clBlack,okno.Canvas);
        nak.show;
while nak.y6<rect.y2 do begin
nak.moveto(0,3,0);
okno.Update;
sleep(10);
end; end;

procedure TForm1.Button3Click(Sender: TObject);
begin
if bll then begin
rect.flagd(l,0);
 end;
 rect.flagd(l,0);
rect.moveto(6,0,0);
rect.flag(l,0);
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
if bll then begin
rect.flagd(l,0);
 end;
 rect.flagd(l+6,0);
rect.moveto(0,6,0);
rect.flag(l,0);
end;

procedure TForm1.Button5Click(Sender: TObject);
begin
if bll then begin
rect.flagd(l,0);
 end;
 rect.flagd(l,0);
rect.moveto(-6,0,0);
rect.flag(l,0);
end;

procedure TForm1.Button6Click(Sender: TObject);
begin
if bll then begin
rect.flagd(l,0);
 end;
  rect.flagd(l-6,0);
rect.moveto(0,-6,0);
rect.flag(l,0);
end;

procedure TForm1.Button7Click(Sender: TObject);
var i:integer;
begin
rect.flag(1,0); rect.flagd(1,0);
i:=1;
while rect.fmax>=rect.machta do begin
rect.flagd(i,0);
okno.Update;
sleep(20);
inc(i);
rect.flag(i,0);
okno.Update;
sleep(20);
end; l:=i;
bll:=true;
 end;

procedure TForm1.BitBtn2Click(Sender: TObject);
begin
rect.Free;
nak.Free;
end;

end.
