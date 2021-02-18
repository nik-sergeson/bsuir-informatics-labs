unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls,math, Buttons;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    Edit1: TEdit;
    Label2: TLabel;
    Edit2: TEdit;
    BitBtn1: TBitBtn;
    Edit3: TEdit;
    Edit4: TEdit;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Edit5: TEdit;
    procedure FormCreate(Sender: TObject);
    procedure Edit1KeyPress(Sender: TObject; var Key: Char);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}
procedure mingr(edit1,edit2,edit3,edit4,edit5:tedit);
var n,i,m,j,k,min,max:integer;
num:extended;
s1,s2,s3,s4,s5:string;
begin
m:=2;
s2:='';
s3:='';
s4:='';
s1:=edit1.text;
if length(s1)<1 then begin showmessage ('введите данные'); exit; end;
while(copy(s1,length(s1),1)=' ') do begin
delete(s1,length(s1),1); end;
s1:=s1+' ';
s2:=s1;
while length(s1)>0 do begin
num:=0;
n:=pos(' ',s1);
while (copy(s1,n+1,1)=' ') do begin
delete(s1,n+1,1); end;
for i:=1 to n-1 do begin
if (s1[i]<>'0') and (s1[i]<>'1')
then  begin
showmessage ('проверьте данные'); exit; end; end;
for j:=1 to n-1 do begin
num:=num+strtoint(s1[j])*power(m,n-1-j); end;
s4:=s4+floattostr(num)+' ';
s5:=s3+' ';
if ((n-1)=length(s2)) then  begin
while length(s5)>0 do begin
if (strtoint(copy(s5,1,pos(' ',s5)-1)))<>(strtoint(copy(s1,1,n-1))) then   begin
s3:=s3+' и '+copy(s1,1,n-1); end;
delete(s5,1,pos(' ',s5)); end; end;
if (n-1)<length(s2) then  begin
s2:=copy(s1,1,n-1);  s3:=s2; end;
delete(s1,1,n);
end;
edit4.Text:=s4;
if length(s3)>length(s2) then begin
edit3.Text:=s3;
edit3.Show ;end;
if length(s3)<=length(s2) then begin
edit2.text:=s2;
edit2.show; end;
max:=strtoint(copy(s4,1,pos(' ',s4)-1));
min:=max;
while length(s4)>0 do begin
k:=pos(' ',s4);
if strtoint(copy(s4,1,k-1))>max then max:=strtoint(copy(s4,1,k-1));
if strtoint(copy(s4,1,k-1))<min then min:=strtoint(copy(s4,1,k-1));
delete(s4,1,k); end;
if min=max then
edit5.Text:='они равны' else
edit5.Text:=inttostr(max)+' и '+inttostr(min);
end;

procedure TForm1.FormCreate(Sender: TObject);
begin
edit1.clear;
edit2.clear;
edit3.clear;
edit4.clear;
edit5.clear;
edit2.Hide;
edit3.Hide;
end;

procedure TForm1.Edit1KeyPress(Sender: TObject; var Key: Char);
begin
if key=#13 then
mingr(edit1,edit2,edit3,edit4,edit5);
end;

end.
