unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, Stdctrls, Math;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Memo1: TMemo;
    Button1: TButton;
    Label4: TLabel;
    procedure FormCreate(Sender: TObject);
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

procedure TForm1.FormCreate(Sender: TObject);
begin
Edit1.text:='16,55E-3';
Edit2.text:='-2,75';
Edit3.text:='0,15';
Memo1.clear;
end;

procedure TForm1.Button1Click(Sender: TObject);
var
x,y,z,a,b,c,d,s:extended;
begin
Memo1.clear;
Memo1.lines.add('Input:');
x:=strtofloat(Edit1.Text);
Memo1.lines.add('x='+floattostrF(x,fffixed,8,4));
y:=strtofloat(Edit2.Text);
Memo1.lines.add('y='+floattostrF(y,fffixed,8,4));
z:=strtofloat(Edit3.Text);
Memo1.lines.add('z='+floattostrF(z,fffixed,8,4));
a:=power(x,(1/3))+power(x,(y+2));
b:=sqrt(10*a);
c:=sqr(arcsin(z));
d:=abs(x-y);
s:=b*(c-d);
Memo1.lines.add('Output s='+floattostrF(s,fffixed,8,5));
end;

end.
