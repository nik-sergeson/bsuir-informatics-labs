unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, unit2;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Edit2: TEdit;
    Label3: TLabel;
    Edit3: TEdit;
    Memo1: TMemo;
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}
function sn(x:extended):extended;
begin
result:=sqr(sin(x));
end;
procedure TForm1.Button1Click(Sender: TObject);
var a,b:extended;
n:integer;
begin
a:=strtofloat(edit1.Text);
b:=strtofloat(edit2.Text);
n:=strtoint(edit3.Text);
memo1.lines.Add(floattostr(tabl(a,b,n,sn)));
end;

end.
 