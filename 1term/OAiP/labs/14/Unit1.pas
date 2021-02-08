unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, ExtCtrls,unit2;

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
    Button5: TButton;
    CheckBox1: TCheckBox;
    Edit8: TEdit;
    Label8: TLabel;
    RadioGroup1: TRadioGroup;
    RadioGroup2: TRadioGroup;
    Button4: TButton;
    Button7: TButton;
    Button6: TButton;
    Button8: TButton;
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
     procedure Button3Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
    procedure BitBtn1Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button6Click(Sender: TObject);
    procedure Button8Click(Sender: TObject);
    procedure Button7Click(Sender: TObject);
           private
    { Private declarations }
  public
    { Public declarations }
  end;

   var
  ft:textfile;
    nzap:integer;
    fz:tfile;
  FileNameZ, FileNameT : string;
  bdd:bd;
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
radiogroup2.itemindex:=0;
bdd:=bd.create;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
 nzap:=nzap+1;
bdd.incfile(nzap,checkbox1.Checked,memo1,fz,edit1,edit2,edit3,edit4,edit5,edit6,edit7);
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
bdd.readfile(fz,memo1,checkbox1.Checked);
 button1.Show;
end;


procedure TForm1.Button5Click(Sender: TObject);
var i:integer;
begin
if savedialog1.execute then begin
filenamet:=savedialog1.filename;
assignfile(ft,filenamet);
rewrite(ft); end;
bdd.mastofile(ft);
 end;

procedure TForm1.BitBtn1Click(Sender: TObject);
begin
closefile(fz);
end;


procedure TForm1.Button4Click(Sender: TObject);
begin
bdd.key:=strtoint(edit8.Text);
memo1.Clear;
case radiogroup1.ItemIndex of
0:bdd.linesearch(memo1);
1:bdd.dsearch(memo1);
end;
end;

procedure TForm1.Button6Click(Sender: TObject);
var i:integer;
begin
case radiogroup2.ItemIndex of
0:bdd.qs(1,bdd.dim);
1: bdd.slsearch(1,bdd.dim); end;
memo1.Clear;
for i:=1 to bdd.dim do
with bdd.team[i] do begin
memo1.Lines.Add('----------------------------');
memo1.Lines.Add('фио '+fio);
memo1.Lines.Add('страна '+str);
memo1.Lines.Add('команда '+tm);
memo1.Lines.Add('номер '+inttostr(num));
memo1.Lines.Add('возраст '+inttostr(age));
memo1.Lines.Add('рост '+floattostr(rst));
end;
end;

procedure TForm1.Button8Click(Sender: TObject);
begin
memo1.Clear;
bdd.age(memo1);
end;

procedure TForm1.Button7Click(Sender: TObject);
begin
bdd.key:=strtoint(edit8.Text);
bdd.delk;
end;

end.


