unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, Grids,mxarrays;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    StringGrid1: TStringGrid;
    BitBtn1: TBitBtn;
    BitBtn2: TBitBtn;
    Edit1: TEdit;
    Label3: TLabel;
    Label2: TLabel;
    Edit2: TEdit;
    Button1: TButton;
    procedure FormCreate(Sender: TObject);
    procedure BitBtn2Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations}
       end;
       type
    Mas=array[1..1] of char;
    Pmas=^mas;


var
  Form1: TForm1;
  ch:char;
  i,j,m,k,l:integer;
    a:pmas;
  mt:word;

implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
edit1.Text:='2';
edit2.Text:='7';
m:=strtoint(edit2.Text);
Randomize;
stringgrid1.colcount:=m;
for i:=1 to m do
stringgrid1.Cells[i-1,0]:=('i'+inttostr(i));
for i:=0 to m do
stringgrid1.Cells[i,1]:=chr(random(94)+33);
end;

procedure TForm1.BitBtn2Click(Sender: TObject);
begin try
k:=strtoint(edit1.Text);
if k<0 then  begin
  ShowMessage('В ячейке отсутствует значение, либо число введено неправильно');
  edit1.Color:=clred;  end;
    except on EConvertError do
    begin
     edit1.Color:=clred;
      ShowMessage('В ячейке отсутствует значение, либо число введено неправильно');
      Exit;
    end; end;
    if (k>=0) then begin
         mt:=sizeof (char);
getmem(a,mt*m);
 edit1.Color:=clwhite; l:=0;
for i:=1 to m do begin
if (length(stringgrid1.Cells[i-1,1])>1) then
l:=l+1; end;
 if l>0 then begin stringgrid1.color:=clred;
 ShowMessage('слишком много символов в одной ячейке'); end;
 if l=0 then begin
try
stringgrid1.color:=clwhite;
for i:=1 to m do
a[i]:=stringgrid1.Cells[i-1,1][1];
   except
  on ERangeError do
    begin
      ShowMessage('Выход за пределы массива. Уменьшите размер массива');
      Exit;
    end;
    on EArrayError do
    begin
      ShowMessage('ошибочный индекс массива,слишком большоe число элементов в массивe фиксированной длины');
      Exit;
    end;
    on EDivByZero do
    begin
      ShowMessage('Попытка целочисленного деления на ноль');
      Exit;
    end;
    on EOverFlow do
      begin
        MessageDlg('Переполнение при операции с плавающей точкой',mtError,[mbCancel],0);
        Exit;
      end;
    on EZeroDivide do
    begin
      ShowMessage('Деление на ноль числа с плавающей точкой');
      Exit;
    end;
      on EConvertError do
    begin
      ShowMessage('В ячейке отсутствует значение, либо число введено неправильно');
      Exit;
    end;
  else
    begin
      ShowMessage('Возникла неизвестная исключительная ситуация');
      Exit;
    end; end;
    try
for i:=1 to k do begin
ch:=a[m];
for j:=(m-1) downto 1 do
a[j+1]:=a[j];
a[1]:=ch;
end;
 except
             on EInvalidOp do
      begin
        MessageDlg('Неправильная операция с плавающей точкой',mtError,[mbCancel],0);
        Exit;
      end;
    on EOverFlow do
      begin
        MessageDlg('Переполнение при операции с плавающей точкой',mtError,[mbCancel],0);
        Exit;
      end;
       on EConvertError do
    begin
      ShowMessage('В ячейке отсутствует значение, либо число введено неправильно');
      Exit;
    end;
    else
      begin
        MessageDlg('Возникла неизвестная ситуация',mtError,[mbCancel],0);
        Exit;
      end;
 end;
for i:=1 to m do begin
stringgrid1.Cells[i-1,1]:=a[i]
end;
freemem(a,mt*m);
end; end;  end;

procedure TForm1.Button1Click(Sender: TObject);
begin
try
m:=strtoint(edit2.Text);
if (m<=0) then  begin
showMessage('В ячейке отсутствует значение, либо число введено неправильно');
edit2.Color:=clred; end;
if (m>0) then begin
edit2.Color:=clwhite;
Randomize;
stringgrid1.colcount:=m;
for i:=0 to m do
stringgrid1.Cells[i,1]:=chr(random(94)+33);
for i:=1 to m do
stringgrid1.Cells[i-1,0]:=('i'+inttostr(i)); end;
except
on EConvertError do
    begin  edit2.Color:=clred;
      ShowMessage('В ячейке отсутствует значение, либо число введено неправильно');
      Exit;
    end; end;

end;

end.
