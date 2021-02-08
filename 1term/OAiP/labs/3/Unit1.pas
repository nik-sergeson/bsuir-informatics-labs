unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Extctrls, Buttons;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    Edit1: TEdit;
    Edit2: TEdit;
    Label2: TLabel;
    Edit3: TEdit;
    Edit4: TEdit;
    Label4: TLabel;
    Memo1: TMemo;
    Button1: TButton;
    Label5: TLabel;
    Label6: TLabel;
    BitBtn1: TBitBtn;
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
Edit1.text:='0,1';
Edit2.text:='1';
Edit3.text:='';
Edit4.text:='0,0001';
memo1.Clear;
Memo1.Lines.Add('Results');
memo1.Lines.Add('Enter m');
end;

procedure TForm1.Button1Click(Sender: TObject);
var
m,xn,xk,x,h,e,a,s,y,l:extended;
n,z:integer;
begin
memo1.Clear;
Memo1.Lines.Add('Results');
memo1.Lines.Add('Enter m');
xn:=strtofloat(Edit1.Text);
Memo1.lines.add('xn='+floattostrF(xn,fffixed,6,2));
xk:=strtofloat(Edit2.Text);
Memo1.lines.add('xk='+floattostrF(xk,fffixed,6,2));
m:=strtofloat(Edit3.Text);
Memo1.lines.add('m='+floattostrF(m,fffixed,8,3));
e:=strtofloat(Edit4.Text);
Memo1.lines.add('e='+floattostrF(e,fffixed,8,4));
h:=(xk-xn)/m;
Memo1.lines.add('h='+floattostrF(h,fffixed,8,3));
z:=0;
l:=e;
while (l<1) or (l=1) do begin
l:=l*10;
z:=z+1;
end;
x:=xn;
repeat
a:=x; s:=x; n:=0;
while abs(a)>e do begin
n:=n+1;
a:=a*sqr(x)/((2*n)*(2*n+1));
s:=s+a;
end;
y:=(exp(x)-exp(-x))/2;
memo1.lines.add('If x='+floattostrf(x,fffixed,6,2)+' Summ='
+floattostrf(s,fffixed,8,z)+' y='+floattostrf(y,fffixed,8,z)+
' n='+inttostr(n));
x:=x+h;
until x>(xk+h/2);
end;

end.
