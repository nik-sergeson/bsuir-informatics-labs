unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls,unit2;

type
  TForm1 = class(TForm)
    SaveDialog1: TSaveDialog;
    Button1: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Edit4: TEdit;
    Memo1: TMemo;
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  fl:textfile;
  m:integer;filename:string;


implementation

{$R *.dfm}
function sx(x:extended):extended;
  var s,b:extended;
  i:integer;
    begin
  s:=x;b:=x;
  for  i:=2 to m do begin
     b:=b*x/i;
    s:=s+b;
    end;
    result:=s;
    end;


procedure TForm1.Button1Click(Sender: TObject);
var a,b:extended;
n:integer;
begin
a:=strtofloat(edit1.Text);
b:=strtofloat(edit2.Text);
n:=strtoint(edit3.Text);
m:=strtoint(edit4.Text);
if savedialog1.execute then begin
filename:=savedialog1.filename;
assignfile(fl,filename);
rewrite(fl); end;
tabl(sx,a,b,n,memo1,fl);
closefile(fl);
end;

end.
