unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, Grids,unit2, StdCtrls, Buttons;

type
  TForm1 = class(TForm)
    StringGrid1: TStringGrid;
    BitBtn1: TBitBtn;
    Memo1: TMemo;
    Edit1: TEdit;
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
for i:=1 to 6 do begin
stringgrid1.cells[1,i]:=inttostr(random(18)+1);
stringgrid1.cells[2,i]:=inttostr(random(18)+1);  end;
tsolv:=solv.create;
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
var i:integer;
begin
tsolv.wmax:=strtoint(edit1.text);
for i:=1 to 6 do begin
tsolv.a[i].wes:=strtoint(stringgrid1.cells[1,i]);
tsolv.a[i].cost:=strtoint(stringgrid1.cells[2,i]); end;
tsolv.n:=6;
tsolv.opts:=[];
tsolv.s:=[]; tsolv.cmax:=0;
tsolv.pp(1);
for i:=1 to tsolv.n do
if (i in tsolv.s) then
memo1.lines.add(inttostr(i)+'          '+inttostr(tsolv.a[i].wes));
memo1.lines.add(inttostr(tsolv.cmax)+inttostr(tsolv.wc));
end;

end.
