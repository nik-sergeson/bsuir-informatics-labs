unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs,Grids,Stdctrls,mxarrays, Buttons;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Edit2: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    StringGrid1: TStringGrid;
    Button1: TButton;
    Button2: TButton;
    BitBtn1: TBitBtn;
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;
   const Nmax=10;
var
  Form1: TForm1;
  A:array[1..Nmax,1..Nmax]of extended;
     N,M,i,j,l:integer;
     r:extended;
  implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
N:=3;
M:=3;
Edit1.Text:=floattostr(N);
Edit2.Text:=floattostr(M);
StringGrid1.RowCount:=N+1;
StringGrid1.ColCount:=M+1;
StringGrid1.Cells[0,0]:='Array:';
for i:=1 to N do  begin
StringGrid1.Cells[0,i]:='i='+inttostr(i);
StringGrid1.Cells[i,0]:='j='+inttostr(i); end;
for i:=1 to M do
for j:=1 to N do StringGrid1.Cells[i,j]:=floattostr(random(100));
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
try
N:=strtoint(edit1.Text);
M:=strtoint(edit2.Text);
if (n<=0) or (m<=0) then
ShowMessage('В tedit число введено неправильно')
else  begin
 StringGrid1.RowCount:=N+1;
StringGrid1.ColCount:=M+1;
for i:=1 to N do
StringGrid1.Cells[0,i]:='i='+inttostr(i);
for i:=1 to M do
StringGrid1.Cells[i,0]:='j='+inttostr(i);
for i:=1 to M do
for j:=1 to N do StringGrid1.Cells[i,j]:=floattostr(random(100));  end;
except
on EConvertError do
    begin
      ShowMessage('В tedit отсутствует значение, либо число введено неправильно');
      Exit;
    end;  end;
end;  

procedure TForm1.Button2Click(Sender: TObject);
begin  {$R+} {$Q+ }  { $С+ }
 try
  for i:=1 to M do
    for j:=1 to N do
      A[i,j]:=StrToFloat(StringGrid1.Cells[j,i]);
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
    end;
 end; try
  for i:=2 to N do
  for j:=n downto i do
  if  a[j,1]<a[j-1,1] then begin
  for l:=1 to M do begin
  r:=a[j,l];
  a[j,l]:=a[j-1,l];
  a[j-1,l]:=r;
  end;  end;
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
       for i:=1 to M do
    for j:=1 to N do
      StringGrid1.Cells[j,i]:=FloatToStr(A[i,j]);
end;

end.
