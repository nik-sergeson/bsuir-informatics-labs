unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls,unit2;

type
  TForm1 = class(TForm)
    Image1: TImage;
    Label1: TLabel;
    Edit1: TEdit;
    Label2: TLabel;
    Edit2: TEdit;
    Label3: TLabel;
    Edit3: TEdit;
    Label4: TLabel;
    Edit4: TEdit;
    Button1: TButton;
    Label5: TLabel;
    Edit5: TEdit;
    Label6: TLabel;
    Edit6: TEdit;
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  m:integer;

implementation

{$R *.dfm}
function sx(x:extended):extended;
var a,s:extended;
i:integer;
begin
a:=x; s:=x;
for i:=2 to m do begin
a:=a*x/i;
s:=s+a; end;
result:=s;
end;

procedure TForm1.Button1Click(Sender: TObject);
var ymax,ymin,a,b:extended;
n:integer;
begin
a:=strtofloat(edit1.Text);
b:=strtofloat(edit2.Text);
m:=strtoint(edit4.Text);
n:=strtoint(edit3.Text);
ymax:=strtofloat(edit6.Text);
ymin:=strtofloat(edit5.Text);
graf(a,b,ymax,ymin,m,n,sx,image1);
end;

end.
