unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls,unit2;

type
  TForm1 = class(TForm)
    Image1: TImage;
    Edit1: TEdit;
    Edit2: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Edit3: TEdit;
    Button1: TButton;
    Edit4: TEdit;
    Label4: TLabel;
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

procedure TForm1.Button1Click(Sender: TObject);
var x,y,h,r:extended;
begin
x:=strtofloat(edit1.Text);
y:=strtofloat(edit2.Text);
r:=strtofloat(edit3.Text);
h:=strtofloat(edit4.Text);
ris(x,y,r,h,image1);
end;

end.
