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
    StringGrid3: TStringGrid;
    BitBtn2: TBitBtn;
    procedure FormCreate(Sender: TObject);
    procedure BitBtn1Click(Sender: TObject);
    procedure BitBtn2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  s:solv;
implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
var i:integer;
c:rec;
begin
s:=solv.create;
for i:=1 to 3 do begin
stringgrid3.cells[0,i]:=inttostr(i);
stringgrid3.cells[1,i]:=inttostr(random(18));
c.num:=i;
c.fio:=strtoint(stringgrid3.cells[1,i]);
s.addlast(c);
end;
stringgrid1.cells[0,0]:=inttostr(s.n1+1);
 end;

procedure TForm1.BitBtn1Click(Sender: TObject);
var c:rec;
begin
c.num:=s.n1+1;
c.fio:=strtoint(stringgrid1.cells[1,0]);
stringgrid1.cells[0,0]:=inttostr(s.n1+2);
s.addlast(c);
s.update(stringgrid3);
end;

procedure TForm1.BitBtn2Click(Sender: TObject);
var c:rec;
begin
s.read1(c);
stringgrid2.cells[0,0]:=inttostr(c.num);
stringgrid2.cells[1,0]:=inttostr(c.fio);
s.update(stringgrid3);
end;

end.
