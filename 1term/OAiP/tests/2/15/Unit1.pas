unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, Grids,unit2;

type
  TForm1 = class(TForm)
    StringGrid1: TStringGrid;
    BitBtn1: TBitBtn;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Button1: TButton;
    procedure BitBtn1Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  he:hesh;

implementation

{$R *.dfm}



procedure TForm1.BitBtn1Click(Sender: TObject);
begin
edit2.text:=he.read(strtoint(edit1.text)).fio;
end;

procedure TForm1.Button1Click(Sender: TObject);
var i,m:integer;
c:tinf;
begin
m:=strtoint(edit3.text);
he:=hesh.create(m);
stringgrid1.rowcount:=m;
for i:=0 to m-1 do begin
stringgrid1.cells[i,0]:=inttostr(m-i);
c.num:=m-i;
c.fio:='0';
he.add(c);
end;
end;

end.
