unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs,classField, StdCtrls, ExtCtrls,classGraph,classbrain,classHighs;

type
  TForm1 = class(TForm)
    Image1: TImage;
    Button1: TButton;
    Shape1: TShape;
    Shape2: TShape;
    Shape3: TShape;
    Shape4: TShape;
    Shape5: TShape;
    Shape6: TShape;
    Image2: TImage;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Edit4: TEdit;
    Edit5: TEdit;
    Edit6: TEdit;
    Edit7: TEdit;
    Edit8: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Button2: TButton;
    Memo1: TMemo;
    Edit9: TEdit;
    Button3: TButton;
    procedure FormMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure Shape1MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure Image1MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure FormCreate(Sender: TObject);
    procedure Shape2MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure Shape6MouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure Shape5MouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure Shape4MouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure Shape3MouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure Shape1MouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure Button1Click(Sender: TObject);
    procedure Image2MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
     private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  UI:Tgraph;
  Plr,Cpu:Tfield;
  Brain:Tbrain;
  Score:Thighscore;
  const shed=12;

implementation

{$R *.dfm}

procedure TForm1.FormMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
UI.CurX:=x;
UI.CurY:=y;
if ((UI.CurX>=Image1.Left) and (UI.CurX<=Image1.Left+Image1.Width) and (ui.CurY>=Image1.Top) and (UI.CurY<=Image1.Height+Image1.Top)) then
        if(Plr.gmstart=true) then
                UI.RdrShape(shape1,shape2,image2)
        else
                UI.RdrShape(shape1,shape2,image1)
else
        if(Plr.gmstart=true) then
                UI.RdrShape(shape1,shape2,image2)
        else
                UI.RdrShape(shape1,shape2,image1);
end;

procedure TForm1.Shape1MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
UI.Curx:=UI.CurX+x;
UI.Cury:=UI.CurY+y;
if ((UI.CurX>=Image1.Left) and (UI.CurX<=Image1.Left+Image1.Width) and (ui.CurY>=Image1.Top) and (UI.CurY<=Image1.Height+Image1.Top)) then
        if(Plr.gmstart=true) then
                UI.RdrShape(shape1,shape2,image2)
        else
                UI.RdrShape(shape1,shape2,image1)
else
        if(Plr.gmstart=true) then
                UI.RdrShape(shape1,shape2,image2)
        else
                UI.RdrShape(shape1,shape2,image1);
end;

procedure TForm1.Image1MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
UI.CurX:=image1.Left+x;
UI.CurY:=image1.Top+y;
if(Plr.gmstart=true) then
                UI.RdrShape(shape1,shape2,image2)
        else
                UI.RdrShape(shape1,shape2,image1);
end;

procedure TForm1.FormCreate(Sender: TObject);
var i:Integer;
begin
DoubleBuffered := true;
Plr:=Tfield.create;
Cpu:=Tfield.create;
Brain:=Tbrain.create;
Cpu.init;
UI:=Tgraph.create;
shape1.Width:=(UI.SqrS+1)*UI.CurSize;
shape2.Width:=(UI.SqrS+1)*UI.CurSize;
UI.DrawField(image1,Cpu.Dim);
for i:=0 to cpu.Nship-1 do
        cpu.ShipLeft[i]:=cpu.Nship-i;
shape3.Left:=image1.Width+image1.Left+3*UI.SqrS;
shape4.Left:=image1.Width+image1.Left+3*UI.SqrS;
shape5.Left:=image1.Width+image1.Left+3*UI.SqrS;
shape6.Left:=image1.Width+image1.Left+3*UI.SqrS;
shape3.Top:=image1.Top+Ui.FieldTop;
shape4.Top:=shape3.Top+(UI.SqrS+1)*2;
shape5.Top:=shape4.Top+(UI.SqrS+1)*2;
shape6.Top:=shape5.Top+(UI.SqrS+1)*2;
Image2.Height:=Image1.Height;
Image2.Width:=Image1.Width;
Image2.Left:=2*shape6.Left-(image1.Left+image1.Width)+shape6.Width;
Image2.Top:=Image1.Top;
UI.DrawField(image2,Cpu.Dim);
edit1.Top:=shape3.Top;
edit1.Left:=shape3.Left-shed-edit1.Width;
edit2.Top:=shape4.Top;
edit2.Left:=shape4.Left-shed-edit2.Width;
edit3.Top:=shape5.Top;
edit3.Left:=shape5.Left-shed-edit3.Width;
edit4.Top:=shape6.Top;
edit4.Left:=shape6.Left-shed-edit4.Width;
edit5.Top:=shape3.Top;
edit5.Left:=shape3.Left+shed+shape3.Width;
edit6.Top:=shape4.Top;
edit6.Left:=shape4.Left+shed+shape4.Width;
edit7.Top:=shape5.Top;
edit7.Left:=shape5.Left+shed+shape5.Width;
edit8.Top:=shape6.Top;
edit8.Left:=shape6.Left+shed+shape6.Width;
edit1.Text:=inttostr(Plr.shipLeft[0]);
edit2.Text:=inttostr(Plr.shipLeft[1]);
edit3.Text:=inttostr(Plr.shipLeft[2]);
edit4.Text:=inttostr(Plr.shipLeft[3]);
edit5.Text:=inttostr(cpu.shipLeft[0]);
edit6.Text:=inttostr(cpu.shipLeft[1]);
edit7.Text:=inttostr(cpu.shipLeft[2]);
edit8.Text:=inttostr(cpu.shipLeft[3]);
label1.Hide;
label2.Hide;
shape1.Visible:=false;
shape2.Visible:=false;
Score:=Thighscore.create;
memo1.clear;
memo1.hide;
edit9.hide;
end;


