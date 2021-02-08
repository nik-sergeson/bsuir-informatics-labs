unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls,unit2;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Button1: TButton;
    Edit2: TEdit;
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  tstack:stack;
implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
edit1.Text:='ab+c-';
tstack:=stack.create;
tstack.a['a']:=5;
tstack.a['b']:=5;
tstack.a['c']:=7;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
edit2.text:=floattostr(tstack.av(edit1.text));
end;

end.
