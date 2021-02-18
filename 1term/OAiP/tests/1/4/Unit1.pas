unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Grids, unit2;

type
  TForm1 = class(TForm)
    StringGrid1: TStringGrid;
    StringGrid2: TStringGrid;
    Label1: TLabel;
    Edit1: TEdit;
    Button1: TButton;
    Button2: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);

  private
    { Private declarations }
  public
    { Public declarations }
  end;


var
  Form1: TForm1;
   a:pmas;
   n,n1:integer;

implementation

{$R *.dfm}


procedure TForm1.Button1Click(Sender: TObject);
var l,i:integer; a:pmas;
begin
try
n:=strtoint(edit1.Text);
getmem(a,n*sizeof(integer));
for i:=1 to n do
a[i]:=strtoint(stringgrid1.cells[i-1,0]); except
showmessage('block1'); end;
del(a,n,n1);
stringgrid2.colCount:=n1;
for l:=1 to n1 do
stringgrid2.cells[l-1,0]:=inttostr(a[l]);
freemem(a,n*sizeof(integer));
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
n:=strtoint(edit1.Text);
stringgrid1.colcount:=n;
end;

end.