procedure TForm1.Shape2MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
if ((UI.CurX>=Image1.Left) and (UI.CurX<=Image1.Left+Image1.Width) and (ui.CurY>=Image1.Top) and (UI.CurY<=Image1.Height+Image1.Top)) then
        if(Plr.gmstart=true) then
                UI.RdrShape(shape1,shape2,image2)
        else
                UI.RdrShape(shape1,shape2,image1)
else
        if(Plr.gmstart=true) then
                UI.RdrShape(shape1,shape2,image2)
        else
                UI.RdrShape(shape1,shape2,image1);
end;

procedure TForm1.Shape6MouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
begin
if(Plr.ShipLeft[3]>0) then begin
        UI.CurSize:=4;
        UI.DisShape(shape3,shape4,shape5,shape6);
        if(UI.Right=true) then begin
                shape1.Height:=(UI.SqrS+1);
                shape1.Width:=(UI.SqrS+1)*UI.CurSize;
                shape2.Height:=UI.SqrS+1;
                shape2.Width:=(UI.SqrS+1)*UI.CurSize;
        end
        else begin
                shape1.width:=(UI.SqrS+1);
                shape1.height:=(UI.SqrS+1)*UI.CurSize;
                shape2.width:=UI.SqrS+1;
                shape2.height:=(UI.SqrS+1)*UI.CurSize;
        end;
        shape1.Visible:=true;
        Dec(Plr.ShipLeft[3]);
        edit4.Text:=inttostr(plr.shipLeft[3]);
end;
end;


procedure TForm1.Shape5MouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
begin
if(Plr.ShipLeft[2]>0) then begin
        UI.CurSize:=3;
        UI.DisShape(shape3,shape4,shape5,shape6);
        if(UI.Right=true) then begin
                shape1.Height:=(UI.SqrS+1);
                shape1.Width:=(UI.SqrS+1)*UI.CurSize;
                shape2.Height:=UI.SqrS+1;
                shape2.Width:=(UI.SqrS+1)*UI.CurSize;
        end
        else begin
                shape1.width:=(UI.SqrS+1);
                shape1.height:=(UI.SqrS+1)*UI.CurSize;
                shape2.width:=UI.SqrS+1;
                shape2.height:=(UI.SqrS+1)*UI.CurSize;
        end;
        shape1.Visible:=true;
        Dec(Plr.ShipLeft[2]);
        edit3.Text:=inttostr(plr.shipLeft[2]);
end;
end;

procedure TForm1.Shape4MouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
begin
if(Plr.ShipLeft[1]>0) then begin
        UI.CurSize:=2;
        UI.DisShape(shape3,shape4,shape5,shape6);
        if(UI.Right=true) then begin
                shape1.Height:=(UI.SqrS+1);
                shape1.Width:=(UI.SqrS+1)*UI.CurSize;
                shape2.Height:=UI.SqrS+1;
                shape2.Width:=(UI.SqrS+1)*UI.CurSize;
        end
        else begin
                shape1.width:=(UI.SqrS+1);
                shape1.height:=(UI.SqrS+1)*UI.CurSize;
                shape2.width:=UI.SqrS+1;
                shape2.height:=(UI.SqrS+1)*UI.CurSize;
        end;
        shape1.Visible:=true;
        Dec(Plr.ShipLeft[1]);
        edit2.Text:=inttostr(plr.shipLeft[1]);
