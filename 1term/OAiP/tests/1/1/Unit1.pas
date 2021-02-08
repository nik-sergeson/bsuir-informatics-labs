unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, unit2;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    Edit1: TEdit;
    Label2: TLabel;
    Edit2: TEdit;
    Label3: TLabel;
    Edit3: TEdit;
    Label4: TLabel;
    Edit4: TEdit;
    Memo1: TMemo;
    Button1: TButton;
    procedure FormKeyPress(Sender: TObject; var Key: Char);
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  x0,x1,a,e:extended;

implementation

{$R *.dfm}

procedure TForm1.FormKeyPress(Sender: TObject; var Key: Char);
begin
if key=#13 then begin
x0:=strtofloat(edit1.Text);
x1:=strtofloat(edit2.Text);
a:=strtofloat(edit3.Text);
e:=strtofloat(edit4.Text);
fun(x0,x1,a,e,memo1);
end; end;

procedure TForm1.FormCreate(Sender: TObject);
begin
edit1.Text:='1';
edit2.Text:='1';
edit3.Text:='4';
edit4.Text:='0,01';
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
x0:=strtofloat(edit1.Text);
x1:=strtofloat(edit2.Text);
a:=strtofloat(edit3.Text);
e:=strtofloat(edit4.Text);
fun(x0,x1,a,e,memo1);
end;

end.
