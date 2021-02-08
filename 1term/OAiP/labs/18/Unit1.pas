unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ComCtrls, StdCtrls,unit2, Grids, Buttons;

type
  TForm1 = class(TForm)
    TreeView1: TTreeView;
    Memo1: TMemo;
    StringGrid1: TStringGrid;
    Edit1: TEdit;
    BitBtn1: TBitBtn;
    BitBtn2: TBitBtn;
    BitBtn3: TBitBtn;
    BitBtn4: TBitBtn;
    BitBtn5: TBitBtn;
    procedure FormCreate(Sender: TObject);
    procedure BitBtn1Click(Sender: TObject);
    procedure BitBtn2Click(Sender: TObject);
    procedure BitBtn3Click(Sender: TObject);
    procedure BitBtn4Click(Sender: TObject);
    procedure BitBtn5Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  maple:solv;

implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
maple:=solv.create;
edit1.text:='10';

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

end;

procedure TForm1.BitBtn1Click(Sender: TObject);
begin
stringgrid1.rowcount:=strtoint(edit1.text)+1;
maple.n:=strtoint(edit1.text);
end;

procedure TForm1.BitBtn2Click(Sender: TObject);
var i:integer;
c:tinf;
begin
maple.n:=strtoint(edit1.text);
if maple.bl then maple.Delete(maple.proot);
for i:=1 to maple.n do begin
maple.a[i].num:=strtoint(stringgrid1.Cells[1,i]);
maple.a[i].fio:=(stringgrid1.Cells[0,i]);
maple.add(maple.a[i]);
end;
maple.view;
end;

procedure TForm1.BitBtn3Click(Sender: TObject);
begin
memo1.Clear;
maple.wrt1;
end;

procedure TForm1.BitBtn4Click(Sender: TObject);
var i:integer;
begin
maple.n:=strtoint(edit1.text);
for i:=1 to maple.n do begin
maple.a[i].num:=strtoint(stringgrid1.Cells[1,i]);
maple.a[i].fio:=(stringgrid1.Cells[0,i]); end;
if maple.bl then maple.Delete(maple.proot);
maple.blns(maple.n);
maple.view;
end;

procedure TForm1.BitBtn5Click(Sender: TObject);
begin
maple.left;
maple.view;
end;

end.
