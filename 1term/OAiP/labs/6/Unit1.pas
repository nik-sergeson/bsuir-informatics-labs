unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, unit2, StdCtrls, Buttons,math, ExtCtrls;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Edit4: TEdit;
    RadioGroup1: TRadioGroup;
    Memo1: TMemo;
    BitBtn1: TBitBtn;
    BitBtn2: TBitBtn;
    procedure FormCreate(Sender: TObject);
    procedure BitBtn2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  xn,xk,e,n:extended;
  m:integer;

implementation
{$R *.dfm}

function sx(x:extended):extended;
var a,s,n:extended;
k:integer;
begin
a:=x; s:=x;n:=0; k:=-1;
try
while (abs(a)>e) do begin
n:=n+1;
a:=a*sqr(x)/((2*n)*(2*n+1));
s:=s+a;
end;
result:=s;
 except
   on EInvalidOp do
             k:=MessageDlg('Неправильная операция с плавающей точкой. '+
                               ' Продолжить вычисления?',mtError,[mbYes,mbNo],0);
   on EOverFlow do
             k:=MessageDlg('Переполнение при выполне-нии операции с'+
       ' плавающей точкой! Продолжить вычисления?',mtError,[mbYes,mbNo],0);
       else
             k:=MessageDlg('Возникла неизвестная исключительная ситуация!'+
                               ' Продолжить вычисления?',mtError,[mbYes,mbNo],0);
     end;
      case k of
       mrYes : Result:=0;
       mrNo  : Halt(1);
       end;
   end;
   function nx(x:extended):extended;
var a,n:extended;
k:integer;
begin
a:=x; n:=0; k:=-1;
try
while (abs(a)>e) do begin
n:=n+1;
a:=a*sqr(x)/((2*n)*(2*n+1));
end;
result:=n;
 except
   on EInvalidOp do
             k:=MessageDlg('Неправильная операция с плавающей точкой. '+
                               ' Продолжить вычисления?',mtError,[mbYes,mbNo],0);
   on EOverFlow do
             k:=MessageDlg('Переполнение при выполне-нии операции с'+
       ' плавающей точкой! Продолжить вычисления?',mtError,[mbYes,mbNo],0);
       else
             k:=MessageDlg('Возникла неизвестная исключительная ситуация!'+
                               ' Продолжить вычисления?',mtError,[mbYes,mbNo],0);
     end;
      case k of
       mrYes : Result:=0;
       mrNo  : Halt(1);
       end;
   end;
   function yx(x:extended):extended;
var s:extended;
begin try
s:=(exp(x)-exp(-x))/2;
result:=s; except
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
    end;end;
end;
procedure TForm1.FormCreate(Sender: TObject);
begin
memo1.clear;
edit1.text:='0,1';
edit2.text:='1';
edit3.text:='9';
edit4.text:='0,0001';
radiogroup1.itemindex:=0;
end;


procedure TForm1.BitBtn2Click(Sender: TObject);
begin
try

xn:=strtofloat(edit1.text);

xk:=strtofloat(edit2.text);

m:=strtoint(edit3.text);

e:=strtofloat(edit4.text);
 if (m<=0) then begin ShowMessage('НЕПРАВИЛЬНОЕ m');edit3.color:=clred;
 edit3.Visible:=false;
 sleep(200);
 edit3.Visible:=true;
  exit; end;
    if xk<=xn then begin ShowMessage('xn=>xk');
    edit1.color:=clred;
    edit2.color:=clred;
    edit1.Visible:=false;
 sleep(200);
 edit1.Visible:=true;
 edit2.Visible:=false;
 sleep(200);
 edit2.Visible:=true;
 exit; end;
    if (e<=0) then begin ShowMessage('неправильная точность');
    edit4.color:=clred;
    edit4.Visible:=false;
 sleep(200);
 edit4.Visible:=true;
  exit; end;
    memo1.clear;
    edit1.color:=clwhite;
    edit2.color:=clwhite;
    edit3.color:=clwhite;
    edit4.color:=clwhite;
memo1.lines.add('Результаты');
memo1.lines.add('xn='+floattostr(xn));
memo1.lines.add('xk='+floattostr(xk));
memo1.lines.add('m='+inttostr(m));
memo1.lines.add('e='+floattostr(e));
except on EDivByZero do
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
    end;  end;
   case radiogroup1.itemindex of
0: begin memo1.lines.add('вычесление s(x)');
tabl(sx,nx,xn,xk,e,m,memo1); end;
1: begin memo1.lines.add('вычесление y(x)');
tabl1(yx,xn,xk,e,m,memo1); end;
end;
end;
end.
