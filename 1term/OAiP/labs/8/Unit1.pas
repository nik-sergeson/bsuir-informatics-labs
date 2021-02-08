unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, ExtCtrls;

type
  TForm1 = class(TForm)
    OpenDialog1: TOpenDialog;
    SaveDialog1: TSaveDialog;
    Edit1: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Edit2: TEdit;
    Label3: TLabel;
    Edit3: TEdit;
    Edit4: TEdit;
    Label4: TLabel;
    Label5: TLabel;
    Edit5: TEdit;
    Label6: TLabel;
    Edit6: TEdit;
    Edit7: TEdit;
    Label7: TLabel;
    Button1: TButton;
    Button2: TButton;
    BitBtn1: TBitBtn;
    Memo1: TMemo;
    Button3: TButton;
    Button4: TButton;
    Button5: TButton;
    RadioGroup1: TRadioGroup;
    CheckBox1: TCheckBox;
    Button6: TButton;
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
     procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
    procedure BitBtn1Click(Sender: TObject);
    procedure Button6Click(Sender: TObject);
        private
    { Private declarations }
  public
    { Public declarations }
  end;
  type
  tstudent=record
  FIO:string[40];
  str:string[40];
  tm:string[40];
  num:integer  ;
  age:integer ;
  rst:extended;
  ves:extended ;  end;
   var
  fz:file of tstudent;
  ft:textfile;
  stud:array[1..100] of tstudent;
  nzap:integer;
  FileNameZ, FileNameT : string;
  var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
edit1.Clear;
edit2.Clear;
edit3.Clear;
edit4.Clear;
edit5.Clear;
edit6.Clear;
edit7.Clear;
memo1.Clear;
button1.Hide;
nzap:=0;
radiogroup1.itemindex:=0;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
nzap:=nzap+1;
with stud[nzap] do begin
fio:=edit1.Text;
str:=edit2.Text;
tm:=edit3.Text;
num:=strtoint(edit4.Text);
age:=strtoint(edit5.Text);
rst:=strtofloat(edit6.Text);
ves:=strtofloat(edit7.Text);
if checkbox1.Checked then begin
memo1.Lines.Add(inttostr(nzap)+' игрок');
memo1.Lines.Add('фио '+fio);
memo1.Lines.Add('страна '+str);
memo1.Lines.Add('команда '+tm);
memo1.Lines.Add('номер '+inttostr(num));
memo1.Lines.Add('возраст '+inttostr(age));
memo1.Lines.Add('рост '+floattostr(rst));
memo1.Lines.Add('вес '+floattostr(ves)); end; end;
write(fz,stud[nzap]);
edit1.Clear;
edit2.Clear;
edit3.Clear;
edit4.Clear;
edit5.Clear;
edit6.Clear;
edit7.Clear;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
opendialog1.Title:='создать новый файл';
if opendialog1.Execute then begin
filenamez:=opendialog1.FileName;
assignfile(fz,filenamez);
rewrite(fz); end;
button1.Show;
end;


procedure TForm1.Button3Click(Sender: TObject);
begin
memo1.Clear;
if opendialog1.Execute then begin
filenamez:=opendialog1.FileName;
assignfile(fz,filenamez);
reset(fz);end;
nzap:=0;
while not eof(fz) do begin
nzap:=nzap+1;
read(fz,stud[nzap]);
if checkbox1.Checked then begin
memo1.Lines.Add('----------------------------');
memo1.Lines.Add('фио '+stud[nzap].fio);
memo1.Lines.Add('страна '+stud[nzap].str);
memo1.Lines.Add('команда '+stud[nzap].tm);
memo1.Lines.Add('номер '+inttostr(stud[nzap].num));
memo1.Lines.Add('возраст '+inttostr(stud[nzap].age));
memo1.Lines.Add('рост '+floattostr(stud[nzap].rst));
memo1.Lines.Add('вес '+floattostr(stud[nzap].ves)); end;
end; button1.Show;
end;


procedure TForm1.Button4Click(Sender: TObject);
var s1,s2,s3:string;
m,n,j,i,l:integer;
sred,min1,min,sum:extended;
begin
min:=0;sred:=0;s1:='';min1:=0;
try
case radiogroup1.ItemIndex of
0:begin for l:=1 to nzap do begin
if stud[l].age>min then min:=stud[l].age; end; end;
3:begin for l:=1 to nzap do begin
if stud[l].rst>min then min:=stud[l].rst; end; end;
5:begin for l:=1 to nzap do begin
if stud[l].ves>min then min:=stud[l].ves; end; end; end;
except showmessage('found1');end;
for i:=1 to nzap do begin
if pos(stud[i].tm,s1)=0 then s1:=s1+stud[i].tm+' '; end;
while length(s1)>0 do begin
n:=pos(' ',s1);
s2:=copy(s1,1,n-1);
delete(s1,1,n);
m:=0; sum:=0;
for j:=1 to nzap do begin
if  pos(stud[j].tm,s2)>0 then begin
m:=m+1;
try
case radiogroup1.ItemIndex of
0:sum:=sum+stud[j].age;
1:sum:=sum+stud[j].age;
2:sum:=sum+stud[j].rst;
3:sum:=sum+stud[j].rst;
4:sum:=sum+stud[j].ves;
5:sum:=sum+stud[j].ves;
 end;
except showmessage('found2');end;
end;
 end;                         //min1 минимальный
try sred:=sum/m;            // min-максим эднмент
case radiogroup1.ItemIndex of
0: BEGIN if sred<min then begin min:=sred; s3:=s2;
end;  end;
1: BEGIN if sred>min1 then begin min1:=sred; s3:=s2;end;  end;
2:BEGIN if sred>min1 then begin min1:=sred; s3:=s2;end;  end;
3: begin if sred<min then begin min:=sred; s3:=s2;;end;  end;
4: BEGIN if sred>min1 then begin min1:=sred; s3:=s2;end;  end;
5: begin if sred<min then begin min:=sred; s3:=s2;end;  end; end;
except showmessage('found3');end;
end;
case radiogroup1.ItemIndex of
0:memo1.Lines.add('самая молодая команда-'+s3+' с средним возрастом'+floattostr(min));
1:memo1.Lines.add('самая старая команда-'+s3+' с средним возрастом'+floattostr(min1));
2:memo1.Lines.add('самая высокая команда-'+s3+' с средним возрастом'+floattostr(min1));
3:memo1.Lines.add('самая низкая команда-'+s3+' с средним возрастом'+floattostr(min));
4:memo1.Lines.add('самая весомая команда-'+s3+' с средним возрастом'+floattostr(min1));
5:memo1.Lines.add('самая худая команда-'+s3+' с средним возрастом'+floattostr(min));
  end; end;


procedure TForm1.Button5Click(Sender: TObject);
var i:integer;
begin
if savedialog1.execute then begin
filenamet:=savedialog1.filename;
assignfile(ft,filenamet);
rewrite(ft); end;
 for i:=1 to nzap do
 with stud[i] do  Writeln(Ft,i:4,'. ',fio,str,tm,num,age,rst,ves);

         CloseFile(Ft);
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
begin
closefile(fz);
end;


procedure TForm1.Button6Click(Sender: TObject);
var n,i:integer;
begin
n:=9;
seek(fz,n-1);
for i:=n-1 to filesize(fz)-2 do begin
seek(fz,i+1);
read(fz,stud[i]);
seek(fz,i);
write(fz,stud[i]); end;
seek(fz,filesize(fz)-1);
truncate(fz);
closefile(fz);
end;

end.
