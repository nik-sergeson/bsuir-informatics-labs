unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ComCtrls, StdCtrls, Buttons, ExtCtrls,unit2, TeEngine, Series,
  TeeProcs, Chart;

type
  TForm1 = class(TForm)
    PageControl1: TPageControl;
    TabSheet1: TTabSheet;
    TabSheet2: TTabSheet;
    Label1: TLabel;
    Label2: TLabel;
    Edit1: TEdit;
    Label3: TLabel;
    Edit2: TEdit;
    Label4: TLabel;
    Edit3: TEdit;
    Label5: TLabel;
    Edit4: TEdit;
    RadioGroup1: TRadioGroup;
    Memo1: TMemo;
    BitBtn1: TBitBtn;
    BitBtn2: TBitBtn;
    TabSheet3: TTabSheet;
    Chart1: TChart;
    Series1: TLineSeries;
    Series2: TLineSeries;
    BitBtn3: TBitBtn;
    Button1: TButton;
    CheckBox1: TCheckBox;
    TabSheet4: TTabSheet;
    Image1: TImage;
    BitBtn4: TBitBtn;
    procedure FormCreate(Sender: TObject);
    procedure BitBtn1Click(Sender: TObject);
    procedure BitBtn3Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure BitBtn4Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  xn,xk,e:extended;
  m:word;

implementation

{$R *.dfm}
function sx(x:extended):extended;
var
sum,a:extended;
n:integer;
begin
sum:=x; a:=x; n:=0;
while abs(a)>e do begin
n:=n+1;
a:=a*sqr(x)/((2*n)*(2*n+1));
sum:=sum+a; end;
result:=sum; end;
function yx(x:extended):extended;begin
result:=(exp(x)-exp(-x))/2; end;


procedure TForm1.FormCreate(Sender: TObject);
begin
edit1.text:='0,1';
edit2.text:='1';
edit3.text:='9';
edit4.text:='0,0001';
radiogroup1.itemindex:=0;
checkbox1.Checked:=true;
end;


procedure TForm1.BitBtn1Click(Sender: TObject);
begin
memo1.clear;
memo1.lines.add('Результаты');
xn:=strtofloat(edit1.text);
memo1.lines.add('xn='+floattostrf(xn,fffixed,8,2));
xk:=strtofloat(edit2.text);
memo1.lines.add('xk='+floattostrf(xk,fffixed,8,2));
m:=strtoint(edit3.text);
memo1.lines.add('m='+inttostr(m));
e:=strtofloat(edit4.text);
memo1.lines.add('e='+floattostrf(e,fffixed,8,7));
case radiogroup1.ItemIndex of
0:begin
tabl(sx,xn,xk,e,m,memo1) end;
1:begin
tabl(yx,xn,xk,e,m,memo1)
end;
end;
end;

procedure TForm1.BitBtn3Click(Sender: TObject);
begin
xn:=strtofloat(edit1.text);
xk:=strtofloat(edit2.text);
m:=strtoint(edit3.text);
e:=strtofloat(edit4.text);
with Chart1 do
    begin
      LeftAxis.Automatic:=True;
      BottomAxis.Automatic:=True;
      SeriesList[0].Clear;
       SeriesList[1].Clear; end;
if checkbox1.Checked then begin
graf2(sx,yx,xn,xk,e,m,chart1);
end;
if checkbox1.Checked=false   then begin
 with Chart1 do
    begin
      LeftAxis.Automatic:=True;
      BottomAxis.Automatic:=True;
      SeriesList[0].Clear;
     case radiogroup1.ItemIndex of
0:begin
graf(sx,xn,xk,e,m,chart1) end;
1:begin
graf(yx,xn,xk,e,m,chart1)
end;   end; end;
end;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
 Chart1.CopyToClipboardMetafile(True);
end;

procedure TForm1.BitBtn4Click(Sender: TObject);
var x1,x2,y1,y2,r1,r2:integer;
begin
x1:=200; x2:=300;
y1:=200; y2:=300;
r1:=40;  r2:=50;
image1.Height:=400;
image1.Width:=400;
with image1.Canvas do begin
ellipse(x1-r1,y1-r1,x1+r1,y1+r1);
ellipse(x2-r2,y2-r2,x2+r2,y2+r2);

end;
end;
end.