end;
end;

procedure TForm1.Shape3MouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
begin
if(Plr.ShipLeft[0]>0) then begin
        UI.CurSize:=1;
        UI.DisShape(shape3,shape4,shape5,shape6);
        if(UI.Right=true) then begin
                shape1.Height:=(UI.SqrS+1);
                shape1.Width:=(UI.SqrS+1)*UI.CurSize;
                shape2.Height:=UI.SqrS+1;
                shape2.Width:=(UI.SqrS+1)*UI.CurSize;
        end
        else begin
                shape1.width:=(UI.SqrS+1);
                shape1.height:=(UI.SqrS+1)*UI.CurSize;
                shape2.width:=UI.SqrS+1;
                shape2.height:=(UI.SqrS+1)*UI.CurSize;
        end;
        shape1.Visible:=true;
        Dec(Plr.ShipLeft[0]);
        edit1.Text:=inttostr(plr.shipLeft[0]);
end;
end;

procedure TForm1.Shape1MouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
begin
if(Button=mbleft) then begin
if(Plr.GmStart=false) then begin
if ((UI.CurX>=Image1.Left) and (UI.CurX<=Image1.Left+Image1.Width) and (ui.CurY>=Image1.Top) and (UI.CurY<=Image1.Height+Image1.Top)) then
        if( UI.PlaceShip(Plr.Dim,image1,Plr)=true) then begin
                shape1.Visible:=false;
                UI.EnebShape(shape3,shape4,shape5,shape6);
        end
        else
else    
end
else
begin
edit1.Text:=inttostr(Plr.shipLeft[0]);
edit2.Text:=inttostr(Plr.shipLeft[1]);
edit3.Text:=inttostr(Plr.shipLeft[2]);
edit4.Text:=inttostr(Plr.shipLeft[3]);
edit5.Text:=inttostr(cpu.shipLeft[0]);
edit6.Text:=inttostr(cpu.shipLeft[1]);
edit7.Text:=inttostr(cpu.shipLeft[2]);
edit8.Text:=inttostr(cpu.shipLeft[3]);
       if(UI.Strike(Cpu.Dim,Cpu,image2)=false) then begin
                if(Cpu.MaxShip=0) then begin
                        label1.Show;
                        shape1.Enabled:=false;
                        memo1.Show;
                        edit9.Show;
                        bitton3.show;
                        shape2.Enabled:=false;
                        end;
                UI.CpuStrike(Brain,Cpu.Dim,plr,image1);
                if(plr.MaxShip=0) then begin
                 shape1.Enabled:=false;
                 shape2.Enabled:=false;
                label2.show;
                end;
       end;
end;
end
else if (Button=mbright) then begin
if(UI.Right=true) then begin
        UI.Right:=false;
        shape1.width:=(UI.SqrS+1);
        shape1.height:=(UI.SqrS+1)*UI.CurSize;
        shape2.width:=UI.SqrS+1;
        shape2.height:=(UI.SqrS+1)*UI.CurSize;
end
else begin
        UI.Right:=true;
         shape1.Height:=(UI.SqrS+1);
        shape1.Width:=(UI.SqrS+1)*UI.CurSize;
        shape2.Height:=UI.SqrS+1;
        shape2.Width:=(UI.SqrS+1)*UI.CurSize;
end;
end;
end;

procedure TForm1.Button1Click(Sender: TObject);
var i,j:integer;
s:string;
begin
if(plr.MaxShip=0) then begin
UI.DisShape(shape3,shape4,shape5,shape6);
UI.CurSize:=1;
shape1.Width:=(UI.SqrS+1)*UI.CurSize;
shape1.Height:=(UI.SqrS+1)*UI.CurSize;
shape2.Width:=(UI.SqrS+1)*UI.CurSize;
shape2.Height:=(UI.SqrS+1)*UI.CurSize;
for i:=0 to cpu.Nship-1 do
        plr.ShipLeft[i]:=plr.Nship-i;
Plr.gmstart:=true;
Cpu.GmStart:=false;
shape1.Visible:=true;
end;
end;

procedure TForm1.Image2MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
UI.CurX:=image2.Left+x;
UI.CurY:=image2.Top+y;
 if(Plr.gmstart=true) then
                UI.RdrShape(shape1,shape2,image2)
        else
                UI.RdrShape(shape1,shape2,image1);
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
Score.Open;
label2.Hide;
Score.show(memo1);
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
Score.add(cpu.Move,edit9.Text);
score.Save;
end;

end.
