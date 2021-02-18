unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, Grids,unit2;

type
  TForm1 = class(TForm)
    StringGrid1: TStringGrid;
    StringGrid2: TStringGrid;
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
  solv:tsolv;

implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
var i:integer;
begin
randomize;
solv:=tsolv.create;
for i:=1 to 5 do begin
stringgrid1.cells[i,1]:=inttostr(i);
stringgrid1.cells[i,2]:=inttostr(random(150));
end;
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
var i:integer;
begin
for i:=1 to 5 do begin
solv.a[i].name:=strtoint(stringgrid1.cells[i,2]);
solv.a[i].num:=strtoint(stringgrid1.cells[i,1]);
end;
solv.sort(1,5);
for i:=1 to 5 do
stringgrid2.cells[i,1]:=inttostr((solv.a[i].name));
end;

end.
