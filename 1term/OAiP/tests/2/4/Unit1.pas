unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs,unit2, StdCtrls, Buttons, Grids;

type
  TForm1 = class(TForm)
    StringGrid1: TStringGrid;
    BitBtn1: TBitBtn;
    procedure FormCreate(Sender: TObject);
    procedure BitBtn1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  tsolv:solv;
implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
var i:integer;
begin
tsolv:=solv.Create;
randomize;
for i:=1 to 10 do
stringgrid1.cells[i,1]:=inttostr(random(150));
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
var i:integer;
begin
for i:=1 to 10 do
tsolv.a[i].fio:=strtoint(stringgrid1.cells[i,1]);
tsolv.sort(1,10);
for i:=1 to 10 do
stringgrid1.cells[i,1]:=inttostr(tsolv.a[i].fio);
end;

end.
