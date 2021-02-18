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
StringGrid1.Cells[0,0]:='Вес';
  StringGrid1.Cells[0,1]:='22';
  StringGrid1.Cells[0,2]:='11';
  StringGrid1.Cells[0,3]:='12';
  StringGrid1.Cells[0,4]:='13';
  StringGrid1.Cells[0,5]:='14';
  StringGrid1.Cells[0,6]:='15';
  StringGrid1.Cells[0,7]:='16';
  StringGrid1.Cells[0,8]:='17';
  StringGrid1.Cells[0,9]:='18';
  StringGrid1.Cells[0,10]:='19';
  StringGrid1.Cells[1,0]:='Цена';
  StringGrid1.Cells[1,1]:='18';
  StringGrid1.Cells[1,2]:='20';
  StringGrid1.Cells[1,3]:='17';
  StringGrid1.Cells[1,4]:='19';
  StringGrid1.Cells[1,5]:='16';
  StringGrid1.Cells[1,6]:='21';
  StringGrid1.Cells[1,7]:='27';
  StringGrid1.Cells[1,8]:='23';
  StringGrid1.Cells[1,9]:='25';
  StringGrid1.Cells[1,10]:='24';
tsolv:=solv.create;
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
var i:integer;
begin
tsolv.wmax:=strtoint(edit1.text);
tsolv.oct:=0;
for i:=1 to 9 do begin
tsolv.a[i].wes:=strtoint(stringgrid1.cells[0,i]);
tsolv.a[i].cost:=strtoint(stringgrid1.cells[1,i]);
tsolv.oct:=tsolv.oct+tsolv.a[i].cost;
 end;
tsolv.n:=9;
tsolv.opts:=[]; tsolv.wt:=0;
tsolv.s:=[]; tsolv.cmax:=0;
tsolv.mves;
for i:=1 to tsolv.n do
if (i in tsolv.s) then
memo1.lines.add(inttostr(i)+'          '+inttostr(tsolv.a[i].wes));
memo1.lines.add(inttostr(tsolv.cmax)+inttostr(tsolv.wc));
end;

end.
