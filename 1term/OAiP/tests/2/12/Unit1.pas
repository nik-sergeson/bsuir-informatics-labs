unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs,unit2, StdCtrls, Buttons, Grids;

type
  TForm1 = class(TForm)
    StringGrid1: TStringGrid;
    BitBtn1: TBitBtn;
    Memo1: TMemo;
    procedure FormCreate(Sender: TObject);
    procedure BitBtn1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  tree:solv;

implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
var i:integer;
c:tinf;
begin
tree:=solv.create;
for i:=0 to 8 do begin
stringgrid1.cells[i,0]:=inttostr(9-i);
c.num:=9-i;
c.fio:='0';
tree.a[i]:=c;
end;
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
begin
tree.blns(0,8);
tree.poisk;
end;

end.
