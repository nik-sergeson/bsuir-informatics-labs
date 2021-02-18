unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, Grids,unit2;

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
c:rec;
begin
tsolv:=solv.create;
tsolv.dim:=9;
for i:=0 to 8 do begin
stringgrid1.Cells[i,0]:=inttostr(9-i);
c.num:=9-i;
c.fio:='0';
tsolv.add(c);
end;
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
var c:rec;
i:integer;
begin
tsolv.sort;
for i:=0 to tsolv.dim-1 do begin
tsolv.read(c);
stringgrid1.Cells[i,0]:=inttostr(c.num);
end;
end;

end.
