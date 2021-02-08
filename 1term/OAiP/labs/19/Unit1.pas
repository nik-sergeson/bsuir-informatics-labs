unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs,unit2, StdCtrls, Buttons, Grids;

type
  TForm1 = class(TForm)
    StringGrid1: TStringGrid;
    Edit1: TEdit;
    Label1: TLabel;
    Edit2: TEdit;
    Label2: TLabel;
    BitBtn3: TBitBtn;
    BitBtn4: TBitBtn;
    Memo1: TMemo;
    BitBtn1: TBitBtn;
    procedure FormCreate(Sender: TObject);
    procedure BitBtn1Click(Sender: TObject);
    procedure BitBtn2Click(Sender: TObject);
    procedure BitBtn3Click(Sender: TObject);
    procedure BitBtn4Click(Sender: TObject);
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

procedure TForm1.FormCreate(Sender: TObject);
var c:tinf;
i:integer;
begin
he:=hesh.create(10);
he.n:=10;
he.m:=5;
  With StringGrid1 do begin
rowcount:=10;
        Cells[0,0]:='Ф.И.О.';
      Cells[1,0]:='Номер';
      Cells[0,1]:='Иванов А.А.';    Cells[1,1]:='100005';
      Cells[0,2]:='Петров С.И.';	  Cells[1,2]:='100002';
      Cells[0,3]:='Сидоров К.М.';   Cells[1,3]:='100004';
      Cells[0,4]:='Васильев М.К.';  Cells[1,4]:='100001';
      Cells[0,5]:='Смирнов В.К.';   Cells[1,5]:='100007';
      Cells[0,6]:='Мишин Т.В.';     Cells[1,6]:='100006';
      Cells[0,7]:='Долин А.К.';	    Cells[1,7]:='100008';
      Cells[0,8]:='Катаев А.М.';    Cells[1,8]:='100000';
      Cells[0,9]:='Рубан В.В.';	    Cells[1,9]:='100009';
      Cells[0,10]:='Шидлов А.С.';   Cells[1,10]:='100012';
                                   end;
 for i:=1 to he.n do begin
 c.num:=strtoint(stringgrid1.Cells[1,i]);
  c.fio:=(stringgrid1.Cells[0,i]);
  he.add(c);
end;  end;

procedure TForm1.BitBtn1Click(Sender: TObject);
begin
he.solv(memo1);
end;

procedure TForm1.BitBtn2Click(Sender: TObject);
begin
he.n:=strtoint(edit2.Text);
stringgrid1.RowCount:=strtoint(edit2.Text);
end;

procedure TForm1.BitBtn3Click(Sender: TObject);
var c:tinf;
i:integer;
begin
 c.num:=strtoint(edit1.Text);
  c.fio:=(edit2.Text);
  he.add(c);
he.print(memo1);
end;

procedure TForm1.BitBtn4Click(Sender: TObject);
begin
he.print(memo1);
end;

end.
