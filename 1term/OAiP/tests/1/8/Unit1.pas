unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, TeEngine, Series, ExtCtrls, TeeProcs, Chart,unit2;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    Edit1: TEdit;
    Label2: TLabel;
    Edit2: TEdit;
    Edit3: TEdit;
    Label3: TLabel;
    Chart1: TChart;
    Series1: TLineSeries;
    BitBtn1: TBitBtn;
    Series2: TLineSeries;
    procedure BitBtn1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;
 var
  Form1: TForm1;

implementation

{$R *.dfm}
function comp(o:extended):complex;
var a,z:extended;
x,y:complex;
begin
x.re:=2; x.im:=sqr(o);
y.im:=-2; y.re:=o;
z:=sqr(y.re)+sqr(y.im);
comp.re:=(x.re*y.re+x.im*y.im)/z;
comp.im:=-(x.re*y.im-x.im*y.re)/z;
end;
procedure TForm1.BitBtn1Click(Sender: TObject);
var a,b:extended;
n:integer;
begin
a:=strtofloat(edit1.Text);
b:=strtofloat(edit2.Text);
n:=strtoint(edit3.Text);
tabl(a,b,n,comp,chart1);
end;

end.
