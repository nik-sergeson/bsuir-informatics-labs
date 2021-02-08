unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls, Math, Buttons;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Edit2: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    CheckBox1: TCheckBox;
    RadioGroup1: TRadioGroup;
    Memo1: TMemo;
    Label3: TLabel;
    Button1: TButton;
    procedure FormCreate(Sender: TObject);
      procedure Memo1Click(Sender: TObject);
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
Edit2.text:='0,356';
Memo1.Clear;
Memo1.Lines.Add('Results:');
RadioGroup1.ItemIndex:=0;
end;

procedure TForm1.Memo1Click(Sender: TObject);
var x,b,g,u:extended;
begin
Memo1.Clear;
Memo1.Lines.Add('Results');
x:=strtofloat(Edit1.Text);
Memo1.lines.add('x='+floattostrF(x,fffixed,8,4));
b:=strtofloat(Edit2.Text);
Memo1.lines.add('b='+floattostrF(b,fffixed,8,4));
case radiogroup1.ItemIndex of
0: u:=sinh(x);
1: u:=sqr(x);
2: u:=exp(x);
end;
if (0.5<x*b) and (x*b<10) then g:=exp(u-abs(b))
else if (0.1<x*b)and (x*b<0.5) then g:=sqrt(abs(u+b))
else g:=2*sqr(u);
if checkbox1.Checked then
memo1.Lines.Add('Value g='+inttostr(round(g)))
else memo1.Lines.Add('Value g='+floattostrf(g,ffgeneral,8,6));

end;

procedure TForm1.Button1Click(Sender: TObject);
begin
close;
end;

end.
